# Generated by Django 3.1 on 2020-10-15 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('membership', '0003_auto_20201015_2212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='phone',
            field=models.CharField(help_text='example. 255700000000', max_length=12, verbose_name='Enter your M-PESA mobile number'),
        ),
    ]
