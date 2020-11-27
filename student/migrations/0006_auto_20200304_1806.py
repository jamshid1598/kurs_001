# Generated by Django 3.0.3 on 2020-03-04 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0005_auto_20200304_1803'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='comment',
            field=models.TextField(blank=True, null=True, verbose_name='Talaba haqida'),
        ),
        migrations.AlterField(
            model_name='student',
            name='f_name',
            field=models.CharField(max_length=100, verbose_name='Ismi'),
        ),
        migrations.AlterField(
            model_name='student',
            name='l_name',
            field=models.CharField(max_length=100, verbose_name='Familyasi'),
        ),
        migrations.AlterField(
            model_name='student',
            name='level',
            field=models.CharField(choices=[('bt', 'Budjet'), ('kt', 'Kantrakt')], default='bt', max_length=2, verbose_name="Ta'lim turi"),
        ),
    ]
