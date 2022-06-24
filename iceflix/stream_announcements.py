
class StreamController:
    def getSDP(userToken, port): #throws Unauthorized;
        return ""
    def getSyncTopic():
        return ""
    def refreshAuthentication(userToken): #throws Unauthorized;
        print("")
    def stop():
        print("")

class StreamSync:
    def requestAuthentication():
        print("")
        
class MediaUploader:
    def receive(size):
        return "Bytes"
    def close():
        print("")

class StreamProvider:
    def getStream(mediaId, userToken): # throws Unauthorized, WrongMediaId;
        return "StreamController*"
    def isAvailable(mediaId):
        return "bool"
    def reannounceMedia(srvId): # throws UnknownService;
        print("")

    def uploadMedia(fileName, uploader, adminToken): # throws Unauthorized, UploadError;
        return ""
    def deleteMedia(mediaId, adminToken): # throws Unauthorized, WrongMediaId:
        print("")

class StreamAnnouncements:
    def newMedia(mediaId, initialName, srvId):
        """// Emitted then media is removed from the StreamProvider()"""
        print("")
    def removedMedia(mediaId, srvId):
        print("")