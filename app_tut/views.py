from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import Hotel
from .serializer import Hotel_Serializer
from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework.response import Response


# Create your views here.

def home(request):
    return HttpResponse('<h1>Hi Dummy</h1>')

@api_view(['GET'])
def hotel_list(request):
    data = Hotel_Serializer(Hotel.objects.all(), many=True).data
    return Response(data)
    # return JsonResponse({
    #     hotel_list : list(Hotel.objects.all())
    # })
@api_view(['POST'])
def add_list(request):
    data = Hotel_Serializer(data = request.data)
    if data.is_valid():
        data.save()
        return Response(Hotel_Serializer(Hotel.objects.all(), many=True).data)
    else:
        return Response({'Error':"Invalid Parameters"})

class HolelList(generics.ListCreateAPIView):
    queryset = Hotel.objects.all()
    serializer_class = Hotel_Serializer

