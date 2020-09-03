from django.urls import path
from japan_inventory.expense_views import (
    AddExpense, ExpenseList, DeleteExpense, UpdateExpense
)

urlpatterns = [
    path('add/expense/', AddExpense.as_view(), name='expense_add'),
    path('list/expense/', ExpenseList.as_view(), name='expense_list'),
    path('delete/<int:pk>/expense/', DeleteExpense.as_view(), name='expense_delete'),
    path('update/<int:pk>/expense/', UpdateExpense.as_view(), name='expense_update'),

]