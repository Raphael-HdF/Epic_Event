from rest_framework.routers import DefaultRouter
from rest_framework_nested.routers import NestedSimpleRouter
from .views import CustomerViewSet, ContractViewSet, EventViewSet

base_router = DefaultRouter()
base_router.register(r'customers', CustomerViewSet, basename='customer')

customers_router = NestedSimpleRouter(base_router, r'customers', lookup='customer')
customers_router.register(
    r'contracts', ContractViewSet, basename='contract'
)

contracts_router = NestedSimpleRouter(customers_router, r'contracts', lookup='contract')
contracts_router.register(
    r'events', EventViewSet, basename='event'
)
