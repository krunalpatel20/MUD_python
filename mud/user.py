#
# Krunal Patel
# User container class
#

import random
from mud.builder import Builder
from mud.room import Room
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Boolean

from mud.user import UserTable


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
        if User.user is None:
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
        record = session.query(UserTable).filter_by(username=username).first()
        self.username = record.username
        self.password = record.password
        room_coord = record.room_coord
        if(len(room_coord) < 3):
            x = 0
            y = room_coord[0]
            z = room_coord[1]
        else:
            x = room_coord[0]
            y = room_coord[1]
            z = room_coord[2]

        builder = Builder()
        builder.setX(x)
        builder.setY(y)
        builder.setZ(z)
        self.currRoom = builder.buildRoom()
        return record

    def getOtherUser(self, username):
        record = session.query(UserTable).filter_by(username=username).first()
        return record


    def insertUser(self, username, password):
        new_record = UserTable(username, password, True, '')
        session.add(new_record)
        session.commit()

    def updateLogin(self, login):
        record = User.session.query(UserTable).filter_by(username=self.username).first()
        record.logged_in = login
        session.add(record)
        session.commit()

    def reset(self):
        self.username = None
        self.password = None

    def checkPassword(self,password):
        return self.password == password

    def getUsersRoom(self):
        x = self.currRoom.getX()
        y = self.currRoom.getY()
        z = self.currRoom.getZ()
        coord = x + "" + y + "" + z

        records = session.query(UserTable).filter_by(room_coord=coord)
        users = []
        for record in records:
            users.append(record.username)

        return users

    def updateRoom(self):
        if self.username == None or self.username == '':
            return False
        x = self.currRoom.getX()
        y = self.currRoom.getY()
        z = self.currRoom.getZ()
        coord = x + "" + y + "" + z
        record = session.query(UserTable).filter_by(username=self.username).first()
        record.room_coord = coord
        session.add(record)
        session.commit()

#
# The User SQL Model
#
engine = create_engine('mysql://root:root@localhost:3306/dungeon', echo=False)
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class UserTable(Base):
    __tablename__ = 'user'

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
        return "<UserTable(%s, %s)>" % (self.username, self.room_coord)


