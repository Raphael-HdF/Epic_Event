import itertools
from datetime import datetime, timedelta
from random import choice, randint

from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.utils import timezone
from faker import Faker

from event_management.models import Customer, Contract, Event


class Command(BaseCommand):
    help = 'Generate demo data using Faker'

    def add_arguments(self, parser):
        parser.add_argument('users', type=int, help='Number of users to create')
        parser.add_argument('customers', type=int, help='Number of customers to create')
        parser.add_argument('contracts', type=int,
                            help='Number of contracts to create per customer')
        parser.add_argument('events', type=int,
                            help='Number of events to create per contract')

    def handle(self, *args, **options):
        fake = Faker()
        users_count = options.get('users', 0)
        customers_count = options.get('customers', 10)
        contracts_count = options.get('contracts', 2)
        events_count = options.get('events', 1)

        User = get_user_model()

        # create users
        for _ in range(users_count):
            username = fake.user_name()
            email = fake.email()

            user = User.objects.create_user(
                username=username,
                email=email,
                password="password",
                is_staff=True,
            )
            if groups := Group.objects.all():
                user.groups.add(choice(groups))

        users = User.objects.all()
        support_users = users.filter(groups__name="Support")
        vente_users = users.filter(groups__name="Vente")

        # create customers
        customers = []
        for _ in range(customers_count):
            vals = dict(
                name=fake.last_name(),
                first_name=fake.first_name(),
                company=fake.company(),
                email=fake.email(),
                address=fake.address(),
                prospect=choice([True, False]),
                phone_number=f'0{fake.msisdn()}'[:17],
                mobile_phone_number=f'0{fake.msisdn()}'[:17],
                sale_employee=choice(vente_users),
            )
            customer = Customer.objects.create(
                **vals
            )
            customers.append(customer)

        # create contracts
        contracts = []
        for customer, _ in itertools.product(customers, range(contracts_count)):
            chosen_state = choice(['proposal', 'signed', 'canceled'])
            signature_date =fake.date_time_between(
                    start_date='-1y',
                    end_date='now',
                    tzinfo=timezone.utc
                ) if chosen_state else None

            contract = Contract.objects.create(
                name=fake.sentence(nb_words=3),
                state=chosen_state,
                customer=customer,
                amount=randint(0, 5000),
                sale_employee=choice(vente_users),
                signature_date=signature_date,
                payment_due=signature_date + timedelta(days=30)
                 if signature_date else None,
            )
            contracts.append(contract)

        # create events
        for contract, _ in itertools.product(contracts, range(events_count)):
            chosen_state = choice(['to_plan', 'planned', 'done', 'canceled'])

            vals = dict(
                name=fake.sentence(nb_words=3),
                event_date=fake.date_time_between(start_date=contract.signature_date,
                                                  end_date='+1y', tzinfo=timezone.utc)
                if contract.signature_date and chosen_state != 'to_plan' else None,
                address=fake.address(),
                notes=fake.paragraph(nb_sentences=5),
                state=chosen_state,
                attendees=randint(0, 300),
                customer=contract.customer,
                support_employee=choice(support_users),
                contract=contract,
            )
            event = Event.objects.create(
                **vals
            )

        self.stdout.write(self.style.SUCCESS(
            f'Successfully generated {users_count} users, {customers_count} customers,'
            f' {contracts_count} contracts per customer, and {events_count} events per contract.'))
