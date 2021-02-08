from rest_framework import serializers
from . import models

class employee_ser(serializers.Serializer):
    emp_ID=serializers.IntegerField()
    emp_name=serializers.CharField(max_length=10)
    
    
    def create(self,vdata):
        return models.employee.objects.create(data)
    
    def update(self,ins,vdata):
        ins.emp_ID=data.get('emp_ID',ins.emp_ID)
        ins.emp_name=data.get('emp_name',ins.emp_name)
        ins.save()
        return ins