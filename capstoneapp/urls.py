from django.urls import path

# from .views import sayHello
from capstoneapp import views

urlpatterns = [
    # path("", sayHello, name="sayhello"),
    path("", views.index, name="index"),
    # path("menu/", views.MenuView.as_view(), name="menu"),
    # path("booking/", views.BookingView.as_view(), name="booking"),
    # API
    path("menu/", views.MenuItemView.as_view()),
    # path("menu/<int:pk>", views.SingleMenuItemView.as_view()),
    # path("booking/", views.BookingItemView.as_view()),
    # path("booking/<int:pk>", views.SingleBookingItemView.as_view()),
]
