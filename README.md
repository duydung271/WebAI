# WebAI
- Đầu tiên cài môi trường:  **pip -m venv env**

- Bật môi trường: **.\env\Scripts\activate**

- Sau đó cài các gói cần thiết, lưu ý không cần cài 2 môi trường cho từng server nên chỉ cần cài phần requirements.txt của ModelAPI là đủ.
Bởi vì trong đó có django + restframework + tensorflow: **pip install - r .\ModelAPI\requirements.txt**

- Chạy Server API:  python **python .\ModelAPI\manage.py runserver**

- Chạy Server WEB:  python **python .\AI_Django_Course\manage.py runserver**
