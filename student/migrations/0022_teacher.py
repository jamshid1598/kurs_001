# Generated by Django 3.0.3 on 2020-03-07 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0021_auto_20200305_1221'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name', models.CharField(max_length=250)),
                ('l_name', models.CharField(max_length=250)),
            ],
        ),
    ]
