from django.shortcuts import render, HttpResponse
from .models import Course


def course_list_view(request):
    all_courses = Course.objects.all()
    data = {"courses": all_courses}
    return render(request, context=data, template_name='index.html')
