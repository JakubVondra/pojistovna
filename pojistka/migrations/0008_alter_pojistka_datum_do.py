# Generated by Django 4.2.7 on 2023-12-01 17:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pojistka', '0007_pojistka_uzivatele_alter_pojistka_datum_do'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pojistka',
            name='datum_do',
            field=models.DateField(default=datetime.datetime(2023, 12, 8, 17, 45, 23, 432956, tzinfo=datetime.timezone.utc), verbose_name='Platnost do'),
        ),
    ]