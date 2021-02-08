from django.db import models

# Create your models here.

class employee(models.Model):
    emp_ID=models.IntegerField()
    emp_name=models.CharField(max_length=10)
    
    def __str__(self):
        return self.emp_name
    

class branch(models.Model):
    emp_ID=models.ForeignKey(employee, on_delete=models.CASCADE, blank=True, null=True)
    branch_name=models.CharField(max_length=20)
    
    def __str__(self):
        return str(self.pk)