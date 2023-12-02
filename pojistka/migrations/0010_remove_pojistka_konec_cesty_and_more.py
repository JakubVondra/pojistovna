# Generated by Django 4.2.7 on 2023-12-01 17:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pojistka', '0009_alter_pojistka_datum_do_alter_pojistka_uzivatele'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pojistka',
            name='konec_cesty',
        ),
        migrations.RemoveField(
            model_name='pojistka',
            name='zacatek_cesty',
        ),
        migrations.AlterField(
            model_name='pojistka',
            name='datum_do',
            field=models.DateField(default=datetime.datetime(2023, 12, 8, 17, 50, 3, 517525, tzinfo=datetime.timezone.utc), verbose_name='Platnost do'),
        ),
    ]
