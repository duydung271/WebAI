import json
import requests
from django.conf import settings
import os
import base64

API_PORT ="http://127.0.0.1:8080/api/"

def image_decode(base64_img,img_name):
    base64_img_bytes = base64_img.encode('utf-8')
    with open(os.path.join(settings.MEDIA_ROOT, img_name), 'wb') as file_to_save:
        decoded_image_data = base64.decodebytes(base64_img_bytes)
        file_to_save.write(decoded_image_data)
        return img_name

def image_encode(img_name):
    with open(os.path.join(settings.MEDIA_ROOT, img_name), 'rb') as binary_file:
        binary_file_data = binary_file.read()
        base64_encoded_data = base64.b64encode(binary_file_data)
        base64_message = base64_encoded_data.decode('utf-8')
        return base64_message

def predict(origin_name, background_name):
    code_dict ={}
    with open(os.path.join(settings.MEDIA_ROOT, origin_name), 'rb') as binary_file:
        binary_file_data = binary_file.read()
        base64_encoded_data = base64.b64encode(binary_file_data)
        base64_message = base64_encoded_data.decode('utf-8')
        code_dict["origin"]=base64_message

    with open(os.path.join(settings.MEDIA_ROOT, background_name), 'rb') as binary_file:
        binary_file_data = binary_file.read()
        base64_encoded_data = base64.b64encode(binary_file_data)
        base64_message = base64_encoded_data.decode('utf-8')
        code_dict["background"]=base64_message

    response = requests.post(API_PORT+"predict/", data=code_dict)
    data = response.json()['predict']
    return data

