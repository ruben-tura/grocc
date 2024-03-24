# Generated by Django 4.1.7 on 2024-03-24 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_alter_entry_discounted_price_alter_entry_total_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='discounted_price',
            field=models.DecimalField(blank=True, decimal_places=2, default='', max_digits=7),
        ),
        migrations.AlterField(
            model_name='entry',
            name='total_price',
            field=models.DecimalField(blank=True, decimal_places=2, default='', max_digits=7),
        ),
    ]
