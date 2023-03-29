from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .models import Customer, Contract, Event
from .permissions import HasGroupPermission
from .serializers import CustomerSerializer, ContractSerializer, EventSerializer


class CustomerViewSet(ModelViewSet):
    serializer_class = CustomerSerializer
    permission_classes = [
        IsAuthenticated,
        HasGroupPermission
    ]
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    filterset_fields = '__all__'
    search_fields = ['name', 'first_name', 'company', 'email']
    def get_queryset(self):
        return Customer.objects.all()


class ContractViewSet(ModelViewSet):
    serializer_class = ContractSerializer
    permission_classes = [
        IsAuthenticated,
        HasGroupPermission
    ]
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    filterset_fields = '__all__'
    search_fields = ['customer__name', 'signature_date', 'amount', 'customer__email']

    def get_queryset(self):
        return Contract.objects.all()



class EventViewSet(ModelViewSet):
    serializer_class = EventSerializer
    permission_classes = [
        IsAuthenticated,
        HasGroupPermission
    ]
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    filterset_fields = '__all__'
    search_fields = ['customer__name', 'event_date', 'customer__email']

    def get_queryset(self):
        return Event.objects.all()
