from django.urls import path
from . import views


urlpatterns = [
    path('dashboard/', views.DashboardView.as_view(), name="home_view"),
    path('create/product/', views.ProductFormsView.as_view(), name="create_product"),
    path('create/shipment/', views.ShipmentFormsView.as_view(), name="create_shipment"),
    path('create/orders/', views.OrdersFormsView.as_view(), name="create_orders"),
    path('create/manif/', views.ManifactureFormsView.as_view(), name="create_manif"),
]
