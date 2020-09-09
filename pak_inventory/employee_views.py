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
    #
    #     return super(
    #         AddEmployee, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
       form.save()
       return HttpResponseRedirect(reverse('pak_inventory:employee_list'))

    def form_invalid(self, form):
        return super(AddEmployee, self).form_invalid(form)


class EmployeeList(ListView):
    template_name = 'employee/employee_list.html'
    model = Employee
    paginate_by = 100
    ordering = '-id'

    # def dispatch(self, request, *args, **kwargs):
    #     if not self.request.user.is_authenticated:
    #         return HttpResponseRedirect(reverse('common:login'))
    #
    #     return super(
    #         EmployeeList, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(EmployeeList, self).get_context_data(**kwargs)
        employees = (
            Employee.objects.all()
        )
        context.update({
            'employees': employees
        })
        return context


class UpdateEmployee(UpdateView):
    model = Employee
    form_class = EmployeeFormView
    template_name = 'employee/update_employee.html'

    # def dispatch(self, request, *args, **kwargs):
    #     if not self.request.user.is_authenticated:
    #         return HttpResponseRedirect(reverse('common:login'))
    #
    #     return super(
    #         UpdateEmployee, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(reverse('pak_inventory:employee_list'))

    def form_invalid(self, form):
        return super(UpdateEmployee, self).form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super(UpdateEmployee, self).get_context_data(**kwargs)
        employees = Employee.objects.all()
        context.update({
            'employees': employees
        })
        return context


class DeleteEmployee(DeleteView):
    model = Employee
    success_url = reverse_lazy('pak_inventory:employee_list')
    success_message = ''

    # def dispatch(self, request, *args, **kwargs):
    #     if not self.request.user.is_authenticated:
    #         return HttpResponseRedirect(reverse('common:login'))
    #
    #     return super(
    #         DeleteEmployee, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)