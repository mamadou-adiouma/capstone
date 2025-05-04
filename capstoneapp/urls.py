from django.urls import path

# from .views import sayHello
from capstoneapp import views

# Obtain the token
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    # path("", sayHello, name="sayhello"),
    path("", views.index, name="index"),
    # path("menu/", views.MenuView.as_view(), name="menu"),
    # path("booking/", views.BookingView.as_view(), name="booking"),
    # API
    path("menu-items/", views.MenuItemView.as_view()),
    # path("menu/<int:pk>", views.SingleMenuItemView.as_view()),
    # path("booking/", views.BookingItemView.as_view()),
    # path("booking/<int:pk>", views.SingleBookingItemView.as_view()),
    # auth token
    # path('menu-items/', views.MenuItemsView.as_view()),
    path("menu-items/<int:pk>", views.SingleMenuItemView.as_view()),
    # Only acces to authenticated users
    path("message/", views.msg),
    path("api-tocken-auth/", obtain_auth_token),
]
