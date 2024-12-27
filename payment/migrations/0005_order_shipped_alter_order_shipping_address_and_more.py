# Generated by Django 4.2.17 on 2024-12-26 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0004_shippingaddress_shipping_state'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='shipped',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='order',
            name='shipping_address',
            field=models.TextField(max_length=15000),
        ),
        migrations.AlterField(
            model_name='shippingaddress',
            name='shipping_address',
            field=models.CharField(max_length=15000),
        ),
    ]
