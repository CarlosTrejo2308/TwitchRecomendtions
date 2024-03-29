class Channel:
    def __init__(self, id, ponderation = 0, name = ""):
        self.id = id
        self._ponderation = ponderation
        #self.followers = [] #Not used in this implimentation
        self.blocked = False
        self.name = name

    def addPonderation(self, num):
        if(not self.blocked):
            self._ponderation += num
        else:
            return -1

    def multiplyPonderation(self, num):
        if(not self.blocked):
            self._ponderation *= num
        else:
            return -1

    def resetPonderation(self):
        if(not self.blocked):
            self._ponderation = 0
        else:
            return -1

    # def changeId(self, id):
    #     self.id = id

    #Not used tho
    # def addFollower(self, channel):
    #     self.followers.append(channel)
    #
    # def removeFollower(self, channel):
    #     self.followers.remove(channel)
    #
    # def getFollowers(self):
    #         return self.followers

    def block(self, b):
        self.blocked = b

        if self.blocked:
            self._ponderation = -9999999
        else:
            self.resetPonderation()

    def toString(self):
        return ("name: ", self.name, " id: ", self.id, " ponderation: ", self._ponderation, " blocked: ", self.blocked)
