import requests
from django.conf import settings
import os

API_PORT ="http://127.0.0.1:8080/api/"
def predict(origin_name, background_name):
    file_dict ={}
    with open(os.path.join(settings.MEDIA_ROOT,origin_name), "rb") as origin:
        file_dict["imageOrigin"] = origin
        with open(os.path.join(settings.MEDIA_ROOT,background_name), "rb") as background:
            file_dict["imageBackground"]= background
            response = requests.post(API_PORT+"upload/", files=file_dict)
            print(response.text)

# https://stackoverflow.com/questions/22567306/how-to-upload-file-with-python-requests
# https://stackoverflow.com/questions/30229231/python-save-image-from-url


    pic_url = API_PORT+'image_predict/'
    new_pic_name = origin_name.split('.')[0]+background_name.split('.')[0]+'.jpg'

    with open(os.path.join(settings.MEDIA_ROOT,new_pic_name), 'wb') as handle:
        response = requests.get(pic_url, stream=True)
        if not response.ok:
            print(response)
        else:
            for block in response.iter_content(1024):
                if not block:
                    break
                handle.write(block)
    return new_pic_name