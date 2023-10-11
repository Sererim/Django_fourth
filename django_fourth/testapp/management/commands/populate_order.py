from django.core.management.base import BaseCommand
from random import randint
from testapp.models import Order, Client, Product
from decimal import Decimal


class Command(BaseCommand):
    help = "Creates a single order. Takes two arguments.\n" \
            "Client id and product id."
    
    def add_arguments(self, parser) -> None:
        parser.add_argument('client_id', type=int, help="Client id.")
        parser.add_argument('product_id', type=int, help="Product id.")
        parser.add_argument('cost', type=Decimal, help="Cost of the order.")
    
    def handle(self, *args: any, **options: any) -> None:
        client_id = options['client_id']
        product_id = options['product_id']
        cost = options['cost']
        
        order = Order(
            client_id=Client.objects.get(id=client_id), product_id=Product.objects.get(id=product_id), cost=cost
        )
        
        order.save()
        self.stdout.write(f"{order}")
