from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    POSTS = ((None, 'Выберете вашу должность'),
             ('Нач. отд.', 'Начальник отдела'),
             ('HR', 'Сотрудник отдела кадров'),
             ('NE', 'Новый сотрудник'),)
    full_name = models.CharField(max_length=50, verbose_name='ФИО')
    email = models.EmailField(verbose_name="Email")
    tlg = models.URLField(verbose_name='Ссылка на соц. сети', blank=True)
    birthday = models.DateField(verbose_name="День рождения", null=True)
    photo = models.ImageField(upload_to='photo/%Y/%m/%d/', verbose_name='Фото', blank=True)
    stack = models.TextField(verbose_name='Навыки', blank=True)
    hobbies = models.TextField(verbose_name='Хобби', blank=True)
    post = models.CharField(max_length=30, verbose_name="Должность", choices=POSTS)

    def __str__(self):
        return self.full_name

    class Meta:
        abstract = True


class HR(Profile):
    employees = models.ManyToManyField("NewEmployee")
    user_name = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ['full_name']
        verbose_name = 'Работник HR службы'
        verbose_name_plural = 'Работники HR службы'


class Boss(Profile):
    subordinates = models.ManyToManyField("NewEmployee")
    user_name = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ['full_name']
        verbose_name = 'Начальник отдела'
        verbose_name_plural = 'Начальники отдела'


class NewEmployee(Profile):
    achievement = models.CharField(max_length=200, verbose_name='Достижения', blank=True)
    rank = models.IntegerField(default=100, verbose_name="Ранг", blank=True)
    point = models.IntegerField(default=0, verbose_name='Очки', blank=True)
    user_name = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ['full_name']
        verbose_name = 'Новый сотрудник'
        verbose_name_plural = 'Новые сотрудники'

