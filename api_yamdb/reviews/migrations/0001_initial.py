# Generated by Django 3.0 on 2022-09-01 08:03

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Введите категорию', max_length=256, verbose_name='Категория')),
                ('slug', models.SlugField(help_text='Введите ссылку', unique=True, verbose_name='Ссылка')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Текст комментария')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации комментария')),
            ],
            options={
                'verbose_name': 'Комментарий',
                'verbose_name_plural': 'Комментарии',
                'ordering': ['pub_date'],
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Введите жанр', max_length=200, verbose_name='Жанр')),
                ('slug', models.SlugField(help_text='Введите ссылку', unique=True, verbose_name='Ссылка')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Текст отзыва')),
                ('score', models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(0, 'Оценка 1-10'), django.core.validators.MaxValueValidator(10, 'Оценка 1-10')], verbose_name='Рейтинг')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации отзыва')),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
                'ordering': ['pub_date'],
            },
        ),
        migrations.CreateModel(
            name='Title',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Введите название', max_length=256, verbose_name='Название')),
                ('year', models.PositiveSmallIntegerField(blank=True, help_text='Введите год выпуска', null=True, validators=[django.core.validators.MaxValueValidator(2022)], verbose_name='Год выпуска')),
                ('description', models.TextField(blank=True, help_text='Введите описание', null=True, verbose_name='Описание')),
                ('category', models.ForeignKey(blank=True, help_text='Выберите категорию', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='titles', to='reviews.Category', verbose_name='Категория')),
                ('genre', models.ManyToManyField(blank=True, help_text='Выберите жанр', related_name='titles', to='reviews.Genre', verbose_name='Жанр')),
            ],
        ),
    ]