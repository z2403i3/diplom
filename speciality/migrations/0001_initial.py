# Generated by Django 3.2 on 2022-04-13 17:03

from django.db import migrations, models
import django.db.models.deletion
import utils.model_utils


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('departments', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Speciality',
            fields=[
                ('id', models.CharField(default=utils.model_utils.generate_id, max_length=10, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=150, verbose_name='имя специальность')),
                ('remote_education_time', models.CharField(max_length=150, verbose_name='Время обучения удалённо')),
                ('locale_education_time', models.CharField(max_length=150, verbose_name='Время обучения очно')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активно')),
                ('department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='departments.department', verbose_name='Кафедра')),
            ],
            options={
                'verbose_name': 'Специальность',
                'verbose_name_plural': 'Специальности',
            },
        ),
    ]
