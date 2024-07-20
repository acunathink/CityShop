import datetime

from django.core import validators
from django.db import models


class City(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'


class Street(models.Model):
    name = models.CharField(max_length=64, verbose_name='Улица')
    city = models.ForeignKey(City, verbose_name='Город',
                             on_delete=models.CASCADE,
                             related_name='streets')

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Улица'
        verbose_name_plural = 'Улицы'


class Shop(models.Model):
    name = models.CharField(max_length=64, verbose_name='Название')
    city = models.ForeignKey(City, related_name='shops',
                             on_delete=models.CASCADE,
                             verbose_name='Город')
    street = models.ForeignKey(Street, related_name='shops',
                               on_delete=models.CASCADE,
                               verbose_name='Улица')
    house = models.SmallIntegerField(
        null=False,
        verbose_name='Дом',
        validators=[validators.MinValueValidator(1)],
    )
    open_time = models.TimeField(default=datetime.time(minute=0),
                                 verbose_name='Время открытия')
    close_time = models.TimeField(default=datetime.time(minute=0),
                                  verbose_name='Время закрытия')

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Магазин'
        verbose_name_plural = 'Магазины'
