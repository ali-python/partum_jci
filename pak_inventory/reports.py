from django.shortcuts import render
from django.views.generic import TemplateView
from django.db.models import Sum
from django.utils import timezone
from pak_inventory.models import Invoice, Customer, Expense, CustomerLedger
from calendar import monthrange
from dateutil.relativedelta import relativedelta
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import forms as auth_forms
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.views.generic import TemplateView, RedirectView, UpdateView
from django.views.generic import FormView
from django.http import HttpResponseRedirect,HttpResponse
from common.models import AdminConfiguration

class MonthlyReports(TemplateView):
    template_name = 'pak_inventory/monthly_reports.html'

    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return HttpResponseRedirect(reverse('common:login'))

        return super(
            MonthlyReports, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(MonthlyReports, self).get_context_data(**kwargs)
        data_result = []
        for month in range(60):
            data = {}
            date_month = timezone.now() - relativedelta(months=month)
            month_range = monthrange(
                date_month.year, date_month.month
            )
            start_month = datetime.datetime(
                date_month.year, date_month.month, 1)

            end_month = datetime.datetime(
                date_month.year, date_month.month, month_range[1]
            )

            invoice = Invoice.objects.filter(
                date__gt=start_month,
                date__lt=end_month.replace(
                    hour=23, minute=59, second=59))

            if invoice.exists():
                commission = invoice.aggregate(
                    Sum('grand_total'))
                grand_total = float(
                    commission.get('grand_total__sum') or 0
                )

            else:
                grand_total = 0

            if invoice.exists():
                cash_payment = invoice.aggregate(
                    Sum('cash_payment'))
                total_cash_payment = float(
                    cash_payment.get(
                        'cash_payment__sum') or 0
                )
            else:
                total_cash_payment = 0

            if invoice.exists():
                quantity = invoice.aggregate(
                    Sum('total_quantity'))
                total_quantity = float(
                    quantity.get(
                        'total_quantity__sum') or 0
                )
            else:
                total_quantity = 0

            customer = Customer.objects.filter(
                date__gt=start_month,
                date__lt=end_month.replace(
                    hour=23, minute=59, second=59))

            if customer.exists():
                total_customer = customer.count()
                print(total_customer)
                print("__________________________")

            else:
                total_customer = 0
                print(total_customer)
                

            expense_record = Expense.objects.filter(
                date__gt=start_month,
                date__lt=end_month.replace(
                    hour=23, minute=59, second=59))

            if expense_record.exists():
                amount = expense_record.aggregate(
                    Sum('amount'))
                total_expense_amount = float(
                    amount.get(
                        'amount__sum') or 0
                )

            else:
                total_expense_amount = 0

            customer_ledger = CustomerLedger.objects.filter(
                date__gt=start_month,
                date__lt=end_month.replace(
                    hour=23, minute=59, second=59))

            if customer_ledger.exists():
                debit_amount = customer_ledger.aggregate(
                    Sum('debit_amount'))
                print(debit_amount.get('debit_amount__sum'))
                print('-----------------11----------------')
                print('-----------------11----------------')
                print('-----------------11----------------')
                total_debit_amount = float(
                    debit_amount.get(
                        'debit_amount__sum') or 0
                )

            else:
                total_debit_amount = 0

            if customer_ledger.exists():
                credit_amount = customer_ledger.aggregate(
                    Sum('credit_amount'))
                total_credit_amount = float(
                    credit_amount.get(
                        'credit_amount__sum') or 0
                )

            else:
                total_credit_amount = 0

            data.update({
               'grand_total': grand_total,
               'total_cash_payment': total_cash_payment,
               'total_quantity': total_quantity,
               'total_customer': total_customer,
               'total_expense_amount': total_expense_amount,
               'total_credit_amount':total_credit_amount,
               'total_debit_amount':total_debit_amount,
               'date': start_month.strftime('%b-%y')
            })
            data_result.append(data)

        context.update({
            'results': data_result
        })
        print(context)
        return context