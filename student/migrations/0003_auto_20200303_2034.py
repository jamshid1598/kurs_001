# Generated by Django 3.0.3 on 2020-03-03 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_auto_20200303_2027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='comment',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='level',
            field=models.CharField(default='kantrakt', max_length=10),
            preserve_default=False,
        ),
    ]
