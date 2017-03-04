from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^travels$', views.index, name = 'travelPlanPage'),
    url(r'^travels/add$', views.addTravelPlan, name = 'addTravel'),
    url(r'^newPlan$', views.newPlan, name = 'addPlan'),
    url(r'^travels/destination/(?P<id>\d+)$', views.show, name="show"),
    url(r'^add/(?P<id>\d+)$', views.add, name= 'add'),
]
