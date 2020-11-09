# Generated by Django 3.0.4 on 2020-10-14 18:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Purchase_product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=64)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('address', models.TextField(max_length=128)),
                ('contact_no', models.IntegerField(default=91, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Product_detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_quantity', models.IntegerField(default=0)),
                ('product_price', models.FloatField(default=0.0)),
                ('product_gst', models.FloatField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modifies_at', models.DateTimeField(auto_now=True)),
                ('purchase_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Product_detail', to='inventory__webapp.Purchase_product')),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Product_detail', to='inventory__webapp.Supplier')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]