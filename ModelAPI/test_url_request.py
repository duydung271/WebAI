import requests
import base64
code_dict ={}

with open('C:/Users/ace02/Desktop/Something/anh.jpg', 'rb') as binary_file:
    binary_file_data = binary_file.read()
    base64_encoded_data = base64.b64encode(binary_file_data)
    base64_message = base64_encoded_data.decode('utf-8')
    code_dict["origin"]=base64_message

with open('C:/Users/ace02/Desktop/Something/debai.png', 'rb') as binary_file:
    binary_file_data = binary_file.read()
    base64_encoded_data = base64.b64encode(binary_file_data)
    base64_message = base64_encoded_data.decode('utf-8')
    code_dict["background"]=base64_message

response = requests.post("http://127.0.0.1:8080/api/predict/", data=code_dict)
print(response.text)