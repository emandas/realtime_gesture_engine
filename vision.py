import base64
import cv2
import numpy as np

def base64_2image_decoder(*,base64str):
    base64str = base64str.split(",")[1]
    array = np.frombuffer(base64.b64decode(base64str),dtype=np.uint8)
    img = cv2.imdecode(array,cv2.IMREAD_COLOR)
    return img


