from django import forms

class getval1(forms.Form):
    ID = forms.CharField(label='Employee ID :',max_length=4,widget=forms.TextInput)
    name = forms.CharField(label='Employee Name :',max_length=10,widget=forms.TextInput)
    branch_name = forms.CharField(label='Employee Branch :',max_length=100,widget=forms.TextInput)