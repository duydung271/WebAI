
from django.shortcuts import redirect, render
from .forms import LinkImageForm, UploadFileForm
from .models import Holder
import os
from django.template import loader
from django.http import HttpResponse
from .call_api import predict, request_img
from django.urls import reverse

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

def background(request):
    context={}
    html_template = loader.get_template('background.html')
    return HttpResponse(html_template.render(context, request))

def homeView2(request):
    item = Holder.objects.last()
    form= LinkImageForm(request.POST or None)
    if form.is_valid():
        url_imgO= form.cleaned_data['linkImgO']
        url_imgB= form.cleaned_data['linkImgB']

        file1 =request_img(url_imgO, "imgOrigin.jpg")
        file2 = request_img(url_imgB, "imgbg.jpg")
        if (file1 != "Wrong"):
            item.imageOrigin.name=file1
        if (file2 !="Wrong"):
            item.imageBackground.name=file2
        item.save()
    base64_image = predict(item.imageOrigin.name, item.imageBackground.name)
    context ={'form': form,'item': item, 'base64_image': base64_image}
    html_template = loader.get_template('home2.html')
    return HttpResponse(html_template.render(context, request))