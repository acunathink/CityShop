# Generated by Django 4.2.14 on 2024-07-20 17:29

import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='city',
            options={'verbose_name': 'Город', 'verbose_name_plural': 'Города'},
        ),
        migrations.AlterModelOptions(
            name='shop',
            options={'verbose_name': 'Магазин', 'verbose_name_plural': 'Магазины'},
        ),
        migrations.AlterModelOptions(
            name='street',
            options={'verbose_name': 'Улица', 'verbose_name_plural': 'Улицы'},
        ),
        migrations.AddField(
            model_name='shop',
            name='close_time',
            field=models.TimeField(default=datetime.time(0, 0)),
        ),
        migrations.AddField(
            model_name='shop',
            name='house',
            field=models.SmallIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1)]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='shop',
            name='open_time',
            field=models.TimeField(default=datetime.time(0, 0)),
        ),
        migrations.AlterField(
            model_name='street',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='streets', to='api.city', verbose_name='Город'),
        ),
    ]
