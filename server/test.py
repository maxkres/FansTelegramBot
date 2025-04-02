import requests


def get_all_students():
    url = "http://127.0.0.1:8000/students"
    response = requests.get(url)
    return response.json()


def get_students_with_param_requests(course: int):
    url = "http://127.0.0.1:8000/students"
    response = requests.get(url, params={"course": course})
    return response.json()


def get_students_with_param_path(course: int):
    url = f"http://127.0.0.1:8000/students/{course}"
    response = requests.get(url)
    return response.json()

def get_student_by_id(id: int):
    url = "http://127.0.0.1:8000/students"
    response = requests.get(url, params={"id": id})
    return response.json()


student = get_student_by_id(3)
print(student)
