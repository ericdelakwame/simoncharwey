# Generated by Django 3.2.23 on 2024-01-02 13:08

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', ckeditor.fields.RichTextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'About Entry',
                'verbose_name_plural': 'About Entries',
            },
        ),
        migrations.CreateModel(
            name='Press',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('feature', models.CharField(max_length=100)),
                ('reference', models.CharField(max_length=100)),
                ('link', models.URLField()),
            ],
            options={
                'verbose_name': 'Press',
                'verbose_name_plural': 'Press Entries',
            },
        ),
        migrations.CreateModel(
            name='Teaching',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', ckeditor.fields.RichTextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Teaching',
                'verbose_name_plural': 'Teaching',
            },
        ),
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', ckeditor.fields.RichTextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Work',
                'verbose_name_plural': 'Works',
            },
        ),
    ]
