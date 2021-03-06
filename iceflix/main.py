"""Module containing a template for a main service."""

import logging
import uuid
import sys
import argparse

import Ice
Ice.loadSlice('iceflix.ice')
import IceStorm


import IceFlix
"""from Iceflix.service_announcement import (
    ServiceAnnouncementsListener,
    ServiceAnnouncementsSender,
)"""

from service_announcement import (
    ServiceAnnouncementsListener,
    ServiceAnnouncementsSender,
)

EXIT_OK = 0
BAD_COMMAND_LINE = 1


class Main(IceFlix.Main):
    """Servant for the IceFlix.Main interface.

    Disclaimer: this is demo code, it lacks of most of the needed methods
    for this interface. Use it with caution
    """

    def __init__(self):
        """Create the Main servant instance."""
        self.service_id = str(uuid.uuid4())

    def share_data_with(self, service):
        """Share the current database with an incoming service."""
        service.updateDB(None, self.service_id)

    def getAuthenticator(): # throws TemporaryUnavailable
        """Returns a proxy to an authentication service"""

        return "Authenticator*" 

    def getCatalog(): # throws TemporaryUnavailable
        """Returns a proxy to a catalog service"""

        return "MediaCatalog*"

    def updateDB(self, values, service_id, current):
        """Receives an updated service database provided by another instance of this service"""
        # pylint: disable=invalid-name,unused-argument
        """Receives the current main service database from a peer."""
        logging.info(
            "Receiving remote data base from %s to %s", service_id, self.service_id
        )

    def isAdmin(userToken):
        """Returns a boolean value to check if the provided token corresponds or not with the administrative one"""
        value = False
        if userToken == "administrative":
            value = True

        return value


class MainApp(Ice.Application):
    """Example Ice.Application for a Main service."""

    def __init__(self):
        super().__init__()
        self.servant = Main()
        self.proxy = None
        self.adapter = None
        self.announcer = None
        self.subscriber = None

    def setup_announcements(self):
        """Configure the announcements sender and listener."""

        communicator = self.communicator()
        topic_manager = IceStorm.TopicManagerPrx.checkedCast(
            communicator.propertyToProxy("IceStorm.TopicManager"),
        )

        try:
            topic = topic_manager.create("ServiceAnnouncements")
        except IceStorm.TopicExists:
            topic = topic_manager.retrieve("ServiceAnnouncements")

        self.announcer = ServiceAnnouncementsSender(
            topic,
            self.servant.service_id,
            self.proxy,
        )

        self.subscriber = ServiceAnnouncementsListener(
            self.servant, self.servant.service_id, IceFlix.MainPrx
        )

        subscriber_prx = self.adapter.addWithUUID(self.subscriber)
        topic.subscribeAndGetPublisher({}, subscriber_prx)

    def run(self, args):
        """Run the application, adding the needed objects to the adapter."""
        logging.info("Running Main application")
        comm = self.communicator()
        self.adapter = comm.createObjectAdapter("Main")
        self.adapter.activate()

        self.proxy = self.adapter.addWithUUID(self.servant)

        self.setup_announcements()
        self.announcer.start_service()

        self.shutdownOnInterrupt()
        comm.waitForShutdown()

        self.announcer.stop()
        return 0


def parse_commandline():
    '''Parse and check commandline'''
    parser = argparse.ArgumentParser('IceDungeon Local Game')
    parser.add_argument('PROXY',nargs='+', default=None,help='Proxy GameServer')
    parser.add_argument(
        '-p', '--player', default=DEFAULT_HERO, choices=game.common.HEROES,
        dest='hero', help='Hero to play with'
    )
    options = parser.parse_args()

    return options


def main(argv):
    '''Iniciar aplicacion'''
    user_options = parse_commandline()
    if not user_options:
        return BAD_COMMAND_LINE
    start_app = MainApp(user_options)
    start_app.main(argv)

    return EXIT_OK


if __name__ == '__main__':
    sys.exit(main(sys.argv))