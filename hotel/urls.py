from urllib.parse import urlparse
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


handler404 = 'hotel.views.notFound'

urlpatterns = [
    path('',views.home,name='home'),
    path('register',views.register,name='register'),
    path('addrooms',views.addrooms,name='addrooms'),
    path('addtype',views.addtype,name='addtype'),
    path('editcustomer/<int:pk>',views.editcustomer,name='editcustomer'),
    path('editpassword/<int:pk>',views.editpassword,name='editpassword'),
    path('room/<int:pk>',views.editrooms,name='editrooms'),
    path('room/<int:pk>/<int:fk>',views.editroom,name='editroom'),
    path('edittype/<int:pk>',views.edittype,name='edittype'),
    path('rooms',views.fetchrooms,name='fetchrooms'),
    path('roomdetail/<int:pk>',views.roomdetail,name='roomdetail'),
    path('login',views.login_user,name='login'),
    path('logout',views.logout_user,name='logout'),
    path('room/delete/<int:pk>/<int:fk>',views.deleteroom,name='deleteroom'),
    path('deletetype/<int:pk>',views.deletetype,name='deletetype'),
    path('booking/<int:pk>',views.booking,name='booking'),
    path('payment',views.payment,name='payment'),
    path('bookdetail/<int:pk>',views.bookdetail,name='bookingdetail'),
    path('delimg/<int:id>/<int:type>',views.delMultiImg,name='delimg'),
    path('addanotherimg',views.addanotherimg,name='addanotherimg'),
    path('alltype',views.alltype,name='alltype'),
    path('contact',views.contact,name='contact'),
    path('transection',views.transection,name='transecton'),
    path('cancle/<int:pk>',views.cancle,name='cancle'),
    path('about',views.about,name='about'),
    path('objective',views.objective,name='objective'),
    path('source',views.source,name='source'),
    path('editmember',views.editmember,name='editmember'),
    path('editmember_admin/<int:pk>',views.editmember_admin,name='editmember_admin'),
    path('delmember_admin/<int:pk>',views.delmember_admin,name='delmember_admin'),
    

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)