from django.shortcuts import render
from django.views.generic import ListView, FormView, UpdateView, DeleteView
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from django.db.models import Sum
from japan_inventory.models import Bank, BankLedger
from japan_inventory.forms import BankForm, BankLedgerForm


class AddBank(FormView):
    form_class = BankForm
    template_name = 'bank/add_bank.html'

    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return HttpResponseRedirect(reverse('common:login'))

        return super(
            AddBank, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(reverse('japan_inventory:bank_list'))

    def form_invalid(self, form):
        return super(AddBank, self).form_invalid(form)


class BankList(ListView):
    model = Bank
    template_name = 'bank/bank_list.html'
    paginate_by = 100
    ordering = 'name'

    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return HttpResponseRedirect(reverse('common:login'))

        return super(
            BankList, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        queryset = self.queryset
        if not queryset:
            queryset = Bank.objects.all().order_by('name')

        if self.request.GET.get('name'):
            queryset = queryset.filter(
                name__icontains=self.request.GET.get('name'))

        return queryset.order_by('name')



class DeleteBank(DeleteView):
    model = Bank
    success_url = reverse_lazy('japan_inventory:bank_list')
    success_message = ''

    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return HttpResponseRedirect(reverse('common:login'))

        return super(
            DeleteBank, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


class BankLedgerListView(ListView):
    model = BankLedger
    template_name = 'bank/bank_ledger_list.html'
    paginate_by = 100

    # def dispatch(self, request, *args, **kwargs):
    #     if not self.request.user.is_authenticated:
    #         return HttpResponseRedirect(reverse('common:login'))

    #     return super(
    #         CustomerLedgerListView, self).dispatch(request, *args, **kwargs)

    def get_queryset(self, **kwargs):

        queryset = self.queryset

        if not queryset:
            queryset = self.model.objects.filter(
                bank__id=self.kwargs.get('pk')).order_by('-date')

        if self.request.GET.get('date'):
            queryset = queryset.filter(
                date__icontains=self.request.GET.get('date')
            )

        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(
            BankLedgerListView, self).get_context_data(**kwargs)

        try:
            bank= Bank.objects.get(id=self.kwargs.get('pk'))
        except bank.DoesNotExist:
            raise Http404('bank does not exits!')

        context.update({
            'bank': bank,
        })
        return context


class DeleteBankLedger(DeleteView):
    model = BankLedger
    success_message = ''

    # def dispatch(self, request, *args, **kwargs):
    #     if not self.request.user.is_authenticated:
    #         return HttpResponseRedirect(reverse('common:login'))

    #     return super(
    #         DeleteCustomerLedger, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        success_url = reverse_lazy('japan_inventory:bank_ledger_list', kwargs={
                                   'pk': obj.bank.id})
        obj.delete()

        return HttpResponseRedirect(success_url)


class DebitBankLedgerFormView(FormView):
    template_name = 'bank/add_debit_bank.html'
    form_class = BankLedgerForm

    # def dispatch(self, request, *args, **kwargs):
    #     if not self.request.user.is_authenticated:
    #         return HttpResponseRedirect(reverse('common:login'))

    #     return super(
    #         DebitCustomerLedgerFormView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        obj = form.save()
        return HttpResponseRedirect(
            reverse('japan_inventory:bank_ledger_list',
                    kwargs={'pk': obj.bank.id}
                    )
        )

    def get_context_data(self, **kwargs):
        context = super(
            DebitBankLedgerFormView, self).get_context_data(**kwargs)
        try:
            bank = Bank.objects.get(id=self.kwargs.get('pk'))
        except Bank.DoesNotExist:
            raise Http404('bank does not exits!')

        context.update({
            'bank': bank
        })
        return context


class CreditBankLedgerFormView(DebitBankLedgerFormView):
    template_name = 'bank/add_credit_bank.html'

    # def dispatch(self, request, *args, **kwargs):
    #     if not self.request.user.is_authenticated:
    #         return HttpResponseRedirect(reverse('common:login'))

    #     return super(
    #         CreditCustomerLedgerFormView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(
            CreditBankLedgerFormView, self).get_context_data(**kwargs)
        try:
            bank = Bank.objects.get(id=self.kwargs.get('pk'))
        except Bank.DoesNotExist:
            raise Http404('Bank does not exits!')

        context.update({
            'bank': bank
        })
        return context
