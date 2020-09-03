from django import forms

class addForm(forms.Form):
    name=forms.CharField(label="name",max_length=30)
    age=forms.FloatField(label='age')
    gender=forms.CharField(label="gender",widget=forms.Select(choices=[('male','male'),('female','female')]))
    aadhar_no=forms.FloatField(label="aadhar_no")




class searchForm(forms.Form):
    name=forms.CharField(label="name",max_length=30)
