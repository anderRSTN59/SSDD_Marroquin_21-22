
USERS_FILE = 'users.json'

class Authenticator(Iceflix.Authenticator):
    
    def __init__(self):
        self._users_ = {}
        self._active_tokens_ = set()
        if os.path.exists(USERS_FILE):
            self.refresh()
        else:
            self.__commit__()
        

    def refreshAuthorization(user, passwordHash): #throws Unauthorized
        return " "

    def isAuthorized(userToken):
        value = False
        if userToken == "existe userToken":
            value = True

        return value

    def whois (userToken): #throws Unauthorized
        return " "

    def addUser(user, passwordHash, adminToken): #throws Unauthorized, TemporaryUnavailable
        print(2)

    def removeUser(user, adminToken): #throws Unauthorized, TemporaryUnavailable
        print(2)

    def updateDB(currentDatabase, srvId): #throws UnknownService
        print(2)

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
