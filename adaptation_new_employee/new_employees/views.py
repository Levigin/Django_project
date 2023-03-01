from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .forms import *
from django.views.generic import ListView


def user_login(request):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if HR.objects.filter(user_name=user):
                return redirect('hr')
            elif Boss.objects.filter(user_name=user):
                return redirect('boss')
            elif NewEmployee.objects.filter(user_name=user):
                return redirect('new_employee')
            else:
                return redirect('home')
    else:
        form = UserLoginForm()
    return render(request, 'new_employees/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('login')


def home(request):
    return render(request, 'new_employees/home.html')


class HRView(ListView):
    model = HR
    template_name = 'new_employees/hr.html'
    context_object_name = 'hr'

    def get_queryset(self):
        user = self.request.user
        print(f'user: {user}')
        qr = HR.objects.get(user_name=user)
        hr_empl = qr.employees.all()
        print(f'qr: = {qr.employees.all()}')
        return render(self.request, self.template_name, {'hr_empl': hr_empl})


def hr_view(request):
    user = request.user
    hr = HR.objects.get(user_name=user)
    hr_employees = hr.employees.all()
    return render(request, 'new_employees/hr.html', {'hr_employees': hr_employees, 'hr': hr})


def boss_view(request):
    user = request.user
    boss = Boss.objects.get(user_name=user)
    boss_subordinates = boss.subordinates.all()
    return render(request, 'new_employees/boss.html', {'boss_subordinates': boss_subordinates, 'boss': boss})


def new_employee(request):
    user = request.user
    employee = NewEmployee.objects.get(user_name=user)
    return render(request, 'new_employees/new_employee.html', {'employee': employee})


class ViewEmployee(ListView):
    model = NewEmployee
    template_name = 'new_employees/employee.html'
    context_object_name = 'employee'

