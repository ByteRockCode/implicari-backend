# Generated by Django 2.1.7 on 2019-03-07 03:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_auto_20190227_0550'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('-creation_timestamp',)},
        ),
    ]
