from .views import *
from django.urls import path

urlpatterns = [
    path('login/', user_login, name="login"),
    path('logout/', user_logout, name="logout"),
    path('', home, name='home'),
    # path('hr/', HRView.as_view(), name='hr'),
    path('hr/', hr_view, name='hr'),
    path('boss/', boss_view, name='boss'),
    path('new_employees/', new_employee, name='new_employee'),
    path('employee/<int:pk>/<str:user_name>', ViewEmployee.as_view(), name='employee'),

]