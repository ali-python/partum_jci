from django.urls import path
from pak_inventory.stock_views import (
    AddCarBrand, CarBrandList, DeleteCarBrand, AddCarStock,
    CarStockList, DeleteCarStock, UpdateCarStockIn, AddCarParts,
    CarPartsList, DeleteCarPartsStock
)
from pak_inventory.expense_views import (
    AddExpense, ExpenseList, UpdateExpense, DeleteExpense
)
from pak_inventory.employee_views import (
    AddEmployee, EmployeeList, UpdateEmployee, DeleteEmployee,
    EmployeeSalaryFormView, EmployeeSalaryListView, DeleteEmployeeSalary
)
from pak_inventory.customer_views import (
    AddCustomer, CustomerList, UpdateCustomer, DeleteCustomer, CustomerLedgerListView, DeleteCustomerLedger, DebitCustomerLedgerFormView, CreditCustomerLedgerFormView
)
# from pak_inventory.invoice_views import (
#     InvoiceListView, CreateInvoiceTemplateView, ProductListAPIView, GenerateInvoiceAPIView, InvoiceDetailTemplateView
# )

urlpatterns = [
    path('add/expense/', AddExpense.as_view(), name='expense_add'),
    path('list/expense/', ExpenseList.as_view(), name='expense_list'),
    path('delete/expense/<int:pk>/', DeleteExpense.as_view(), name='expense_delete'),
    path('update/expense/<int:pk>/', UpdateExpense.as_view(), name='expense_update'),
    path('add/employee/', AddEmployee.as_view(), name='add_employee'),
    path('list/employee/', EmployeeList.as_view(), name='employee_list'),
    path('update/employee/<int:pk>/', UpdateEmployee.as_view(), name='employee_update'),
    path('delete/employee/<int:pk>/', DeleteEmployee.as_view(), name='employee_delete'),
    path('employee/salary/<int:pk>/', EmployeeSalaryFormView.as_view(), name='employee_salary'),
    path('employee/salary/detail/<int:pk>/', EmployeeSalaryListView.as_view(), name='employee_salary_detail'),
    path('delete/employee/salary/detail/<int:pk>/', DeleteEmployeeSalary.as_view(), name='delete_employee_salary'),
    path('add/car/brand/', AddCarBrand.as_view(), name='add_car_brand'),
    path('list/brand/', CarBrandList.as_view(), name='list_car_brand'),
    path('delete/<int:pk>/', DeleteCarBrand.as_view(), name='delete_car_brand'),
    path('add/car/stock/in/', AddCarStock.as_view(), name='add_car_stockin'),
    path('car/stock/in/list/', CarStockList.as_view(), name='car_stock_list'),
    path('car/stock/<int:pk>/delete/', DeleteCarStock.as_view(), name='delete_car_stockin'),
    path('update/car/<int:pk>/stock/in/', UpdateCarStockIn.as_view(), name='update_car_stockin'),
    path('add/car/parts/', AddCarParts.as_view(), name='add_car_parts'),
    path('list/car/parts/', CarPartsList.as_view(), name='list_car_parts'),
    path('delete/<int:pk>/car/parts/', DeleteCarPartsStock.as_view(), name='delete_car_parts'),
    path('add/customer/', AddCustomer.as_view(), name='add_customer'),
    path('list/customer/', CustomerList.as_view(), name='customer_list'),
    path('update/customer/<int:pk>/', UpdateCustomer.as_view(), name='customer_update'),
    path('delete/customer/<int:pk>/', DeleteCustomer.as_view(), name='customer_delete'),
    # path('list/invoice/', InvoiceListView.as_view(), name='invoice_list'),
    # path('add/invoice/customer/', CreateInvoiceTemplateView.as_view(), name='add_invoice'),
    # path('product/invoice/customer/api/', ProductListAPIView.as_view(), name='product_api'),
    # path('generate/invoice/api/', GenerateInvoiceAPIView.as_view(), name='generate_invoice'),
    # path("invoice/<int:pk>/detail/", InvoiceDetailTemplateView.as_view(), name='invoice_detail'),
    path('<int:pk>/ledger/delete', DeleteCustomerLedger.as_view(), name='delete_ledger'),
    path(
        '<int:pk>/ledger/list/',
        CustomerLedgerListView.as_view(),
        name='ledger_list'
    ),
    path(
        '<int:pk>/ledger/debit/',
        DebitCustomerLedgerFormView.as_view(),
        name='ledger_debit'
    ),
    path(
        '<int:pk>/ledger/credit/',
        CreditCustomerLedgerFormView.as_view(),
        name='ledger_credit'
    ),

]