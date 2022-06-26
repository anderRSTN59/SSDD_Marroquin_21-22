#!/usr/bin/python3 -u
# -*- coding: utf-8 -*-

import sys
import signal
import random
import os
import time
import json
import logging

import Ice
Ice.loadSlice('Iceflix.ice')
import Iceflix


USERS_FILE = 'users.json'
USERS_FILE = 'users.json'
PASSWORD_HASH = 'password_hash'
CURRENT_TOKEN = 'current_token'
TOKEN_SIZE = 40

class Authenticator(Iceflix.Authenticator):
    
    def __init__(self):
        self._users_ = {}
        self._active_tokens_ = set()
        if os.path.exists(USERS_FILE):
            self.updateDB()
        else:
            self.__commit__()


    def __commit__(self):
        logging.debug('Actualizada la database de usuarios')
        with open(USERS_FILE, 'w') as contents:
            json.dump(self._users_, contents, indent=4, sort_keys=True)


    def refreshAuthorization(self, user, passwordHash): #throws Unauthorized

        while True:
            time.sleep(120)
            if self.isAuthorized(user):
                return passwordHash
            else:
                print("Usuario no autorizado")

    def isAuthorized(self, userToken):
        value = False
        if userToken == "existe userToken":
            value = True

        return value

    def whois (self, userToken): #throws Unauthorized
        return " "

    def addUser(self, user, passwordHash, adminToken): #throws Unauthorized, TemporaryUnavailable
        print(2)

    def removeUser(self, user, adminToken): #throws Unauthorized, TemporaryUnavailable
        print(2)

    def updateDB(self, currentDatabase, srvId): #throws UnknownService
        '''Actualiza la BBDD de Usuarios'''
        logging.debug('Cargando Database')
        with open(USERS_FILE, 'r') as contents:
            self._users_ = json.load(contents)
        self._active_tokens_ = set([
            user.get(CURRENT_TOKEN, None) for user in self._users_.values()
        ])

class Server(Ice.Application):
    '''Servidor Servicio de Autenticacion'''

    def run (self, args):
        '''Server loop'''
        logging.debug('Iniciando servicio de autenticacion')
        servant = Authenticator()
        signal.signal(signal.SIGUSR1, servant.updateDB)

        adapter = self.communicator().createObjectAdapter('AuthenticationAdapter')
        proxy = adapter.add(servant, self.communicator().stringToIdentity('default'))
        adapter.addDefaultServant(servant, '')
        adapter.activate()
        logging.debug('Adapter ready, servant proxy: {}'.format(proxy))
        print('"{}"'.format(proxy), flush=True)

        logging.debug('Entering server loop...')
        self.shutdownOnInterrupt()
        self.communicator().waitForShutdown()

        return 0


class UserUpdates:
    def newUser(user, passwordHash, srvId):
        new_user = user, passwordHash

    def newToken(user, userToken, srvId):
        print ("")

class Revocations:
    def revokeToken(userToken, srvId):
        print("revoked token")

    def revokeUser(user, srvId):
        print("revoked user")
