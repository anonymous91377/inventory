# Generated by Django 3.0.4 on 2020-10-19 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory__webapp', '0004_purchase_return'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supplier',
            name='contact_no',
            field=models.IntegerField(default=91),
        ),
    ]