import requests
import json

# token = input("Please enter your Canvas token here: ")
token = ""

print("Fetching grades...")

def fetch(url):
    res = requests.get(f'https://canvas.instructure.com/api/v1' + url, headers={"Authorization": f"Bearer {token}"}).text
    return json.loads(res)

courses = fetch("/courses")
enrollments = []

for course in courses:
    enrollment = fetch(f'/courses/{course["id"]}/enrollments')

    enrollments.append(enrollment)

for enrollment in enrollments:
    print(enrollment)
    print(enrollment["grades"]["current_grade"])