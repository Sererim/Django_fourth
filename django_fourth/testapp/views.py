from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.utils.timezone import datetime, timedelta
from .models import Client, Order


def order_list(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        surname = request.POST.get('surname')
        timeframe = request.POST.get('timeframe')

        if firstname and surname and timeframe:
            if timeframe == '7':
                start_date = datetime.now() - timedelta(days=7)
            elif timeframe == '30':
                start_date = datetime.now() - timedelta(days=30)
            elif timeframe == '365':
                start_date = datetime.now() - timedelta(days=365)
            else:
                pass

            client = Client.objects.filter(firstname=firstname, surname=surname).first()
            orders = Order.objects.filter(client_id=client, date_of_order__gte=start_date)
            
            context = {
                'orders': orders,
                'client': client,
            }
            return render(request, 'testapp/order_list.html', context)

    return render(request, 'testapp/index.html')