#
# Krunal Patel
# module to handle all the commands
#

from mud.room import Room
from mud.user import User
from mud.messages import Messages

class CommandHandler:
    TELL = 1
    SAY = 2
    YELL = 3

    def __init__(self):
        self.command_list = [
            'say',
            'yell',
            'tell',
            'north',
            'south',
            'east',
            'west',
            'up',
            'down'
        ]

    def handleCommand(self, request):
        arr = request.split(' ', 2)
        arr[0] = arr[0].lower()
        if arr[0] not in self.command_list:
            return False

        #TODO populate the dictionary with real methods
        return {
            'say': self.sayCommandHandler(request),
            'yell':self.yellCommandHandler(request),
            'tell':self.tellCommandHandler(request),
            'north':self.northCommandHandler(),
            'south':self.southCommandHandler(),
            'east':self.eastCommandHandler(),
            'west':self.westCommandHandler(),
            'up':self.upCommandHandler(),
            'down':self.downCommandHandler()
        }.get(request, False)

    # Handles SAY command which is used to broadcast in a room
    def sayCommandHandler(self, request):
        userClass = User.getInstance()
        user = userClass.getUser('foo') #TODO get username from session
        room = user.getRoom()
        message = Messages.getInstance()
        coord = room.getX() + room.getY() + room.getZ()
        message.insertSayMessage(user.id, CommandHandler.SAY, request, coord)
        return {
            'type':'message',
            'success': True
        }

    # Handles YELL command which is used to broadcast all over the world
    def yellCommandHandler(self, request):
        userClass = User.getInstance()
        user = userClass.getUser('foo')  # TODO get username from session
        message = Messages.getInstance()
        message.insertYellMessage (user.id, CommandHandler.YELL, request)
        return {
            'type': 'message',
            'success': True
        }

    # Handles TELL command which is used send a private chat to a user
    def tellCommandHandler(self, request):
        userClass = User.getInstance()
        user = userClass.getUser('foo')  # TODO get username from session
        message = Messages.getInstance()
        arr = request.split(' ', 2)
        other_user = user.getOtherUser(arr[0])
        if other_user is None:
            return {
                'type': 'message',
                'success': False
            }

        message.insertTellMessage (user.id, CommandHandler.TELL, request, other_user.id)
        return {
            'type': 'message',
            'success': True
        }

    # Handles NORTH command through which user traverse to the room north to the current room
    def northCommandHandler(self):
        response = {
            'type':'direction'
        }
        userClass = User.getInstance()
        user = userClass.getUser('foo')
        curr_room = user.getRoom()
        x = curr_room.getX()
        y = curr_room.getY()
        z = curr_room.getZ()
        y += 1
        if y >= User.MAX_WIDTH:
            response['success'] = False
            response['reason'] = 'out of bounds'
            return response

        if Room.checkOpacity(x, y, z) is False:
            response['success'] = False
            response['reason'] = 'opaque'
            return response

        user.createRoom(x, y, z)
        response['success'] = True
        response['room'] = {
            'name':user.getRoom().getName(),
            'description':user.getRoom().getDescription
        }
        response['users'] = user.getUsersRoom()

        return response

    # Handles SOUTH command through which user traverse to the room south to the current room
    def southCommandHandler(self):
        response = {
            'type': 'direction'
        }
        userClass = User.getInstance()
        user = userClass.getUser('foo')
        curr_room = user.getRoom()
        x = curr_room.getX()
        y = curr_room.getY()
        z = curr_room.getZ()
        y -= 1
        if y < 0:
            response['success'] = False
            response['reason'] = 'out of bounds'
            return response

        if Room.checkOpacity(x, y, z) is False:
            response['success'] = False
            response['reason'] = 'opaque'
            return response

        user.createRoom(x, y, z)
        response['success'] = True
        response['room'] = {
            'name': user.getRoom().getName(),
            'description': user.getRoom().getDescription
        }
        response['users'] = user.getUsersRoom()

        return response

    # Handles EAST command through which user traverse to the room east to the current room
    def eastCommandHandler(self):
        response = {
            'type': 'direction'
        }
        userClass = User.getInstance()
        user = userClass.getUser('foo')
        curr_room = user.getRoom()
        x = curr_room.getX()
        y = curr_room.getY()
        z = curr_room.getZ()
        x += 1
        if x >= User.MAX_LENGTH:
            response['success'] = False
            response['reason'] = 'out of bounds'
            return response

        if Room.checkOpacity(x, y, z) is False:
            response['success'] = False
            response['reason'] = 'opaque'
            return response

        user.createRoom(x, y, z)
        response['success'] = True
        response['room'] = {
            'name': user.getRoom().getName(),
            'description': user.getRoom().getDescription
        }
        response['users'] = user.getUsersRoom()

        return response

    # Handles WEST command through which user traverse to the room west to the current room
    def westCommandHandler(self):
        response = {
            'type': 'direction'
        }
        userClass = User.getInstance()
        user = userClass.getUser('foo')
        curr_room = user.getRoom()
        x = curr_room.getX()
        y = curr_room.getY()
        z = curr_room.getZ()
        x -= 1
        if x < 0:
            response['success'] = False
            response['reason'] = 'out of bounds'
            return response

        if Room.checkOpacity(x, y, z) is False:
            response['success'] = False
            response['reason'] = 'opaque'
            return response

        user.createRoom(x, y, z)
        response['success'] = True
        response['room'] = {
            'name': user.getRoom().getName(),
            'description': user.getRoom().getDescription
        }
        response['users'] = user.getUsersRoom()

        return response

    # Handles UP command through which user traverse to the room UP to the current room
    def upCommandHandler(self):
        response = {
            'type': 'direction'
        }
        userClass = User.getInstance()
        user = userClass.getUser('foo')
        curr_room = user.getRoom()
        x = curr_room.getX()
        y = curr_room.getY()
        z = curr_room.getZ()
        z += 1
        if z >= User.MAX_HEIGHT:
            response['success'] = False
            response['reason'] = 'out of bounds'
            return response

        if Room.checkOpacity(x, y, z) is False:
            response['success'] = False
            response['reason'] = 'opaque'
            return response

        user.createRoom(x, y, z)
        response['success'] = True
        response['room'] = {
            'name': user.getRoom().getName(),
            'description': user.getRoom().getDescription
        }
        response['users'] = user.getUsersRoom()

        return response

    # Handles DOWN command through which user traverse to the room down to the current room
    def downCommandHandler(self):
        response = {
            'type': 'direction'
        }
        userClass = User.getInstance()
        user = userClass.getUser('foo')
        curr_room = user.getRoom()
        x = curr_room.getX()
        y = curr_room.getY()
        z = curr_room.getZ()
        z -= 1
        if z < 0:
            response['success'] = False
            response['reason'] = 'out of bounds'
            return response

        if Room.checkOpacity(x, y, z) is False:
            response['success'] = False
            response['reason'] = 'opaque'
            return response

        user.createRoom(x, y, z)
        response['success'] = True
        response['room'] = {
            'name': user.getRoom().getName(),
            'description': user.getRoom().getDescription
        }
        response['users'] = user.getUsersRoom()

        return response