# Generated by Django 3.0.3 on 2020-03-04 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0012_auto_20200304_1922'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='level',
            field=models.CharField(choices=[('bt', 'Budjet'), ('kt', 'Kantrakt'), (' ', 'Boshqa')], default=' ', max_length=2, verbose_name="Ta'lim turi"),
        ),
    ]