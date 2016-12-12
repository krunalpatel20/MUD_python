#
# Krunal Patel
# Builder class to build a room
#
from mud.room import Room

class Builder:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.z = 0
        self.transparency = False

    def setX(self, x):
        self.x = x

    def setY(self, y):
        self.y = y

    def setZ(self, z):
        self.z = z

    def buildRoom(self):
        self.transparency = Room.checkOpacity(self.x,self.y,self.z)
        room = Room(self.x, self.y, self.z)
        return room
