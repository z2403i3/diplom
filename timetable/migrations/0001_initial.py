# Generated by Django 3.2 on 2022-04-13 17:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import shortuuid.django_fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('groups', '0001_initial'),
        ('departments', '0001_initial'),
        ('disciplines', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Timetable',
            fields=[
                ('para', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8')], default='none', max_length=10, verbose_name='Пара')),
                ('visit', models.CharField(choices=[('remote', 'Удаленная'), ('locale', 'Очная')], default='none', max_length=10, verbose_name='Тип пары')),
                ('type', models.CharField(choices=[('lecture', 'Лекция'), ('practice', 'Практика'), ('laboratory_work', 'Лабораторная работа'), ('course_work', 'Курсовая работа'), ('diplom_work', 'Дипломная работа'), ('assessment', 'Зачет'), ('assessment_with_score', 'Зачет с оценкой'), ('exam', 'Экзамен')], default='none', max_length=30, verbose_name='Тип занятий')),
                ('id', shortuuid.django_fields.ShortUUIDField(alphabet=None, editable=False, length=10, max_length=10, prefix='', primary_key=True, serialize=False, unique=True)),
                ('date', models.DateField(verbose_name='Дата')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('session', models.BooleanField(default=False, verbose_name='Сессия')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активно')),
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
