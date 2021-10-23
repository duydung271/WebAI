from django.forms import ModelForm
from django import forms
from Home.models import Holder
from django.template.defaultfilters import mark_safe

class UploadFileForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['imageOrigin'].label=mark_safe('<strong style="color:#51b340">Image Origin</strong>')
        self.fields['imageBackground'].label=mark_safe('<strong style="color:#4085b3">Image Origin</strong>')

    class Meta:
        model=Holder
        fields =['imageOrigin', 'imageBackground']


class LinkImageForm(forms.Form):
    linkImgO = forms.CharField(label=mark_safe('<strong style="color:#51b340">Image Origin</strong>'),max_length=1000, required=False)
    linkImgB = forms.CharField(label=mark_safe('<strong style="color:#4085b3">Image Background</strong>'),max_length=1000, required=False)
    