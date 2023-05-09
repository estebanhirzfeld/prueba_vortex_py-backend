from django.urls import path
from .views import UserCreateView, UserListView
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', csrf_exempt(UserCreateView.as_view()) ),
    path('list/', UserListView.as_view())
]