#
# Krunal Patel
# db model for storing messages
#

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, SmallInteger, Text, DateTime

engine = create_engine('mysql://root:root@localhost:3306/dungeon', echo=False)
Session = sessionmaker(bind=engine)
session = Session()

class Messages:
    message = None

    def getInstance(self):
        if Messages.message is None:
            Messages.message = Messages()

        return Messages.message


    def insertSayMessage(self, user_id, message_type, message, room_coord):
        new_record = messageTable(user_id, message_type, message, room_coord, None)
        session.add(new_record)
        session.commit

    def insertYellMessage(self, user_id, message_type, message):
        new_record = messageTable(user_id, message_type, message, None, None)
        session.add(new_record)
        session.commit

    def insertTellMessage(self, user_id, message_type, message, target_user_id):
        new_record = messageTable(user_id, message_type, message, None, target_user_id)
        session.add(new_record)
        session.commit




#
# Message SQL model
#

Base = declarative_base()

class messageTable(Base):
    __tablename__ = 'messages'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False)
    message_type = Column(SmallInteger, nullable=False)
    message = Column(Text, nullable=True)
    room_coord = Column(String(10), nullable=True)
    target_user_id = Column(Integer, nullable=True)
    time_added = Column(DateTime, nullable=False)

    def __init__(self, user_id, message_type, message, room_coord, target_user_id):
        self.user_id = user_id
        self.message_type = message_type
        self.message = message
        self.room_coord = room_coord
        self.target_user_id = target_user_id

    def __repr__(self):
        return "<MessageTable(%s, %s)>" % (self.user_id, self.message_type)