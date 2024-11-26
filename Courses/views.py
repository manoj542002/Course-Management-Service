from django.shortcuts import render
from .models import Course

# Create your views here.
def course_list(request):
    offered_courses = Course.objects.all()
    return render(request, 'Courses/course_list.html',{'offered_courses' : offered_courses})


