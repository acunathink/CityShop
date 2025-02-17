# Generated by Django 4.2.14 on 2024-07-20 23:20

import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_city_options_alter_shop_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shops', to='api.city', verbose_name='Город'),
        ),
        migrations.AlterField(
            model_name='shop',
            name='close_time',
            field=models.TimeField(default=datetime.time(0, 0), verbose_name='Время закрытия'),
        ),
        migrations.AlterField(
            model_name='shop',
            name='house',
            field=models.SmallIntegerField(validators=[django.core.validators.MinValueValidator(1)], verbose_name='Дом'),
        ),
        migrations.AlterField(
            model_name='shop',
            name='name',
            field=models.CharField(max_length=64, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='shop',
            name='open_time',
            field=models.TimeField(default=datetime.time(0, 0), verbose_name='Время открытия'),
        ),
        migrations.AlterField(
            model_name='shop',
            name='street',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shops', to='api.street', verbose_name='Улица'),
        ),
        migrations.AlterField(
            model_name='street',
            name='name',
            field=models.CharField(max_length=64, verbose_name='Улица'),
        ),
    ]
