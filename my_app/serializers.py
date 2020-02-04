from rest_framework import serializers
from . models import *
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        fields=('student_id','name','address')
        model=Student