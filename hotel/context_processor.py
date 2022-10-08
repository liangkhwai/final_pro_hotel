from hotel.views import booking
from .models import *


def extras(req):
    rooms = RoomType.objects.all()

    if req.user.is_authenticated:
        search_cust = Customer.objects.get(account_id = req.session['user'])
        booking_user  = Booking.objects.all().filter(cust = search_cust)   
    else:
        booking_user = ""
    context = {
        'roomname':rooms,
        'booking_user':booking_user
    }
    
    return context






