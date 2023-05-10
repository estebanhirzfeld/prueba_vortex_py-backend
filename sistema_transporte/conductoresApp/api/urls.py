from django.urls import path
from conductoresApp.api.views import conductor_api_view, conductor_detail_view

urlpatterns = [
    path('', conductor_api_view, name='conductores_api'),
    path("<int:pk>/", conductor_detail_view, name="Conductor_detail_view"),
]
