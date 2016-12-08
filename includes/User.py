#
# Krunal Patel
# User container class
#

import random
from includes.Builder import Builder
from includes.Room import Room
from includes.Database import Database

class User:
    user = None
    MAX_WIDTH = 3
    MAX_LENGTH = 3
    MAX_HEIGHT = 3

    def __init__(self):
        self.username = ''
        self.currRoom = None
        self.password = ''

    def getInstance(self):
        if User.user == None:
            User.user = User()

        return User.user

    def setUsername(self, username):
        self.username = username

    def getUsername(self):
        return self.username

    def setRoom(self, room):
        self.currRoom = room

    def createRoom(self, x, y, z):
        if x==False or y==False or z==False:
            while True:
                x = random.randrange(0, User.MAX_HEIGHT)
                y = random.randrange(0, User.MAX_WIDTH)
                z = random.randrange(0, User.MAX_LENGTH)

                if Room.checkOpacity(x, y, z) != True:
                    break

        builder = Builder()
        builder.setX(x)
        builder.setY(y)
        builder.setZ(z)

        room = builder.buildRoom()
        self.setRoom(room)

    def getRoom(self):
        return self.currRoom

    def getUser(self, username):
        db = Database.getInstance()
        sql = 'SELECT * FROM users WHERE username = \'' + username + '\''
        db.ExecQuery(sql)
        user = db.getAssoc()
        self.username = user[0]
        self.password = user[1]

        #TODO do the rest of the stuff

    def insertUser(self, username, password):
        db = Database.getInstance()
        sql = "INSERT INTO users (username, password, logged_in) VALUES ('" + username + "', '" + password + "', 1)"
        db.ExecQuery(sql)
        self.setUsername(username)


