from django.db import models
from shortuuid.django_fields import ShortUUIDField

from utils.model_utils import generate_id


class Timetable(models.Model):

    NOT_SPECIFIED = 'none'
    PARA = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
    )
    VISITTYPE = (
        ('remote', 'Удаленная'),
        ('locale', 'Очная'),
    )
    DISCTYPE = (
        ('lecture', 'Лекция'),
        ('practice', 'Практика'),
        ('laboratory_work', 'Лабораторная работа'),
        ('course_work', 'Курсовая работа'),
        ('diplom_work', 'Дипломная работа'),
        ('assessment', 'Зачет'),
        ('assessment_with_score', 'Зачет с оценкой'),
        ('exam', 'Экзамен'),
    )

    para = models.CharField(
        'Пара', max_length=10, choices=PARA, default=NOT_SPECIFIED
    )

    visit = models.CharField(
        'Тип пары', max_length=10, choices=VISITTYPE, default=NOT_SPECIFIED
    )

    type = models.CharField(
        'Тип занятий', max_length=30, choices=DISCTYPE, default=NOT_SPECIFIED
    )

    id = ShortUUIDField(
        primary_key=True, length=10, unique=True, default=generate_id, editable=False
    )
    date = models.DateField('Дата')
    discipline = models.ForeignKey('disciplines.Discipline', related_name='Discipline', verbose_name='Дисциплина',
                                   on_delete=models.CASCADE, blank=True,
                                   null=True, to_field='id')
    teacher = models.ForeignKey('profiles.Profile', related_name='Profile', verbose_name='Преподаватель',
                                on_delete=models.CASCADE, blank=True,
                                null=True, to_field='id')
    department = models.ForeignKey('departments.Department', related_name='Department', verbose_name='Кафедра',
                                   on_delete=models.CASCADE, blank=True,
                                   null=True, to_field='id')
    group = models.ForeignKey('groups.Group', related_name='Group', verbose_name='Группа',
                              on_delete=models.CASCADE, blank=True,
                              null=True, to_field='id')
    description = models.TextField(verbose_name='Описание', null=True, blank=True)
    session = models.BooleanField('Сессия', default=False)
    is_active = models.BooleanField('Активно', default=True)

    def delete(self):
        self.is_active = False
        self.save()

    def __str__(self):
        return self.id

    class Meta:
        verbose_name = "Расписание"
        verbose_name_plural = "Расписание"
