from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Student
# Create your views here.

def student_info(request):
	return render(
			request=request,
			template_name='student/home.html',
			context={
				'student_info' : Student.objects.all()
			}
		)


