import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("firebaseAccount.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://smartattendence-44e72-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

data = {
    "321654":
        {
            "name": "Saviru Bandara",
            "major": "SE",
            "starting_year": 2014,
            "total_attendance": 1,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2023-05-22 00:54:34"
        },
    "852741":
        {
            "name": "Emly Blunt",
            "major": "Economics",
            "starting_year": 2021,
            "total_attendance": 12,
            "standing": "B",
            "year": 1,
            "last_attendance_time": "2023-05-22 00:54:34"
        },
    "963852":
        {
            "name": "Elon Musk",
            "major": "Physics",
            "starting_year": 2020,
            "total_attendance": 7,
            "standing": "G",
            "year": 2,
            "last_attendance_time": "2023-05-22 00:54:34"
        }
}

for key, value in data.items():
    ref.child(key).set(value)