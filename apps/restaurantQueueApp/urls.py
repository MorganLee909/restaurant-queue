from django.conf.urls import url
from . import views

'''
Basic outline for the routes (this is RESTful routing, mostly)
This can change as needed, such as if we need to combine some of the
    routes into a single one
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
    url(r'^user/logout$', views.logout)
    #Tables
    url(r'^tables$', views.displayTables),
    url(r'^tables/new$', views.newTable),
    url(r'^tables/create$', views.createTable),
    url(r'^tables/(?P<tableId>\d+)/edit$', views.editTable),
    url(r'^tables/(?P<tableId>\d+)/update$', views.updateUser),
    url(r'^tables/(?P<tableId>\d+)/destroy$', views.deleteTable),
    #Other routes
    url(r'^dashboard/user$', view.userDashboard),
    url(r'^dashboard/restaurant$', view.restaurantDashboard)
]