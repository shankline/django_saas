# Generated by Django 3.1 on 2020-10-17 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('membership', '0011_auto_20201017_1047'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='business',
            name='reference_no',
        ),
        migrations.AddField(
            model_name='payment',
            name='reference_no',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
