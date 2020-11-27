# Generated by Django 3.0.3 on 2020-03-07 16:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0026_teacher_program_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='teacher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='student_name', to='student.Teacher'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='program_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='teacher_name', to='student.ProgrammingLanguage'),
        ),
    ]