from datetime import timezone

from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator


class Customer(models.Model):
    name = models.CharField(
        _('Last Name'),
        max_length=555
    )

    first_name = models.CharField(
        _('First Name'),
        max_length=555
    )

    company = models.CharField(
        _('Company Name'),
        max_length=555
    )

    email = models.EmailField(_('Email address'), unique=True)

    address = models.TextField(
        _('Address'),
        max_length=1080,
        blank=True
    )

    prospect = models.BooleanField(
        _('Prospect'),
    )

    phone_number = models.CharField(
        _('Phone'),
        max_length=17,
        blank=True
    )
    mobile_phone_number = models.CharField(
        _('Mobile Phone'),
        max_length=17,
        blank=True
    )

    sale_employee = models.ForeignKey(
        verbose_name=_('Sales Contact'),
        to=get_user_model(),
        on_delete=models.CASCADE,
        related_name='customer_managed',
        blank=False,
    )

    time_created = models.DateTimeField(
        _('Created time'),
        auto_now_add=True
    )
    time_updated = models.DateTimeField(
        _('Updated time'),
        auto_now=True
    )

    def __str__(self):
        return self.name


class Contract(models.Model):
    name = models.CharField(
        _('Name'),
        max_length=255
    )

    state = models.CharField(
        verbose_name=_('State'),
        choices=[
            ('proposal', _('Proposal')),
            ('signed', _('Signed')),
            ('canceled', _('Canceled')),
        ],
        max_length=255,
        default='proposal',
    )

    customer = models.ForeignKey(
        verbose_name=_('Customer'),
        to=Customer,
        on_delete=models.CASCADE,
        related_name='contracts',
        blank=False,
    )

    sale_employee = models.ForeignKey(
        verbose_name=_('Sales Contact'),
        to=get_user_model(),
        on_delete=models.CASCADE,
        related_name='contract_managed',
        blank=False,
    )

    signature_date = models.DateTimeField(
        _('Signature Date'),
        null=True,
        blank=True
    )

    amount = models.FloatField(
        _('Amount'),
        null=True,
        blank=True
    )

    payment_due = models.DateTimeField(
        _('Payment Due'),
        null=True,
        blank=True
    )

    time_created = models.DateTimeField(
        _('Created time'),
        auto_now_add=True
    )
    time_updated = models.DateTimeField(
        _('Updated time'),
        auto_now=True
    )

    def __str__(self):
        return f"{self.name} - {self.customer}"


class Event(models.Model):
    name = models.CharField(
        _('Name'),
        max_length=255
    )

    event_date = models.DateTimeField(
        _('Event Date'),
        null=True,
        blank=True
    )

    address = models.TextField(
        _('Address'),
        max_length=1080,
        blank=True
    )

    state = models.CharField(
        verbose_name=_('State'),
        choices=[
            ('to_plan', _('To Plan')),
            ('planned', _('Planned')),
            ('done', _('Done')),
            ('canceled', _('Canceled')),
        ],
        max_length=255,
        default='proposal',
    )

    support_employee = models.ForeignKey(
        verbose_name=_('Support Employee'),
        to=get_user_model(),
        on_delete=models.CASCADE,
        related_name='events_to_support',
        blank=False,
    )

    attendees = models.IntegerField(
        _('Attendees'),
        null=True,
        blank=True
    )

    customer = models.ForeignKey(
        verbose_name=_('Customer'),
        to=Customer,
        on_delete=models.CASCADE,
        related_name='events',
        blank=False,
    )

    notes = models.TextField(
        _('Notes'),
        null=True,
        blank=True
    )

    contract = models.ForeignKey(
        verbose_name=_('Contract'),
        to=Contract,
        on_delete=models.CASCADE,
        related_name='events',
        blank=False,
    )

    def __str__(self):
        return f"{self.name} - {self.contract}"
