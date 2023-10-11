from django.core.management.base import BaseCommand
from testapp.models import Client, Product, Order


class Command(BaseCommand):
    help = "Prints out who and what was ordered.\n" \
            "Needs id of an oreder"
    
    def add_arguments(self, parser) -> None:
        parser.add_argument('order_id', type=int, help="Id of an order to check who and what was ordered")
    
    def handle(self, *args: any, **options: any):
        order_id = options['order_id']
        
        client = Order.objects.get(id=order_id).client_id
        product = Order.objects.get(id=order_id).product_id
        
        self.stdout.write(f"{client}\n{product}")
    