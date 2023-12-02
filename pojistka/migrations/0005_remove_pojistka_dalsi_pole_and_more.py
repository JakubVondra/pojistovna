# Generated by Django 4.2.7 on 2023-12-01 13:15

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pojistka', '0004_pojistka'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pojistka',
            name='dalsi_pole',
        ),
        migrations.RemoveField(
            model_name='pojistka',
            name='dalsi_pole2',
        ),
        migrations.AddField(
            model_name='pojistka',
            name='castka',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10, verbose_name='Částka pojistky'),
        ),
        migrations.AddField(
            model_name='pojistka',
            name='datum_do',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 8, 13, 15, 8, 422409, tzinfo=datetime.timezone.utc), verbose_name='Platnost do'),
        ),
        migrations.AddField(
            model_name='pojistka',
            name='datum_od',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Platnost od'),
        ),
        migrations.AddField(
            model_name='pojistka',
            name='konec_cesty',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Konec cesty'),
        ),
        migrations.AddField(
            model_name='pojistka',
            name='predmet_pojisteni',
            field=models.TextField(default='', verbose_name='Předmět pojištění'),
        ),
        migrations.AddField(
            model_name='pojistka',
            name='zacatek_cesty',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Začátek cesty'),
        ),
    ]