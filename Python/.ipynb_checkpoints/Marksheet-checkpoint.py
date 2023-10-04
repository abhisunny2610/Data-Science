import json
import random

# open the file
file = open("Person data.json")

# load the file
data = json.load(file)

# getting user as a student from the file
student = data["users"]

subjects = ["Hindi", "English", "Math", "Science", "Social Science"]

# First we extract the user
# only required first we take
def extract_student(student, keys= ["firstName", "lastName", "age", "email"]):
    student_data = {}

    for key in keys:
        student_data[key] = student.get(key, "")

    student_data["marks"] = {subject:random.randint(30, 100)  for subject in subjects}

    return student_data

extract_student(student[0])


    