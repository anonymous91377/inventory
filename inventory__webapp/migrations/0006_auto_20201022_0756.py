# Generated by Django 3.0.4 on 2020-10-22 07:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory__webapp', '0005_auto_20201019_1427'),
    ]

    operations = [
        migrations.RenameField(
            model_name='purchase_return',
            old_name='Supplier',
            new_name='supplier',
        ),
    ]