import base64
import os
from django.conf import settings
import numpy as np
import cv2

INPUT_SHAPE = 256
OUTPUT_SHAPE = 256
# Create your views here.
def predict_image(origin_image_path, background_image_path):
    img_origin = cv2.imread(origin_image_path)
    shape_origin = img_origin.shape

    img = cv2.resize(img_origin, (INPUT_SHAPE, INPUT_SHAPE), cv2.INTER_LINEAR)
    img = img/255.
    img_expand = img[np.newaxis, ...]
    img_pred = settings.MODEL.predict(img_expand).reshape(OUTPUT_SHAPE, OUTPUT_SHAPE,2)

    
    img_pred[img_pred < 0.5] = 0
    img_pred[img_pred >= 0.5] = 1
    img_pred_resize=cv2.resize(img_pred, (shape_origin[1],shape_origin[0]), interpolation = cv2.INTER_LINEAR)


    img_background = cv2.imread(background_image_path)
    img_background = cv2.resize(img_background, (shape_origin[1], shape_origin[0]), cv2.INTER_LINEAR)


    img_name = 'pre'+origin_image_path.split('\\')[-1]
    img_cut = np.empty(shape_origin,dtype=int)
    for i in range(0,3):
        img_cut[:,:,i] = np.multiply(img_origin[:,:,i],img_pred_resize[:,:,0])+ np.multiply(img_background[:,:,i],img_pred_resize[:,:,1])
    cv2.imwrite(os.path.join(settings.MEDIA_ROOT,img_name), img_cut)
    return img_name


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
