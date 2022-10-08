from hotel.views import booking
from .models import *


def extras(req):
    rooms = RoomType.objects.all()

    if req.session['user']:
        search_cust = Customer.objects.get(account_id = req.session['user'])
        booking_user  = Booking.objects.all().filter(cust = search_cust)   
        print(booking_user)
    
    context = {
        'roomname':rooms,
        'booking_user':booking_user
    }
    
    return context






