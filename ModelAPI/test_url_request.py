import requests
# file_dict ={}
# with open("C:/Users/ace02/Desktop/Something/test.jpg", "rb") as origin:
#     file_dict["imageOrigin"] = origin
#     with open("C:/Users/ace02/Desktop/Something/alo.jpg", "rb") as background:
#         file_dict["imageBackground"]= background
#         response = requests.post("http://127.0.0.1:8080/api/upload/", files=file_dict)
#         print(response.text)

# https://stackoverflow.com/questions/22567306/how-to-upload-file-with-python-requests
# https://stackoverflow.com/questions/30229231/python-save-image-from-url


pic_url = 'http://127.0.0.1:8080/api/image_predict'
with open('pic1.jpg', 'wb') as handle:
    response = requests.get(pic_url, stream=True)
    if not response.ok:
        print(response)
    else:
        for block in response.iter_content(1024):
            if not block:
                break
            handle.write(block)