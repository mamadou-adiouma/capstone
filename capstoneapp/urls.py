from .views import sayHello
from django.urls import path

urlpatterns = [path("", sayHello, name="sayhello")]
