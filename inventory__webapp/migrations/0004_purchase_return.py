# Generated by Django 3.0.4 on 2020-10-19 06:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory__webapp', '0003_auto_20201017_0538'),
    ]

    operations = [
        migrations.CreateModel(
            name='Purchase_return',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
                ('price', models.FloatField(default=0.0)),
                ('gst', models.FloatField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('Supplier', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='purchase_return', to='inventory__webapp.Supplier')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='purchase_return', to='inventory__webapp.Purchase_product')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]
