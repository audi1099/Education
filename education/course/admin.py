import django.contrib.admin
from .models import Course
from .models import Topic

django.contrib.admin.site.register(Course)
django.contrib.admin.site.register(Topic)



