# Generated by Django 3.0.3 on 2020-03-04 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0008_auto_20200304_1851'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='level',
            field=models.CharField(choices=[('bt', 'Budjet'), ('kt', 'Kantrakt'), (None, 'Boshqa')], default='bt', max_length=2, verbose_name="Ta'lim turi"),
        ),
    ]