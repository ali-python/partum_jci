from japan_inventory.forms import (
    CarBrandForm, StockInForm, StockOutForm
)
from japan_inventory.models import (
    CarBrand, StockIn, StockOut
)
from django.views.generic import ListView, FormView, UpdateView, DeleteView
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404

############# car brand views########################
class AddCarBrand(FormView):
    form_class = CarBrandForm
    template_name = 'carbrand/add_car_brand.html'

    # def dispatch(self, request, *args, **kwargs):
    #     if not self.request.user.is_authenticated:
    #         return HttpResponseRedirect(reverse('common:login'))

    #     return super(
    #         AddProductCategory, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(reverse('japan_inventory:list_car_brand'))

    def form_invalid(self, form):
        return super(AddCarBrand, self).form_invalid(form)


class CarBrandList(ListView):
    model = CarBrand
    template_name = 'carbrand/list_car_brand.html'
    paginate_by = 100
    ordering = 'brand_name'

    # def dispatch(self, request, *args, **kwargs):
    #     if not self.request.user.is_authenticated:
    #         return HttpResponseRedirect(reverse('common:login'))

    #     return super(
    #         ProductList, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        queryset = self.queryset
        if not queryset:
            queryset = CarBrand.objects.all().order_by('-id')
        if self.request.GET.get('car_brand_name'):
            queryset = queryset.filter(
                brand_name__contains=self.request.GET.get('car_brand_name')
            )
        return queryset.order_by('brand_name')


class DeleteCarBrand(DeleteView):
    model = CarBrand
    success_url = reverse_lazy('japan_inventory:list_car_brand')
    success_message = ''

    # def dispatch(self, request, *args, **kwargs):
    #     if not self.request.user.is_authenticated:
    #         return HttpResponseRedirect(reverse('common:login'))

    #     return super(
    #         DeleteProduct, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

################ end car brand views##############################


######### stock views #####################################

class AddCarStock(FormView):
    form_class = StockInForm
    template_name = 'stock/add_stock.html'

    # def dispatch(self, request, *args, **kwargs):
    #     if not self.request.user.is_authenticated:
    #         return HttpResponseRedirect(reverse('common:login'))

    #     return super(
    #         AddProductCategory, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(reverse('japan_inventory:car_stock_list'))

    def form_invalid(self, form):
        return super(AddCarStock, self).form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super(AddCarStock, self).get_context_data(**kwargs)
        brand = CarBrand.objects.all()
        context.update({
            'brand': brand
        })
        return context


class CarStockList(ListView):
    model = CarBrand
    template_name = 'stock/stock_list.html'
    paginate_by = 100
    ordering = 'car_brand'

    # def dispatch(self, request, *args, **kwargs):
    #     if not self.request.user.is_authenticated:
    #         return HttpResponseRedirect(reverse('common:login'))

    #     return super(
    #         ProductList, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        queryset = self.queryset
        if not queryset:
            queryset = StockIn.objects.all().order_by('-id')
        if self.request.GET.get('chasis_number'):
            queryset = queryset.filter(
                chasis_number__contains=self.request.GET.get('chasis_number')
            )
        return queryset.order_by('chasis_number')


class DeleteCarStock(DeleteView):
    model = StockIn
    success_url = reverse_lazy('japan_inventory:car_stock_list')
    success_message = ''

    # def dispatch(self, request, *args, **kwargs):
    #     if not self.request.user.is_authenticated:
    #         return HttpResponseRedirect(reverse('common:login'))

    #     return super(
    #         DeleteProduct, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


class UpdateCarStockIn(UpdateView):
    model = StockIn
    form_class = StockInForm
    template_name = 'stock/update_stockin.html'

    # def dispatch(self, request, *args, **kwargs):
    #     if not self.request.user.is_authenticated:
    #         return HttpResponseRedirect(reverse('common:login'))

    #     return super(
    #         UpdateStockIn, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        obj = form.save()
        return HttpResponseRedirect(reverse('japan_inventory:car_stock_list'))

    def form_invalid(self, form):
        return super(UpdateCarStockIn, self).form_invalid(form)



