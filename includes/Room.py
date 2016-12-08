#
# Krunal Patel
# Room class for all the rooms
#

import random

class Room:

    descriptions = [
        'You are in a beautiful garden. Enjoy the roses!',
        'You are in a dining room. Enjoy some food!',
        'You are in a living room. Enjoy watching TV!',
        'You are in the bedroom. Go to sleep!',
        'You are in the class room. This class room has 45 students'
    ]

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.transparency = Room.checkOpacity(self.x, self.y, self.z)
        self.description = Room.descriptions[random.randrange(0, len(Room.descriptionse))]
        self.name = self.x + '' + self.y + '' + self.z;

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getZ(self):
        return self.z

    def getDesciption(self):
        return self.description

    def getName(self):
        return self.name

    def getOpacity(self):
        return self.transparency



    @staticmethod
    def checkOpacity(x,y,z):
        trans = True
        if z%2==0 and y%2==0 and x%2==0:
            trans = False
        elif z%2!=0 and y%2!=0 and x%2!=0:
            trans = False

        return trans


