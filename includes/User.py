#
# Krunal Patel
# User container class
#

import random
from includes.Builder import Builder
from includes.Room import Room
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Boolean

class User:
    user = None
    MAX_WIDTH = 3
    MAX_LENGTH = 3
    MAX_HEIGHT = 3

    engine = create_engine('mysql://root:root@localhost:3306/dungeon', echo=False)
    Session = sessionmaker(bind=engine)
    session = Session()


    Base = declarative_base()
    class UserTable(Base):
        __tablename__='user'

        id = Column(Integer, primary_key=True)
        username = Column(String(45), nullable=False)
        password = Column(String(45), nullable=True)
        logged_in = Column(Boolean, nullable=False)
        room_coord = Column(String(10), nullable=False)

        def __init__(self, username, password, logged_in, room_coord):
            self.username = username
            self.password = password
            self.logged_in = logged_in
            self.room_coord = room_coord

        def __repr__(self):
            return "<UserTable(%s, %s)>" %(self.username, self.room_coord)


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


