import base64
base64_img=""

with open('C:/Users/ace02/Desktop/Something/debai.png', 'rb') as binary_file:
    binary_file_data = binary_file.read()
    base64_encoded_data = base64.b64encode(binary_file_data)
    base64_message = base64_encoded_data.decode('utf-8')
    base64_img=base64_message
    print("Ok")


base64_img_bytes = base64_img.encode('utf-8')
with open('decoded_image.png', 'wb') as file_to_save:
    decoded_image_data = base64.decodebytes(base64_img_bytes)
    file_to_save.write(decoded_image_data)

#https://stackabuse.com/encoding-and-decoding-base64-strings-in-python/