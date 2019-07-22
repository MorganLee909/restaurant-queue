from django.conf.urls import url
from . import views

urlpatterns = [
    #Users
    url(r'^$', views.registerAndLogin),
    url(r'^create$', views.createUser),
    url(r'^new$', views.newUser),
    url(r'^(?P<userId>\d+)$', views.viewUser),
    url(r'^(?P<userId>\d+)/edit$', views.editUser),
    url(r'^(?P<userId>\d+)/update$', views.updateUser),
    url(r'^(?P<userId>\d+)/destroy$', views.deleteUser),
    url(r'^login$', views.login),
    url(r'^logout$', views.logout),
    #Dashboard
    url(r'^dashboard/user$', views.userDashboard)
]