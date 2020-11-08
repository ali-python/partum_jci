import json
from django.core.paginator import Paginator
from django.views.generic import ListView, TemplateView, View, DeleteView
from django.http import JsonResponse
from django.db.models import Sum
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.db import transaction
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from japan_inventory.models import CarPartsInvoice, CarBuyPart, Customer, CarPartsStockOut
from japan_inventory.forms import CarPartsInvoiceForm, CustomerForm, CarPartsStockoutForm, CustomerLedgerForm

class CarPartsInvoiceListView(ListView):
    template_name = 'sales/invoice_list_car_parts.html'
    model = CarPartsInvoice
    paginate_by = 100

    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return HttpResponseRedirect(reverse('common:login'))

        return super(
            CarPartsInvoiceListView, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        queryset = self.queryset
        if not queryset:
            queryset = CarPartsInvoice.objects.all().order_by('-id')

        if self.request.GET.get('customer_name'):
            queryset = queryset.filter(
                customer__name__contains=self.request.GET.get('customer_name'))

        if self.request.GET.get('customer_id'):
            queryset = queryset.filter(
                id=self.request.GET.get('customer_id').lstrip('0')
            )

        if self.request.GET.get('bill_no'):
            queryset = queryset.filter(
                bill_no=self.request.GET.get('bill_no')
            )

        if self.request.GET.get('date'):
            queryset = queryset.filter(
                date=self.request.GET.get('date')
            )

        return queryset.order_by('-id')


class CarPartsCreateInvoiceTemplateView(TemplateView):
    template_name = 'sales/create_invoice_car_parts.html'

    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return HttpResponseRedirect(reverse('common:login'))

        return super(
            CarPartsCreateInvoiceTemplateView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(CarPartsCreateInvoiceTemplateView, self).get_context_data(**kwargs)
        context.update({
            'customers': Customer.objects.all().order_by('name'),
            'cars': CarBuyPart.objects.all(),
            'today_date': timezone.now().date(),
        })
        return context


class CarPartsProductListAPIView(View):

    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return HttpResponseRedirect(reverse('common:login'))

        return super(
            CarPartsProductListAPIView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        print('__________________coming here__________________')
        products = CarBuyPart.objects.filter(status=True)
        print(products)
        items = []

        for product in products:
            p = {
                'id': product.id,
                'name': product.description,
                'price': product.amount
            }
            print(product.description)
            print(product.amount)
            print("__________________________")

            items.append(p)

        return JsonResponse({'products': items})

class CarPartsGenerateInvoiceAPIView(View):

    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return HttpResponseRedirect(reverse('common:login'))

        return super(
            CarPartsGenerateInvoiceAPIView, self).dispatch(request, *args, **kwargs)

    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super(CarPartsGenerateInvoiceAPIView, self).dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        print(self.request.POST.get('customer_name'))
        print(self.request.POST.get('country'))
        print("______________________________________")
        name = self.request.POST.get('customer_name')
        mobile = self.request.POST.get('customer_phone')
        cnic = self.request.POST.get('customer_cnic')
        sub_total = self.request.POST.get('sub_total')
        discount = self.request.POST.get('discount')
        shipping = self.request.POST.get('shipping')
        grand_total = self.request.POST.get('grand_total')
        totalQty = self.request.POST.get('totalQty')
        remaining_payment = self.request.POST.get('remaining_amount')
        paid_amount = self.request.POST.get('paid_amount')
        cash_payment = self.request.POST.get('cash_payment')
        returned_cash = self.request.POST.get('returned_cash')
        dated = self.request.POST.get('dated')
        bill_no = self.request.POST.get('bill_no')
        country = self.request.POST.get('country')
        items = json.loads(self.request.POST.get('items'))

        with transaction.atomic():
            invoice_form_kwargs = {
                'bill_no': bill_no,
                'date': dated,
                'discount': float(discount),
                'sub_total': float(sub_total),
                'grand_total': float(grand_total),
                'total_quantity': totalQty,
                'shipping': float(shipping),
                'paid_amount': float(paid_amount),
                'remaining_payment': float(remaining_payment),
                'cash_payment': float(cash_payment),
                'returned_payment': float(returned_cash),
                'country': country,
            }
            invoice_form = CarPartsInvoiceForm(invoice_form_kwargs)
            invoice = invoice_form.save(commit=False)
            invoice_form.save()
            if self.request.POST.get('customer_id'):
                customer_id = self.request.POST.get('customer_id')
                customer = Customer.objects.get(id=customer_id)
            else:
                customer_form_kwargs = {
                    'name': customer_name,
                    'cnic': customer_cnic,
                    'mobile': customer_phone,
                }
                customer_form = CustomerForm(customer_form_kwargs)
                if customer_form.is_valid():
                    customer = customer_form.save()
                    customer_id = customer.id
                else:
                    customer_id = ''

            if customer_id:
                invoice.customer = customer
                invoice.save()

            for item in items:
                product = CarBuyPart.objects.get(id=item.get('item_id'))
                latest_stockin = CarBuyPart.objects.all().latest('id')
                stock_out_kwargs = {
                    'car_parts': product.id,
                    'invoice': invoice.id,
                    'stock_out_quantity':  float(item.get('qty')),
                    'sale_price': (
                            float(item.get('price'))),
                    'country': invoice.country,
                    'date': timezone.now().date()
                }
                stock_out = CarPartsStockoutForm(stock_out_kwargs)
                stock_out.save()
                product.status_car = False
                product.save()

            if customer_id or self.request.POST.get('customer_id'):
                if float(remaining_payment):
                    ledger_form_kwargs = {
                        'customer': customer_id,
                        'invoice': invoice.id,
                        'debit_amount': float(remaining_payment),
                        'details': (
                                'Remaining Payment for Bill/Receipt No %s '
                                % str(invoice.id).zfill(7)),
                        'date': timezone.now()
                    }

                    customer_ledger = CustomerLedgerForm(ledger_form_kwargs)
                    customer_ledger.save()


        return JsonResponse({'invoice_id': invoice.id})


class CarPartsInvoiceDetailTemplateView(TemplateView):
    template_name = 'sales/car_parts_invoice_detail.html'

    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return HttpResponseRedirect(reverse('common:login'))

        return super(
            CarPartsInvoiceDetailTemplateView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(CarPartsInvoiceDetailTemplateView, self).get_context_data(**kwargs)
        invoice = CarPartsInvoice.objects.get(id=self.kwargs.get('pk'))
        context.update({
            'invoice': invoice
        })
        return context