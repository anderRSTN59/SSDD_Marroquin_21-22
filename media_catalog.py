
def getTile(mediaId, userToken): #throws WrongMediaId, TemporaryUnavailable, Unauthorized:

    return "media"
def getTilesByName(name, exact):
    
    return "stringList"

def getTilesByTags(tags, includeAllTags, userToken): #throws Unauthorized

    return "stringList"

def addTags(mediaId, tags, userToken): #throws Unauthorized, WrongMediaId:
    print ("tags")

def removeTags(mediaId, tags, userToken): #throws Unauthorized, WrongMediaId:
    print ("tags")

def renameTile(mediaId, name, adminToken): #throws Unauthorized, WrongMediaId:
    print ("tags")

def updateDB(catalogDatabase, srvId): #throws UnknownService:
    print ("tags")