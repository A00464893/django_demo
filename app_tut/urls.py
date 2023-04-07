from django.urls import path
from .views import home, hotel_list,HolelList

urlpatterns = [
    path('home', home),
    path('hotel_list', hotel_list),
    path('class_hotel',HolelList.as_view())
]
