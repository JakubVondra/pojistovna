# Generated by Django 4.2.7 on 2023-11-29 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pojistka', '0002_uzivatel'),
    ]

    operations = [
        migrations.AddField(
            model_name='uzivatel',
            name='cislo',
            field=models.CharField(default='', max_length=10, verbose_name='Číslo domu'),
        ),
        migrations.AddField(
            model_name='uzivatel',
            name='jmeno',
            field=models.CharField(default='', max_length=100, verbose_name='Jméno'),
        ),
        migrations.AddField(
            model_name='uzivatel',
            name='mesto',
            field=models.CharField(default='', max_length=100, verbose_name='Město'),
        ),
        migrations.AddField(
            model_name='uzivatel',
            name='prijmeni',
            field=models.CharField(default='', max_length=100, verbose_name='Příjmení'),
        ),
        migrations.AddField(
            model_name='uzivatel',
            name='psc',
            field=models.CharField(default='', max_length=10, verbose_name='PSČ'),
        ),
        migrations.AddField(
            model_name='uzivatel',
            name='telefon',
            field=models.CharField(default='', max_length=20, verbose_name='Telefon'),
        ),
        migrations.AddField(
            model_name='uzivatel',
            name='ulice',
            field=models.CharField(default='', max_length=100, verbose_name='Ulice'),
        ),
    ]
