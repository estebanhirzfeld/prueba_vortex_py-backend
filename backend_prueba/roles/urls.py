from django.urls import path
from .views import UserCreateView
from django.views.decorators.csrf import csrf_exempt
urlpatterns = [
    path('', csrf_exempt(UserCreateView.as_view()) ),

]