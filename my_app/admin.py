from django.contrib import admin
from . models import Student
from . models import Registration
from . models import User
from . models import Post
# Register your models here.

admin.site.register(Post)
admin.site.register(Student)
admin.site.register(Registration)
admin.site.register(User)
# Register your models here.
