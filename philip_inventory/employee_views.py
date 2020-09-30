from django.shortcuts import render
from philip_inventory.forms import EmployeeFormView, EmployeeSalaryForm
from philip_inventory.models import Employee, EmployeeSalary
from django.views.generic import ListView, FormView, DeleteView, UpdateView, TemplateView
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.http import Http404


class AddEmployee(FormView):
    form_class = EmployeeFormView
    template_name = 'philip_inventory/employee/add_employee.html'

    # def dispatch(self, request, *args, **kwargs):
    #     if not self.request.user.is_authenticated:
    #         return HttpResponseRedirect(reverse('common:login'))
    #
    #     return super(
    #         AddEmployee, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
       form.save()
       return HttpResponseRedirect(reverse('philip_inventory:employee_list'))

    def form_invalid(self, form):
        return super(AddEmployee, self).form_invalid(form)


class EmployeeList(ListView):
    template_name = 'philip_inventory/employee/employee_list.html'
    model = Employee
    paginate_by = 100
    ordering = 'name'

    # def dispatch(self, request, *args, **kwargs):
    #     if not self.request.user.is_authenticated:
    #         return HttpResponseRedirect(reverse('common:login'))
    #
    #     return super(
    #         EmployeeList, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        queryset = self.queryset
        if not queryset:
            queryset = Employee.objects.all().order_by('employee_name')

        if self.request.GET.get('employee_name'):
            queryset = queryset.filter(
                employee_name__icontains=self.request.GET.get('employee_name'))

        if self.request.GET.get('employee_cnic'):
            queryset = queryset.filter(
                employee_cnic=self.request.GET.get('employee_cnic').lstrip('0')
            )

        return queryset.order_by('employee_name')


class UpdateEmployee(UpdateView):
    model = Employee
    form_class = EmployeeFormView
    template_name = 'philip_inventory/employee/update_employee.html'

    # def dispatch(self, request, *args, **kwargs):
    #     if not self.request.user.is_authenticated:
    #         return HttpResponseRedirect(reverse('common:login'))
    #
    #     return super(
    #         UpdateEmployee, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(reverse('philip_inventory:employee_list'))

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
    success_url = reverse_lazy('philip_inventory:employee_list')
    success_message = ''

    # def dispatch(self, request, *args, **kwargs):
    #     if not self.request.user.is_authenticated:
    #         return HttpResponseRedirect(reverse('common:login'))
    #
    #     return super(
    #         DeleteEmployee, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


class EmployeeSalaryFormView(FormView):
    template_name = 'philip_inventory/employee/employee_salary.html'
    form_class = EmployeeSalaryForm

    # def dispatch(self, request, *args, **kwargs):
    #     if not self.request.user.is_authenticated:
    #         return HttpResponseRedirect(reverse('common:login'))

    #     return super(
    #         DebitCustomerLedgerFormView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        obj = form.save()
        return HttpResponseRedirect(
            reverse('philip_inventory:employee_salary_detail',
                    kwargs={'pk': obj.employee.id}
                    )
        )

    def form_invalid(self, form):
        return super(EmployeeSalaryFormView, self).form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super(
            EmployeeSalaryFormView, self).get_context_data(**kwargs)
        try:
            employee = Employee.objects.get(id=self.kwargs.get('pk'))
        except Employee.DoesNotExist:
            raise Http404('Employee does not exits!')

        context.update({
            'employee': employee
        })
        return context


class EmployeeSalaryListView(TemplateView):
    model = EmployeeSalary
    template_name = 'philip_inventory/employee/employee_salary_detail.html'

    # def dispatch(self, request, *args, **kwargs):
    #     if not self.request.user.is_authenticated:
    #         return HttpResponseRedirect(reverse('common:login'))
    #
    #     return super(
    #         EmployeeSalaryListView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(
            EmployeeSalaryListView, self).get_context_data(**kwargs)

        try:
            employee = EmployeeSalary.objects.filter(employee__id=self.kwargs.get('pk'))
        except EmployeeSalary.DoesNotExist:
            raise Http404('Employee does not exits!')

        context.update({
            'emp' : Employee.objects.get(id=self.kwargs.get('pk')),
            'employee': employee
        })
        return context


class DeleteEmployeeSalary(DeleteView):
    model = EmployeeSalary
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
        success_url = reverse_lazy('philip_inventory:employee_salary_detail', kwargs={
                                   'pk': obj.employee.id})
        obj.delete()

        return HttpResponseRedirect(success_url)