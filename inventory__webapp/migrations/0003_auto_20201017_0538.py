# Generated by Django 3.0.4 on 2020-10-17 05:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory__webapp', '0002_stock'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stock',
            old_name='quatity',
            new_name='quantity',
        ),
    ]
