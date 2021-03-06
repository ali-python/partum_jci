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
from philip_inventory.models import Invoice, StockIn, Customer, StockOut
from philip_inventory.forms import InvoiceForm, CustomerForm, StockOutForm, CustomerLedgerForm

class InvoiceListView(ListView):
    template_name = 'philip_inventory/sales/invoice_list.html'
    model = Invoice
    paginate_by = 100

    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return HttpResponseRedirect(reverse('common:login'))

        return super(
            InvoiceListView, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        queryset = self.queryset
        if not queryset:
            queryset = Invoice.objects.all().order_by('-id')

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


class CreateInvoiceTemplateView(TemplateView):
    template_name = 'philip_inventory/sales/create_invoice.html'

    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return HttpResponseRedirect(reverse('common:login'))

        return super(
            CreateInvoiceTemplateView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(CreateInvoiceTemplateView, self).get_context_data(**kwargs)
        context.update({
            'customers': Customer.objects.all().order_by('name'),
            'cars': StockIn.objects.all().order_by('car_brand'),
            'today_date': timezone.now().date(),
        })
        return context


class ProductListAPIView(View):

    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return HttpResponseRedirect(reverse('common:login'))

        return super(
            ProductListAPIView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        products = StockIn.objects.filter(status_car=True)
        items = []

        for product in products:
            p = {
                'id': product.id,
                'name': product.car_name,
                'car_model': product.car_model,
                'chasis': product.chasis_number,
                'colour': product.colour,
                'category_name': product.car_brand.brand_name,
                'price': product.buying_price
            }

            # if product:
            #     stock_detail = StockIn.objects.filter(status='Available')
            #     p.update({
            #         'buying_price': '%g' % stock_detail.buying_price,
            #     })
            # else:
            #     p.update(
            #         {
            #             'buying_price': 0
            #         }
            #     )

            items.append(p)

        return JsonResponse({'products': items})

class GenerateInvoiceAPIView(View):

    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return HttpResponseRedirect(reverse('common:login'))

        return super(
            GenerateInvoiceAPIView, self).dispatch(request, *args, **kwargs)

    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super(GenerateInvoiceAPIView, self).dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
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
            invoice_form = InvoiceForm(invoice_form_kwargs)
            print(invoice_form.errors)
            print("____________________________philip invoiceform errors________________________")
            invoice = invoice_form.save(commit=False)
            invoice_form.save()
            if self.request.POST.get('customer_id'):
                customer_id = self.request.POST.get('customer_id')
                customer = Customer.objects.get(id=customer_id)
            else:
                customer_form_kwargs = {
                    'name': name,
                    'cnic': cnic,
                    'mobile': mobile,
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
                product = StockIn.objects.get(id=item.get('item_id'))
                latest_stockin = StockIn.objects.all().latest('id')
                stock_out_kwargs = {
                    'car': product.id,
                    'invoice': invoice.id,
                    'sale_price': (
                            float(item.get('price'))),
                    'country': invoice.country,
                    'date': timezone.now().date()
                }
                stock_out = StockOutForm(stock_out_kwargs)
                print(stock_out.errors)
                print("_____________________________F_______________________")
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


class InvoiceDetailTemplateView(TemplateView):
    template_name = 'philip_inventory/sales/invoice_detail.html'

    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return HttpResponseRedirect(reverse('common:login'))

        return super(
            InvoiceDetailTemplateView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(InvoiceDetailTemplateView, self).get_context_data(**kwargs)
        invoice = Invoice.objects.get(id=self.kwargs.get('pk'))
        context.update({
            'invoice': invoice
        })
        return context


class DeleteInvoice(DeleteView):
    model = Invoice
    success_url = reverse_lazy('philip_inventory:invoice_list')
    success_message = ''

    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return HttpResponseRedirect(reverse('common:login'))

        return super(
            DeleteInvoice, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)