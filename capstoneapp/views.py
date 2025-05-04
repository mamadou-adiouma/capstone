from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.views import APIView

# from rest_framework import viewsets
from rest_framework.response import Response

from capstoneapp.models import Menu, Booking
from capstoneapp.serializers import menuSerializer, bookingSerializer


#  For authentification
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated


# from django.http import HttpResponse


# Create your views here.


# To acces this y'wd authenticated
@api_view()
@permission_classes([IsAuthenticated])
def msg(request):
    return Response({"message": "this view is protected"})


# def sayHello(request):
#     return HttpResponse("Hello, World ! response")


def index(request):
    return render(request, "index.html", {})


# class UserViewSet(viewsets.ViewSet):
#     def get_permissions(self):
#         permission_classes = []
#         if self.request.method != "GET":
#             permission_classes = [IsAuthenticated]
#             return [permission() for permission in permission_classes]


# class MenuView(APIView):
#     def get(self, request):
#         items = Menu.objects.all()
#         serializer = menuSerializer(items, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = menuSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"status": "success", "data": serializer.data})


#  VIA API
#  POST && GET
class MenuItemView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Menu.objects.all()
    serializer_class = menuSerializer


#  GET PUT && DELETE
class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = menuSerializer


# class BookingView(APIView):
#     def get(self, request):
#         items = Booking.objects.all()
#         serializer = bookingSerializer(items, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = bookingSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"status": "success", "data": serializer.data})


#  VIA API
#  POST && GET
# class BookingItemView(generics.ListCreateAPIView):
#     queryset = Booking.objects.all()
#     serializer_class = bookingSerializer


#  GET PUT && DELETE
# class SingleBookingItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
#     queryset = Booking.objects.all()
#     serializer_class = bookingSerializer


#  VIEWSET
class bookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = bookingSerializer


# View (auth - token)  (PUT, GET && POST)
class SingleMenuItemView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = menuSerializer
