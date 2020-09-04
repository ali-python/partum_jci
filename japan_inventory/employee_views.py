from django.shortcuts import render
from japan_inventory.forms import EmployeeFormView
from japan_inventory.models import Employee
from django.views.generic import ListView, FormView, DeleteView, UpdateView
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy


class AddEmployee(FormView):
    form_class = EmployeeFormView
    template_name = 'employee/add_employee.html'

    # def dispatch(self, request, *args, **kwargs):
    #     if not self.request.user.is_authenticated:
    #         return HttpResponseRedirect(reverse('common:login'))

    #     return super(
    #         AddEmployee, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
       form.save()
       return HttpResponseRedirect(reverse('employee:employee_list'))

    def form_invalid(self, form):
        return super(AddEmployee, self).form_invalid(form)