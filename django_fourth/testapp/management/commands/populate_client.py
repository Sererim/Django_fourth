from django.core.management.base import BaseCommand
from random import shuffle, randint
from testapp.models import Client


class Command(BaseCommand):
    help = "Populates Client table with randomly generated clients.\n" \
           "Amount must be specified"

    def add_arguments(self, parser):
        parser.add_argument('amount', type=int, help="Amount of clients to create.")

    def handle(self, *args, **options):
        amount = options['amount']
        names: list[str] = []
        surnames: list[str] = []
        num: int = 0
        phone: list[str] = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        countries: list[str] = ["USA, New York, New York", "USA, D.C. Washington", "USA, Ohio, Columbus",
                                "USA, Maryland, Baltimore", "USA, Delaware, Dover", "USA, West Virginia, Charleston",
                                "UK, London", "UK, Oxford", "UK, York", "UK, Edinburgh"]
        with open("names.txt", '+r') as source_names, \
                open("lastnames.txt", '+r') as source_lastnames:
            names = source_names.read().splitlines()
            surnames = source_lastnames.read().splitlines()

        shuffle(names)
        shuffle(surnames)
        
        for _ in range(amount):
            num = randint(0, len(names) - 1)
            shuffle(phone)
            client = Client(
                firstname=names[num], surname=surnames[num], email=f"{names[num]}@test.com",
                phone_number=f"+{randint(1, 20)}" + ''.join(map(str, phone)),
                address=countries[randint(0, len(countries) - 1)]
            )
            client.save()
            self.stdout.write(f'{client}')
            names.pop(num), surnames.pop(num)
