from django.shortcuts import render
from .forms import UploadFileForm
from .models import Holder
import os
from django.template import loader
from django.http import HttpResponse
from .call_api import predict


def homeView(request):
    object_list = Holder.objects.all()

    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            #Delete all database with image media
            for item in object_list:
                if os.path.exists(item.imageOrigin.path):
                    os.remove(item.imageOrigin.path)
                else:
                    print("The file Origin does not exist")
                if os.path.exists(item.imageBackground.path):
                    os.remove(item.imageBackground.path)
                else:
                    print("The file Background does not exist")
            object_list.delete()
            form.save()  
            object_list = Holder.objects.all()
    else:
        form = UploadFileForm()

    data_pre = Holder.objects.get(id=Holder.objects.last().id)
    base64_image = predict(data_pre.imageOrigin.name, data_pre.imageBackground.name)
    context ={'form': form,'object_list': object_list, 'base64_image': base64_image}
    html_template = loader.get_template('home.html')
    return HttpResponse(html_template.render(context, request))