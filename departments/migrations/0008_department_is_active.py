# Generated by Django 3.2 on 2022-04-10 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('departments', '0007_department_gallery'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Активно'),
        ),
    ]
