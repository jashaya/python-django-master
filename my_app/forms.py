from django import forms
from . models import Student
from . models import Registration
class studentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields=['name','address']

class signupForm(forms.Form):
    name=forms.CharField(widget=forms.TextInput(attrs={'pattern':'[a-zA-Z]'}))
    lastname=forms.CharField(widget=forms.TextInput(attrs={'pattern':'[a-zA-Z]'}))
    address=forms.CharField(widget=forms.Textarea(attrs={'pattern':'[a-zA-Z]'}))
    choice= [
        ('1', 'India'),
        ('2','Pakistan'),
        ('3', 'China'),
    ]
    country = forms.CharField(label='country', widget=forms.Select(choices=choice))

    username=forms.CharField(widget=forms.TextInput(attrs={'pattern':'[a-zA-Z]'}))

    password=forms.CharField(widget=forms.PasswordInput(attrs={'pattern':'[a-zA-Z]'}))
    confirmpassword=forms.CharField(widget=forms.PasswordInput(attrs={'pattern':'[a-zA-Z]'}))
    terms=forms.BooleanField()
    def clean_name(self):
        name=self.cleaned_data['name']
        if name.isupper():
            raise forms.ValidationError("please don't use uppercase")
        return name
    def clean_lastname(self):
        lname=self.cleaned_data['lastname']
        if lname.isupper():
            raise forms.ValidationError("please don't use uppercase")
        return lname
    def clean_address(self):
        add=self.cleaned_data['address']
        if add.isupper():
            raise  forms.ValidationError("please don't use uppercase")
        return add
    def clean_confirmpassword(self):
        password = self.cleaned_data['password']
        cpassword=self.cleaned_data['confirmpassword']
        if not password == cpassword:
            raise forms.ValidationError("passowrd $ confirmpw are not equal")
        return cpassword
class userForm(forms.Form):
    username=forms.CharField(max_length=20)
    photo=forms.FileField()
class emailForm(forms.Form):
    subject=forms.CharField(max_length=20)
    message=forms.CharField(max_length=20)
    to=forms.CharField(max_length=20)
    photo = forms.FileField()
    lastname=forms.CharField(max_length=20)