# Generated by Django 4.2.17 on 2024-12-19 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='old_cart',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
