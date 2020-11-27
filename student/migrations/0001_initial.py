# Generated by Django 3.0.3 on 2020-03-03 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name', models.CharField(max_length=100)),
                ('l_name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('level', models.CharField(max_length=10, null=True)),
                ('comment', models.TextField(blank=True)),
                ('published_time', models.DateField(auto_now_add=True)),
                ('updated_time', models.DateField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Student',
                'verbose_name_plural': 'Students',
            },
        ),
    ]
