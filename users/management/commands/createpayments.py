from django.core.management import BaseCommand

from users.models import Payment


class Command(BaseCommand):
    """Создание суперюзера"""

    def handle(self, *args, **options):
        data = [
            {'price': '5000', 'payment_method': 'cash'},
            {'price': '10000', 'payment_method': 'non_cash'},
            {'price': '2000', 'payment_method': 'non_cash'},
            {'price': '2000', 'payment_method': 'non_cash'}
        ]

        for each in data:
            pay = Payment.objects.create(**each)

            pay.save()
