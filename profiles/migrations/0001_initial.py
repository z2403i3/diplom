# Generated by Django 3.1 on 2022-01-29 13:56

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import shortuuid.django_fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('id', shortuuid.django_fields.ShortUUIDField(alphabet=None, editable=False, length=10, max_length=10, prefix='', primary_key=True, serialize=False, unique=True)),
                ('full_name', models.CharField(max_length=150, verbose_name='ФИО')),
                ('first_name', models.CharField(max_length=50, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=50, verbose_name='Фамилия')),
                ('gender', models.CharField(choices=[('male', 'Мужской'), ('female', 'Женский'), ('none', 'Не указан')], default='none', max_length=10, verbose_name='Пол')),
                ('birth_date', models.DateField(blank=True, null=True, verbose_name='Дата рождения')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Почта')),
                ('phone_number', models.CharField(max_length=50, verbose_name='Номер телефона')),
                ('address', models.CharField(max_length=100, verbose_name='Адрес')),
                ('photo', models.ImageField(blank=True, upload_to='users/', verbose_name='Фотография')),
                ('user_type', models.CharField(blank=True, choices=[('student', 'Студент'), ('teacher', 'Преподаватель'), ('none', 'Не указано')], default='none', max_length=10, null=True, verbose_name='Тип пользователя')),
                ('group_number', models.CharField(blank=True, max_length=20, null=True, verbose_name='Номер группы')),
                ('course_number', models.CharField(blank=True, max_length=10, null=True, verbose_name='Номер курса')),
                ('headman', models.BooleanField(blank=True, default=False, null=True, verbose_name='Староста')),
                ('phone_number_parents', models.CharField(blank=True, max_length=50, null=True, verbose_name='Контактный телефон родителей')),
                ('educ_type', models.CharField(blank=True, choices=[('full_time', 'Очная'), ('part_time', 'Заочная'), ('none', 'Не указано')], default='none', max_length=10, null=True, verbose_name='Форма обучения')),
                ('position', models.CharField(blank=True, max_length=50, null=True, verbose_name='Должность')),
                ('qualification', models.CharField(blank=True, max_length=50, null=True, verbose_name='Квалификация')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('teacher', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Профиль',
                'verbose_name_plural': 'Профили',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
