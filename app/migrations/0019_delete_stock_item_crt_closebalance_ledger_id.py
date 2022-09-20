# Generated by Django 4.0.5 on 2022-09-17 07:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_closebalance'),
    ]

    operations = [
        migrations.DeleteModel(
            name='stock_item_crt',
        ),
        migrations.AddField(
            model_name='closebalance',
            name='ledger_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.ledger'),
        ),
    ]
