# WebAI
- Đầu tiên cài môi trường:
pip -m venv env

- Sau đó cài các gói cần thiết, lưu ý không cần cài 2 môi trường cho từng server nên chỉ cần cài phần requirements.txt của ModelAI là đủ.
Bởi vì trong đó có django + restframework + tensorflow.

pip install requirements.txt

- Bật môi trường:

.\env\Scripts\activate

- Chạy Server API:

python .\ModelAPI\manage.py runserver

- Chạy Server WEB:

python .\AI_Django_Course\manage.py runserver
