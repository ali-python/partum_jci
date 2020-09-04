from django.urls import path
from japan_inventory.expense_views import (
    AddExpense, ExpenseList, UpdateExpense, DeleteExpense
)

urlpatterns = [
    path('add/expense/', AddExpense.as_view(), name='expense_add'),
    path('list/expense/', ExpenseList.as_view(), name='expense_list'),
    path('delete/expense/<int:pk>/', DeleteExpense.as_view(), name='expense_delete'),
    path('update/expense/<int:pk>/', UpdateExpense.as_view(), name='expense_update'),

]