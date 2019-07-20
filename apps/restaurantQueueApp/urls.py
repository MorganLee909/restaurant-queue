from django.conf.urls import url
from . import views

'''
Basic outline for the routes (this is RESTful routing, mostly)
This can change as needed, such as if we need to combine some of the
    routes into a single one

Added restaurants so that we can control them as users and have many
    of them right from the start.  It occured to me that this might
    be the best way to handle this.  We can talk about it.
'''

urlpatterns = [
    url(r'^$', views.index),
    #Users
    url(r'^users$', views.registerAndLogin),
    url(r'^users/create$', views.createUser),
    url(r'^users/(?P<userId>\d+)$', views.viewUser),
    url(r'^users/(?P<userId>\d+)/edit$', views.editUser),
    url(r'^users/(?P<userId>\d+)/update$', views.updateUser),
    url(r'^users/(?P<userId>\d+)/destroy$', views.deleteUser),
    url(r'^users/login$', views.login),
    url(r'^user/logout$', views.logout),
    #Restaurants
    url(r'^restaurants/new$', views.newRestaurant),
    url(r'^restaurants/create$', views.createRestaurant),
    url(r'^restaurants/(?P<restuarantId>\d+)$', views.showRestaurant),
    url(r'^restaurants/(?P<restuarantId>\d+)/edit$', views.editRestaurant),
    url(r'^restaurants/(?P<restuarantId>\d+)/update$', views.updateRestaurant),
    url(r'^restaurants/(?P<restuarantId>\d+)/destroy$', views.destroyRestaurant),
    #Tables
    url(r'^tables$', views.displayTables),
    url(r'^tables/new$', views.newTable),
    url(r'^tables/create$', views.createTable),
    url(r'^tables/(?P<tableId>\d+)/edit$', views.editTable),
    url(r'^tables/(?P<tableId>\d+)/update$', views.updateTable),
    url(r'^tables/(?P<tableId>\d+)/destroy$', views.deleteTable),
    #Other routes
    url(r'^dashboard/user$', views.userDashboard),
    url(r'^dashboard/restaurant$', views.restaurantDashboard)
]