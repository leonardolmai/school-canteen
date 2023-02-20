# Generated by Django 4.1.3 on 2023-01-18 13:46

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product_Sale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(verbose_name='quantidade')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_method', models.CharField(choices=[('Cartão de crédito', 'Cartão de crédito'), ('Cartão de débito', 'Cartão de débito'), ('Dinheiro', 'Dinheiro'), ('PIX', 'PIX')], max_length=20, verbose_name='método de pagamento')),
                ('total', models.FloatField(default=0)),
                ('datetime', models.DateTimeField(default=django.utils.timezone.now)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clients.client')),
                ('products', models.ManyToManyField(through='sales.Product_Sale', to='products.product')),
            ],
        ),
        migrations.AddField(
            model_name='product_sale',
            name='sale',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sales.sale'),
        ),
        migrations.AlterUniqueTogether(
            name='product_sale',
            unique_together={('sale', 'product')},
        ),
    ]
