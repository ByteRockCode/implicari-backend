# Generated by Django 2.1.7 on 2019-02-27 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_post_is_sent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='is_sent',
            field=models.BooleanField(default=False),
        ),
    ]
