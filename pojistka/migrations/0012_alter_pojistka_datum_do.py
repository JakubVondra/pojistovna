# Generated by Django 4.2.7 on 2023-12-01 18:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pojistka', '0011_alter_pojistka_datum_do'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pojistka',
            name='datum_do',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Platnost do'),
        ),
    ]
