from hotel.views import booking
from .models import *


def extras(req):
    rooms = RoomType.objects.all()

    if req.user.is_authenticated:
        search_cust = Customer.objects.get(account_id = req.session['user'])
        booking_user  = Booking.objects.all().filter(cust = search_cust)   
        booking_count = Booking.objects.all().filter(cust = search_cust).count()
    else:
        booking_user = ""
        booking_count = 0
    context = {
        'roomname':rooms,
        'booking_user':booking_user,
        'booking_count':booking_count
    }
    
    return context






