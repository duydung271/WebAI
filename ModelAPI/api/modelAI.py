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
