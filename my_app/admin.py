from django.contrib import admin
from . models import Student
from . models import Registration
from . models import User
admin.site.register(Student)
admin.site.register(Registration)
admin.site.register(User)
# Register your models here.
