# Generated by Django 3.1 on 2022-02-12 12:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import shortuuid.django_fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('disciplines', '0002_auto_20220212_1258'),
        ('departments', '0004_auto_20220212_1258'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('groups', '0004_auto_20220212_1258'),
    ]

    operations = [
        migrations.CreateModel(
            name='Timetable',
            fields=[
                ('id', shortuuid.django_fields.ShortUUIDField(alphabet=None, editable=False, length=10, max_length=10, prefix='', primary_key=True, serialize=False, unique=True)),
                ('date', models.DateTimeField()),
                ('department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Department', to='departments.department', verbose_name='Кафедра')),
                ('discipline', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Discipline', to='disciplines.discipline', verbose_name='Дисциплина')),
                ('group', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Group', to='groups.group', verbose_name='Группа')),
                ('teacher', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Profile', to=settings.AUTH_USER_MODEL, verbose_name='Преподаватель')),
            ],
            options={
                'verbose_name': 'Расписание',
                'verbose_name_plural': 'Расписание',
            },
        ),
    ]