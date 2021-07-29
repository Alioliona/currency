from django.core.management.base import BaseCommand
from currency.models import Rate, ContactUs
from faker import Faker

import random


class Command(BaseCommand):
    helpme = 'Generating random data'

    def handle(self, *args, **options):
        fake = Faker()

        for index in range(10):
            Rate.objects.create(
                currency_type=random.choice(('usd', 'eur')),
                sale=random.uniform(20.00, 29.99),
                buy=random.uniform(20.00, 29.99),
                source=random.choice(('monobank', 'privatbank', 'vkurse')))

            ContactUs.objects.create(
                email_from=fake.email(),
                subject=fake.sentence(),
                message=fake.text())
