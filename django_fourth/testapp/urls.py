from django.urls import path
from .views import order_list, upload_image, product_details

urlpatterns = [
    path('', order_list, name='order_list'),
    path('upload/<int:product_id>', upload_image, name='upload_image'),
    path('product/<int:product_id>/', product_details, name='product_details')
]
