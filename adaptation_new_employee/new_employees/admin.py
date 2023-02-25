from django.contrib import admin
from .models import *


class NewEmployeeAdmin(admin.ModelAdmin):
    list_display = (
        'full_name', 'email', 'tlg', 'birthday', 'photo', 'stack', 'hobbies', 'rank', 'point', 'post')
    list_display_links = ('full_name',)


class BossAdmin(admin.ModelAdmin):
    list_display = (
        'full_name', 'email', 'tlg', 'birthday', 'photo', 'stack', 'hobbies', 'post')
    list_display_links = ('full_name',)


class HRAdmin(admin.ModelAdmin):
    list_display = (
        'full_name', 'email', 'tlg', 'birthday', 'photo', 'stack', 'hobbies', 'post')
    list_display_links = ('full_name',)


admin.site.register(NewEmployee, NewEmployeeAdmin)
admin.site.register(Boss, BossAdmin)
admin.site.register(HR, HRAdmin)