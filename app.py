# from flask import Flask, request, jsonify
# from flask_restful import Resource, Api
import os
import numpy as np
# import base64
import pytesseract
from PIL import Image
# import re
# import requests
# import json
# import datetime
# app = Flask(__name__)

# ROOT_PREFIX = '/' + os.path.dirname(os.path.realpath(__file__)).rsplit('\\', 1)[-1]

# def save_image(data):
#     # print("SAVING THE IMAGE FILE")
#     fh = open("C:\\inetpub\\wwwroot\\TCIL_OCR\\Doc\\org_image.jpg", "wb")
#     decstr = base64.b64decode(data['image_bytes'])
#     fh.write(decstr)
#     fh.close()
#     return 

# # saving logs for future
# def save_history(data):
#     # print("SAVING COPY OF THE IMAGE FILE")
#     system_datetime = datetime.datetime.now()
#     str1 = str(system_datetime)
#     str2 = str1.replace(" ", "_")
#     str3 = str2.replace(".","_")
#     str4 = str3.replace(":","_")
#     log_filename = 'history/'+'Image_'+str4+'.jpg'
#     fh1 = open(log_filename, "wb")
#     decstr = base64.b64decode(data['image_bytes'])
#     fh1.write(decstr)
#     fh1.close()
#     return 
    
def get_text():
    print("EXTRACTING THE TEXT FROM THE IMAGE")
    pytesseract.tesseract_cmd = r"Tesseract-OCR\tesseract.exe"
    tessaract_config = ('-l eng --oem 1 --psm 3') #Page Segmentation Mode (psm) 

    img = Image.open("sample_image.png")
    text = pytesseract.image_to_string(img, config=tessaract_config)
    return text
    # tmp_text = text.split('\n')
    # tmp_text_new = [i for i in tmp_text if i]
    # print("*********************************************************************")
    # print(tmp_text_new)
    # text manipulation

 
# def log_file(logdata):
#     system_datetime = datetime.datetime.now()
#     str1 = str(system_datetime)
#     str2 = str1.replace(" ", "_")
#     str3 = str2.replace(".","_")
#     str4 = str3.replace(":","_")
#     log_filename = 'history/'+'log_'+ str4 +'.txt'
#     file = open(log_filename, 'a')
#     file.write(logdata)
#     file.write("\n")
#     return

# @app.route(ROOT_PREFIX+'/image_rec',methods=['POST'])
# def flask_func():
#     data = request.get_json(force=True)
#     # # print("START")
#     save_image(data)
    
#     save_history(data)
    
#     try:
#         image_text = get_text(data)

#         # print("reached main file image text function")
#         output = {'image_text' : image_text,
#         'status': 'Valid',}
#         log_file(str(output))
#         return jsonify(output)
#     except Exception as e:
#         error = str(e)
#         output = {'status': 'Invalid',
#         'image_text' : error,
#         } #"Please scan again.
#         log_file(str(output))
#         return jsonify(output)
#     output = {'status': "valid",
#         'image_text' :data["image_bytes"],
#         } #"Please scan again.
        
#     return jsonify(output)
        
if __name__ == "__main__":
    text = get_text()