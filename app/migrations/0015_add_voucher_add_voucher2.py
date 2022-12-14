# Generated by Django 4.0.5 on 2022-09-13 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_delete_add_voucher'),
    ]

    operations = [
        migrations.CreateModel(
            name='add_voucher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=225)),
                ('particular', models.CharField(max_length=225)),
                ('voucher_type', models.CharField(max_length=225)),
                ('voucher_number', models.CharField(max_length=225)),
                ('quntity', models.CharField(max_length=225)),
                ('value', models.CharField(max_length=225)),
            ],
        ),
        migrations.CreateModel(
            name='add_voucher2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=225)),
                ('particular', models.CharField(max_length=225)),
                ('voucher_type', models.CharField(max_length=225)),
                ('voucher_number', models.CharField(max_length=225)),
                ('debit', models.CharField(max_length=225)),
                ('credit', models.CharField(max_length=225)),
            ],
        ),
    ]
