from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from .forms import *
from django.views.generic import ListView
from adaptation_new_employee import settings


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
    # print(request.session['_auth_user_id'])
    employee = NewEmployee.objects.get(user_name=user)
    missions = MissionsModel.objects.filter(employee=employee.pk)
    # print(f'missions: {missions}')
    return render(request, 'new_employees/new_employee.html', {'employee': employee, 'missions': missions})


class ViewEmployee(ListView):
    model = NewEmployee
    template_name = 'new_employees/employee.html'
    context_object_name = 'employee'


def view_employee(request, user_id):
    employee = get_object_or_404(NewEmployee, pk=user_id)
    return render(request, 'new_employees/employee.html', {'employee': employee})
    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #
    #     return context


def add_missions(request, user_id):
    if request.method == 'POST':
        form = MissionsForm(request.POST)
        employee = NewEmployee.objects.get(pk=user_id)
        if form.is_valid():
            mission = form.save(commit=False)
            mission.employee = employee
            mission.save()
            try:
                send_mail('', f'У ВАС НОВОЕ ЗАДАНИЕ от {request.user}:\n{mission.content}', settings.EMAIL_HOST_USER,
                          [employee.email])
            except Exception:
                return HttpResponse('Ошибка в теме письма.')
            return redirect('home')
    else:
        form = MissionsForm()

    return render(request, 'new_employees/mission.html', {'form': form})
