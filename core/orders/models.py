from django.db import models
from users.models import User


class Order(models.Model):
    CREATED = 0
    PAID = 1  # НАДО БУДЕТ ДОБАВИТЬ ЛОГИКУ ДЛЯ ЭТОГО С ТГ БОТОМ ОТ ВАДИМА
    ON_WAY = 2
    DELIVERED = 3
    STATUSES = (
        (CREATED, 'Created'),
        (PAID, 'Paid'),
        (ON_WAY, 'On Way'),
        (DELIVERED, 'Delivered')
    )

    first_name = models.CharField('First Name', max_length=25)
    last_name = models.CharField('Last Name', max_length=40)
    email = models.EmailField('Email', max_length=256)
    country = models.CharField('Country', max_length=40)
    city = models.CharField('City', max_length=40)
    address = models.CharField('Address', max_length=60)
    basket_history = models.JSONField('Basket History', default=dict)
    created = models.DateTimeField('Created Time', auto_now_add=True)
    status = models.SmallIntegerField('Status', default=CREATED, choices=STATUSES)
    customer = models.ForeignKey(User, verbose_name='Customer', on_delete=models.CASCADE)

    def __str__(self):
        return f'Order #{self.id}. {self.first_name} {self.last_name}.Status order {self.status}'

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'
        db_table = 'Order'
