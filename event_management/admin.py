from django.contrib import admin
from django import forms

from .models import Customer, Contract, Event


class ContractForm(forms.ModelForm):
    contracts = forms.ModelChoiceField(queryset=Contract.objects.all())  # your filter
    class Meta:
        model = Contract

        fields = ('name', )

class ContractInline(admin.TabularInline):
    model = Contract
    form = ContractForm
@admin.register(Customer)
class CustomerAdminConfig(admin.ModelAdmin):
    model = Customer
    search_fields = ('name', 'email', 'prospect')
    # list_filter = ('user',)
    ordering = ('-time_created',)
    list_display = ('id', 'name', 'email', 'phone_number', 'prospect')
    inlines = (ContractInline,)
    fieldsets = (
        ('Informations', {'fields': (
            'prospect',
            'name',
            'phone_number',
            'email',
            'address',
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
    # filter_horizontal = (
    #     "contracts",
    # )

@admin.register(Contract)
class ContractAdminConfig(admin.ModelAdmin):
    model = Contract
    search_fields = ('name', 'customer', 'state')
    list_filter = ('state', 'customer', 'sale_employee',)
    ordering = ('-time_created', 'state',)
    list_display = ('name', 'customer', 'state', 'signature_date', 'sale_employee',)


@admin.register(Event)
class EventAdminConfig(admin.ModelAdmin):
    model = Event
    search_fields = ('name', 'event_date', 'state',)
    list_filter = ('state', 'customer', 'support_employee',)
    ordering = ('-event_date',)
    list_display = ('name', 'customer', 'event_date', 'state', 'support_employee',)
