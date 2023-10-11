from django.core.management.base import BaseCommand
from random import randint
from testapp.models import Product
from decimal import Decimal


class Command(BaseCommand):
    help = "Populates Product table with ten products and their prices."

    def handle(self, *args: any, **options: any) -> None:
        name: str = ""
        print: Decimal = 0.00
        
        with open("products.txt", '+r') as f:
            s = f.read().splitlines()
        
        for x in s[1:-1]:
            name, price = x.strip().split("-")
            product = Product(
                name=name, description=f"Very good {name}. BUY it. It costs {price}",
                price=price, amount=randint(1, 25)
            )
            product.save()
            self.stdout.write(f"{product}")
    