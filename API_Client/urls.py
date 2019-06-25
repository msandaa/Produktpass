
from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.produktpass_search ,name='produktpass_search'),
    path('produktpass/<str:agProID>/',views.produktpass_show ,name='produktpass_show'),
    path('produktpass/<str:agProID>/nutzflaechenmassnahmen',views.nutzflaechenmassnahmen_show ,name='nutzflaechenmassnahmen_show'),

]
