from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator


# class Manager(models.Model):
#     name = models.CharField(max_length=100, verbose_name='Имя Менеджера')
#
#     def __str__(self):
#         return self.name
#
#
# class Executor(models.Model):
#     name = models.CharField(max_length=100, verbose_name='Взял в работу')
#
#     def __str__(self):
#         return self.name


class JobList(models.Model):
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Принято')
    time_in_work = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Готово')
    STATUS = (
        ('o', 'Открыт'),
        ('g', 'Готов'),
        ('p', 'Закрыт'),
    )
    status = models.CharField(max_length=1, choices=STATUS, default='o', verbose_name='Статус')
    manager = models.ManyToManyField(User, related_name='manager', verbose_name='Менеджер')
    executor = models.ManyToManyField(User, related_name='executor', blank=True, null=False, verbose_name='Исполнитель')
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Цена')
    name = models.CharField(max_length=150, verbose_name='Имя')
    surname = models.CharField(max_length=150, verbose_name='Фамилия')
    patronymic = models.CharField(max_length=150, blank=True, null=False, verbose_name='Отчество')
    phone_regex = RegexValidator(regex=r"^\+?1?\d{8,15}$")
    phone = models.CharField(validators=[phone_regex], max_length=13, verbose_name='Номер телефона')
    email = models.EmailField(blank=True, null=False, verbose_name='Электронная почта')
    address = models.CharField(max_length=250, blank=True, null=False, verbose_name='Адрес')
    comment = models.CharField(max_length=250, verbose_name='Причина обращения')
    appearance = models.CharField(max_length=100, verbose_name='Внешний вид')
    DEVICE = (
        (None, 'Выберите тип устройства'),
        ('s', 'Смартфон'),
        ('n', 'Ноутбук'),
        ('m', 'Мобильный телефон'),
    )
    device = models.CharField(max_length=1, choices=DEVICE, blank=True, verbose_name='Устройство')
    imei_sn = models.CharField(max_length=50, blank=True, null=False, verbose_name='Имэй или серийный номер')
    brand = models.CharField(max_length=50, verbose_name='Брэнд')
    model = models.CharField(max_length=50, verbose_name='Модель')
    equipment = models.CharField(max_length=150, verbose_name='Комплектация')
    password = models.CharField(max_length=50, blank=True, null=False, verbose_name='Пароль')
    estimated_price = models.CharField(max_length=8, blank=True, null=False, verbose_name='Ориентировочная цена')

    class Meta:
        ordering = ['-published']

    def __str__(self):
        return self.surname
