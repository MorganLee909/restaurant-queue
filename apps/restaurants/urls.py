from django.conf.urls import url
from . import views

urlpatterns = [
    #Restaurants
    url(r'^$', views.loginPage),
    url(r'^login$', views.restaurantLogin),
    url(r'^new$', views.newRestaurant),
    url(r'^create$', views.createRestaurant),
    url(r'^(?P<restuarantId>\d+)$', views.showRestaurant),
    url(r'^(?P<restuarantId>\d+)/edit$', views.editRestaurant),
    url(r'^(?P<restuarantId>\d+)/update$', views.updateRestaurant),
    url(r'^(?P<restuarantId>\d+)/destroy$', views.destroyRestaurant),
    #Tables
    url(r'^tables$', views.displayTables),
    url(r'^tables/new$', views.newTable),
    url(r'^tables/create$', views.createTables),
    url(r'^tables/(?P<tableId>\d+)/edit$', views.editTables),
    url(r'^tables/(?P<tableId>\d+)/update$', views.updateTables),
    url(r'^tables/(?P<tableId>\d+)/destroy$', views.deleteTable),
    #Dashboard
    url(r'^dashboard$', views.restaurantDashboard)
]