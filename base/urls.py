from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^room/', views.room, name="room"),
    url('', views.home, name="home"),
]
