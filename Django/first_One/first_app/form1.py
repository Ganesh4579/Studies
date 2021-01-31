from django import forms

class exform(forms.Form):
    Name=forms.CharField(label='name',max_length=100,widget=forms.TextInput)
    Des=forms.CharField(label='des',max_length=300,widget=forms.Textarea)