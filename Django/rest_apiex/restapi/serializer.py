from rest_framework import serializers
from .models import employee

'''class empser(serializers.Serializer):
    emp_ID=serializers.IntegerField()
    emp_name=serializers.CharField(max_length=10)
    
    
    def create(self, validated_data):
        return employee.create(validated_data)
    
    def update(self, instance, validated_data):
        instance.emp_ID = validated_data.get('emp_ID',instance.emp_ID)
        instance.emp_name = validated_data.get('emp_name',instance.emp_name)
        instance.save()
        return instance'''
        
        
class empser(serializers.ModelSerializer):
    class Meta:
        model = employee
        fields='__all__'