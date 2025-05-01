from django.urls import path

# from .views import sayHello
from . import views

urlpatterns = [
    #     path("", sayHello, name="sayhello"),
    path("", views.index, name="index"),
]
