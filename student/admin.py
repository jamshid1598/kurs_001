from django.contrib import admin
from .models import Student, Teacher, ProgrammingLanguage
from django.db import models
from tinymce.widgets import TinyMCE

# Register your models here.

class StudentAdmin(admin.ModelAdmin):
	list_display = [
		'f_name',
		'l_name',
		'age',
		'level',
		'year_in_school',
		'published_time',
		'updated_time',
		'teacher',
		'student_language',
		'Program_Language'
	]

	def student_language(self, languages):
		return languages.teacher.program_name.program_name
	student_language.short_description="Dasturlash Tili"

	def Program_Language(self, program):
		is_true=False
		if program.teacher.program_name.id==4:
			is_true=True
		return is_true
	Program_Language.short_description="Django"
	Program_Language.boolean=True

	list_display_links = [
		'f_name',
		'l_name',
		'age',
		'level',
		'year_in_school',
		'published_time',
		'updated_time',
	]

	search_fields=[
		'f_name',
		'l_name',
		'age',
		'level',
		'year_in_school',
	]

	ordering=[
		'f_name',
		'l_name',
		'age',
		'level',
		'year_in_school',
	]

	formsets = (
			('Full Name and Age:', {
				'fields' : [
						'f_name', 'l_name', 'age'
					]
				}
			),
			('Level/Course:', {
				'fields' : [
					'level', 
					'year_in_school'
					]
				}
			),
			('O\'qtuvchi', {'fields' : ['teacher']}),
			('Definition:', {'fields' : ['definition']}),
			('Published and Updated time:',{
				'fields' : [
						'published_time', 
						'updated_time'
					]
				}
			),
			('Comment: ', {'fields' : ['comment']})

		)

	formfield_overrides = {
		models.TextField : {'widget' : TinyMCE}
	}


admin.site.register(ProgrammingLanguage)

admin.site.register(Teacher)
	
admin.site.register(Student, StudentAdmin)