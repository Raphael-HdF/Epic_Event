from rest_framework.routers import DefaultRouter
from rest_framework_nested.routers import NestedSimpleRouter
from .views import CustomerViewSet, ContractViewSet, EventViewSet

base_router = DefaultRouter()
base_router.register(r'customers', CustomerViewSet, basename='customer')
base_router.register(r'contracts', ContractViewSet, basename='contract')
base_router.register(r'events', EventViewSet, basename='event')
