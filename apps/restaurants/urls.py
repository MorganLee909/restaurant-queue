from django.conf.urls import url
from . import views

urlpatterns = [
    #Restaurants
    url(r'^$', views.loginPage),
    url(r'^login$', views.restaurantLogin),
    url(r'^new$', views.newRestaurant),
    url(r'^create$', views.createRestaurant),
    url(r'^(?P<restaurantId>\d+)$', views.showRestaurant),
    url(r'^(?P<restaurantId>\d+)/edit$', views.editRestaurant),
    url(r'^(?P<restaurantId>\d+)/update$', views.updateRestaurant),
    url(r'^(?P<restaurantId>\d+)/destroy$', views.destroyRestaurant),
    #Tables
    url(r'^tables/create$', views.createTables),
    url(r'^tables/(?P<tableId>\d+)/edit$', views.editTables),
    url(r'^tables/(?P<tableId>\d+)/update$', views.updateTables),
    url(r'^tables/(?P<tableId>\d+)/destroy$', views.deleteTable),
    #Dashboard
    url(r'^dashboard$', views.restaurantDashboard),
    url(r'^addParty$', views.addParty),
    url(r'^tables/(?P<tableId>\d+)/assign$', views.assignTable),
    url(r'^removeParty/(?P<partyId>\d+)$', views.removeParty),
    url(r'^checkoutParty/(?P<partyId>\d+)$', views.checkout),
    url(r'^createuser$', views.createTempUser)
]