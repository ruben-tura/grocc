# Generated by Django 4.1.7 on 2024-03-24 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='additional_notes',
            field=models.CharField(default='notes', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='entry',
            name='club',
            field=models.CharField(default='cesena', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='entry',
            name='discounted_price',
            field=models.DecimalField(decimal_places=2, default=15.0, max_digits=7),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='entry',
            name='first_name',
            field=models.CharField(default='Lorenzo', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='entry',
            name='last_name',
            field=models.CharField(default='Rocca', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='entry',
            name='size',
            field=models.CharField(default='M', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='entry',
            name='total_price',
            field=models.DecimalField(decimal_places=2, default=20.0, max_digits=7),
            preserve_default=False,
        ),
    ]
