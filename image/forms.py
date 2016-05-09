import django.forms as forms

class PictureForm(forms.Form):
    imageFile = forms.ImageField()
