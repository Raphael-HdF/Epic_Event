from django.contrib import admin
from django import forms

from .models import Customer, Contract, Event
from .permissions import DjangoAdminPermission


class ContractForm(forms.ModelForm):
    contracts = forms.ModelChoiceField(queryset=Contract.objects.all())  # your filter

    class Meta:
        model = Contract
        fields = ('name',)


class ContractInline(admin.TabularInline):
    model = Contract
    form = ContractForm


@admin.register(Customer)
class CustomerAdminConfig(DjangoAdminPermission):
    model = Customer
    search_fields = ('name', 'email', 'prospect')
    list_filter = ('sale_employee',)
    ordering = ('-time_created',)
    list_display = ('name', 'email', 'phone_number', 'prospect', 'sale_employee', 'id', )
    inlines = (ContractInline,)
    fieldsets = (
        ('Informations', {'fields': (
            'prospect',
            'name',
            'first_name',
            'company',
            'phone_number',
            'mobile_phone_number',
            'email',
            'address',
            'sale_employee',
        )}),
        # ('Contracts', {'fields': ('contracts',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'prospect',
                'name',
                'phone_number',
                'email',
                'address',
            )
        }
         ),
    )


@admin.register(Contract)
class ContractAdminConfig(DjangoAdminPermission):
    model = Contract
    search_fields = ('name', 'customer', 'state')
    list_filter = ('state', 'customer', 'sale_employee',)
    ordering = ('-time_created', 'state',)
    list_display = ('name', 'customer', 'state', 'signature_date', 'sale_employee',)


@admin.register(Event)
class EventAdminConfig(DjangoAdminPermission):
    model = Event
    search_fields = ('name', 'event_date', 'state',)
    list_filter = ('state', 'customer', 'support_employee',)
    ordering = ('-event_date',)
    list_display = ('name', 'customer', 'event_date', 'state', 'support_employee',)
