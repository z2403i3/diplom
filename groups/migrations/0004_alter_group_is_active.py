# Generated by Django 3.2 on 2022-04-10 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0003_group_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Активно'),
        ),
    ]