from django.contrib import admin

from .models import Customer, Contract, Event


@admin.register(Customer)
class CustomerAdminConfig(admin.ModelAdmin):
    model = Customer
    search_fields = ('name', 'email', 'prospect')
    # list_filter = ('user',)
    ordering = ('-time_created',)
    list_display = ('id', 'name', 'email', 'phone_number', 'prospect')


@admin.register(Contract)
class ContractAdminConfig(admin.ModelAdmin):
    model = Contract
    search_fields = ('name', 'customer', 'state')
    list_filter = ('customer',)
    ordering = ('-time_created', 'state',)
    list_display = ('name', 'customer', 'state', 'signature_date',)


@admin.register(Event)
class EventAdminConfig(admin.ModelAdmin):
    model = Event
    search_fields = ('name', 'event_date', 'state',)
    list_filter = ('state', )
    ordering = ('-event_date',)
    list_display = ('name', 'event_date', 'state', 'support_employee',
                    'event_employee',)

