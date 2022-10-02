from .models import *


def extras(req):
    rooms = RoomType.objects.all()
    return {'roomname':rooms}

