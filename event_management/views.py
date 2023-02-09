from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .models import Customer, Contract, Event
# from .permissions import IsContract
from .serializers import CustomerSerializer, ContractSerializer, EventSerializer


class CustomerViewSet(ModelViewSet):
    serializer_class = CustomerSerializer
    permission_classes = [
        IsAuthenticated,
        # IsContract
    ]

    def get_queryset(self):
        return Customer.objects.all()
        # return Customer.objects.filter(event=self.kwargs['event_pk'])


class ContractViewSet(ModelViewSet):
    serializer_class = ContractSerializer
    permission_classes = [
        IsAuthenticated,
        # IsContract
    ]

    def get_queryset(self):
        return Contract.objects.all()
        # contract = Contract.objects.filter(
        #     event=self.kwargs['event_pk']
        # )
        # if self.kwargs.get('pk'):
        #     contract = contract.filter(
        #         user=self.kwargs['pk'],
        #     )
        # return contract

    # def get_object(self):
    #     queryset = self.filter_queryset(self.get_queryset())
    #     obj = get_object_or_404(queryset)
    #     return obj


class EventViewSet(ModelViewSet):
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # if self.request.user.is_superuser:
        #     return Event.objects.all()
        # return Event.objects.filter(contracts__user=self.request.user).distinct()
        return Event.objects.all()
