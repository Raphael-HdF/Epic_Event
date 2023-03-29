from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from event_management.models import Customer, Contract, Event
from django.contrib.auth import get_user_model


class Command(BaseCommand):
    help = 'Create groups with all permissions on Customer, Contract and Event models'

    def handle(self, *args, **options):
        User = get_user_model()

        user_ct = ContentType.objects.get_for_model(User)
        customer_ct = ContentType.objects.get_for_model(Customer)
        contract_ct = ContentType.objects.get_for_model(Contract)
        event_ct = ContentType.objects.get_for_model(Event)

        user_perms = Permission.objects.filter(content_type=user_ct)
        customer_perms = Permission.objects.filter(content_type=customer_ct)
        contract_perms = Permission.objects.filter(content_type=contract_ct)
        event_perms = Permission.objects.filter(content_type=event_ct)
        management_perms = user_perms | customer_perms | contract_perms | event_perms
        view_perms = management_perms.filter(codename__startswith='view')

        gestion_perms = Permission.objects.all()
        support_perms = event_perms | view_perms
        vente_perms = customer_perms | contract_perms | view_perms | \
                      event_perms.filter(codename__startswith='add')

        gestion_group, _ = Group.objects.get_or_create(name='Gestion')
        support_group, _ = Group.objects.get_or_create(name='Support')
        vente_group, _ = Group.objects.get_or_create(name='Vente')

        for perm in gestion_perms:
            gestion_group.permissions.add(perm)

        for perm in support_perms:
            support_group.permissions.add(perm)

        for perm in vente_perms:
            vente_group.permissions.add(perm)

        self.stdout.write(self.style.SUCCESS('Successfully created groups with all permissions'))
