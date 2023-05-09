from django.urls import path
from pedidosApp.api.api import pedido_api_view, pedido_detail_view

urlpatterns = [
    path('pedido/', pedido_api_view, name='pedido_api'),
    path("pedido/<int:pk>/", pedido_detail_view, name="pedido_detail_view")
]