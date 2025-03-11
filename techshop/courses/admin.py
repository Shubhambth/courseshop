from django.contrib import admin
from .models import Course , Lesson , Enrollment

admin.site.register(Course)
admin.site.register(Enrollment)
admin.site.register(Lesson)

# Register your models here.
