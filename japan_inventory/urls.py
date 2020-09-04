from django.urls import path
from japan_inventory.stock_views import (AddCarBrand, CarBrandList, DeleteCarBrand,
	AddCarStock, CarStockList, DeleteCarStock, UpdateCarStockIn)


urlpatterns = [

    path('add/car/brand/', AddCarBrand.as_view(), name='add_car_brand'),
    path('list/', CarBrandList.as_view(), name='list_car_brand'),
    path('delete/<int:pk>/', DeleteCarBrand.as_view(), name='delete_car_brand'),
    path('add/car/stock/in/', AddCarStock.as_view(), name='add_car_stockin'),
    path('car/stock/list/', CarStockList.as_view(), name='car_stock_list'),
    path('car/stock/<int:pk>/delete/', DeleteCarStock.as_view(), name='delete_car_stockin'),
    path('update/car/<int:pk>/stock/in/', UpdateCarStockIn.as_view(), name='update_car_stockin'),
]