from django.forms import ModelForm

from Home.models import Holder

class UploadFileForm(ModelForm):
    class Meta:
        model=Holder
        fields =['imageOrigin', 'imageBackground']