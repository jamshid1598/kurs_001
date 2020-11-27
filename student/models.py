from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.translation import gettext_lazy as _




# Create your models here.

class ProgrammingLanguage(models.Model):
	program_name=models.CharField(
		max_length=200,
		blank=True,
		null=True
	)

	def __str__(self):
		return self.program_name

class Teacher(models.Model):
	f_name=models.CharField(max_length=250)
	l_name=models.CharField(max_length=250)

	program_name=models.ForeignKey(
		ProgrammingLanguage, 
		on_delete=models.SET_NULL, 
		related_name='programs_name',
		blank=True,
		null=True,
	)


	def __str__(self):
		return f"{self.f_name} {self.l_name}"


class Student(models.Model):
	
	f_name = models.CharField(
		max_length=100, 
		verbose_name='Ismi'
	)
	l_name = models.CharField(
		max_length=100, 
		verbose_name='Familyasi'
	)
	age = models.IntegerField(
		default=1, 
		validators=[
			MaxValueValidator(100),
			MinValueValidator(1)
		],
		verbose_name='Yoshi',	
	 )

	# choices for student level

	""" educ type choices choices with 'choices' """

	# BUDJET = 'bt'
	# KANTRAKT = 'kt'
	# LevelChoices = [
	# 	(BUDJET, 'Budjet'),
	# 	(KANTRAKT, 'Kantrakt'),
	# 	(" ", 'Boshqa')
	# ]
	
	# level = models.CharField(
	# 		max_length=2,
	# 		choices=LevelChoices,
	# 		default=" ",
	# 		verbose_name='Ta\'lim turi'
	# 	)
	
	""" educ type choices with Enumeration types """

	class LevelChoices(models.TextChoices):
		BUDJET = 'BT', _('Budjet')
		KANTRAKT = 'KT', _('Kantrakt')
		__empty__ = _('(Aniqmas)')

	level = models.CharField(
			max_length=2,
			choices=LevelChoices.choices,
			default=LevelChoices.__empty__,
			verbose_name='Ta\'lim turi'
		)

	# end choices

	teacher=models.ForeignKey(
		Teacher, 
		# on_delete=models.CASCADE, 
		on_delete=models.SET_NULL,
		blank=True, 
		null=True,
		related_name='teacher_name',
	)

	# choices for 'year in school'

	class YearInSchool(models.IntegerChoices):
		FRESHMAN = 1, _('I')
		SOPHOMORE = 2, _('II')
		JUNIOR = 3, _('III')
		GRADUATE = 4, _('IV')
		__empty__ = _('(Aniqmas)')

	year_in_school = models.IntegerField(
		choices = YearInSchool.choices, 
		default = YearInSchool.__empty__,
		verbose_name = 'Kursi',
	)

	# end choices

	definition = models.TextField(
			blank=True, 
			null=True, 
			verbose_name='Talaba haqida'
		)
	published_time = models.DateField(auto_now_add=True)
	updated_time = models.DateField(auto_now=True)
	comment = models.TextField(
		blank=True, 
		null=True, 
		help_text="Fikr muloazalaringizni yozib qoldiring"
	)

	class Meta:
		verbose_name = 'Student'
		verbose_name_plural='Students'

	def __str__(self):
		return f"Talaba {self.f_name} {self.l_name} {self.level}"

