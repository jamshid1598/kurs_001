# Generated by Django 3.0.3 on 2020-03-05 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0013_auto_20200304_1926'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='definition',
            field=models.TextField(blank=True, null=True, verbose_name='Talaba haqida'),
        ),
        migrations.AlterField(
            model_name='student',
            name='comment',
            field=models.TextField(blank=True, null=True),
        ),
    ]
