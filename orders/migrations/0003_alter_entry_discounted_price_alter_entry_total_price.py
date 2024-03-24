# Generated by Django 4.1.7 on 2024-03-24 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_entry_additional_notes_entry_club_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='discounted_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=7),
        ),
        migrations.AlterField(
            model_name='entry',
            name='total_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=7),
        ),
    ]
