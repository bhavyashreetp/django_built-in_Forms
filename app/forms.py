from django import forms


def validate_for_a(svalue):
    if svalue[0].lower()=='a':
        raise forms.ValidationError('invalid data')

def validate_for_len(name):
    if len(name)<=5:
        raise forms.ValidationError('invalid data')


class StudentForm(forms.Form):
    sname=forms.CharField(max_length=100,validators=[validate_for_a,validate_for_len])
    sage=forms.IntegerField()
    email=forms.EmailField(validators=[validate_for_a])
    
