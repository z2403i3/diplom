# Generated by Django 3.1 on 2022-01-31 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('departments', '0019_auto_20220131_2210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='id',
            field=models.CharField(default='6bcc652d5e', max_length=10, primary_key=True, serialize=False, unique=True),
        ),
    ]