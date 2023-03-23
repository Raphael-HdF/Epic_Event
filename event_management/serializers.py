from rest_framework.serializers import ModelSerializer, ValidationError
from .models import Customer, Contract, Event


class EventSerializer(ModelSerializer):
    class Meta:
        model = Event
        fields = "__all__"

    def create(self, validated_data):
        try:
            event = Event(**validated_data)
            event.save()
        except Exception as e:
            raise ValidationError(e)
        return event


class ContractSerializer(ModelSerializer):
    class Meta:
        model = Contract
        fields = "__all__"

    def create(self, validated_data):
        try:
            contract = Contract(**validated_data)
            contract.save()
        except Exception as e:
            raise ValidationError(e)
        return contract


class CustomerSerializer(ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"

    def create(self, validated_data):
        try:
            customer = Customer(**validated_data)
            customer.save()
        except Exception as e:
            raise ValidationError(e)
        return customer
