# WebAI

Một con app dùng để tách background người và thay background mới!

Kết quả thu được:

+ Viết web cơ bản bằng Django.

+ Viết API cơ bản bằng rest_API.

+ Áp dụng Model AI vào một bài toán thực tế. Cụ thể là Unet với bài toán segmentation.

+ Biết qua về Html, Css, Js cơ bản.

Các vấn đề còn tồn tại:

+ Chưa tối ưu, khi chạy rất tốn CPU và RAM

+ GUI trông còn rối mắt và chưa được hợp lý

Demo
- Cấu trúc WEB

![cautruc](https://github.com/duydung271/WebAI/blob/main/demo/Cautruc.png)


- Chức năng POST ảnh lên server và nhận response là một ảnh đã được thay background

![demo1](https://github.com/duydung271/WebAI/blob/main/demo/demo1.png)

![demo2](https://github.com/duydung271/WebAI/blob/main/demo/demo2.png)

- Chức năng request ảnh từ một address image và nhận response là một ảnh đã được thay background

![demo3](https://github.com/duydung271/WebAI/blob/main/demo/demo3.png)

![demo4](https://github.com/duydung271/WebAI/blob/main/demo/demo4.png)

Cài đặt và chạy theo từng bước:

- Đầu tiên cài môi trường:  **pip -m venv env**

- Bật môi trường: **.\env\Scripts\activate**

- Sau đó cài các gói cần thiết: **pip install - r .\requirements.txt**

- Chạy Server API:  **python .\ModelAPI\manage.py runserver**

- Chạy Server WEB:  **python .\AI_Django_Course\manage.py runserver**
