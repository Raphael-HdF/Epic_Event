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
            # customer = Customer(**{
            #     "event": event,
            #     "user": self.context['request'].user,
            #     "permission": "editor",
            #     "role": "Author",
            # })
            # customer.save()
        except Exception as e:
            raise ValidationError(e)
        return event


class ContractSerializer(ModelSerializer):
    class Meta:
        model = Contract
        fields = "__all__"
        # read_only_fields = ['employee', 'author_user']

    def create(self, validated_data):
        try:
            contract = Contract(**validated_data)
            # contract.employee_id = self.context["view"].kwargs.get('employee_pk')
            # contract.author_user = self.context['request'].user
            contract.save()
        except Exception as e:
            raise ValidationError(e)
        return contract


class CustomerSerializer(ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"
        # read_only_fields = ['event']

    def create(self, validated_data):
        try:
            customer = Customer(**validated_data)
            # customer.event_id = self.context["view"].kwargs.get('event_pk')
            customer.save()
        except Exception as e:
            raise ValidationError(e)
        return customer
