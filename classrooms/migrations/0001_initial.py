# Generated by Django 2.1 on 2018-08-16 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Classroom',
            fields=[
                (
                    'id',
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                ('name', models.CharField(max_length=255, verbose_name='nombre')),
                ('is_archived', models.BooleanField(default=False, verbose_name='is archived')),
                (
                    'creation_timestamp',
                    models.DateTimeField(
                        auto_now_add=True,
                        verbose_name='creation timestamp',
                    ),
                ),
                (
                    'update_timestamp',
                    models.DateTimeField(
                        auto_now=True,
                        verbose_name='update timestamp',
                    ),
                ),
            ],
            options={
                'verbose_name_plural': 'classrooms',
            },
        ),
    ]
