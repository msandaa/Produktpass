
from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.produktpass_search ,name='produktpass_search'),
    path('produktpass/<str:id>',views.produktpass_show ,name='produktpass_show'),
    path('produktpass/<str:id>/massnahmen',views.massnahmen_show ,name='massnahmen_show'),

]
