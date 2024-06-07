import json
from datetime import datetime

def load_data():
    try:
        with open("attendance_data.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_data(data):
    with open("attendance_data.json", "w") as file:
        json.dump(data, file)

def mark_attendance(student_id):
    data = load_data()
    current_date = datetime.now().strftime("%Y-%m-%d")
    if current_date not in data:
        data[current_date] = []
    if student_id not in data[current_date]:
        data[current_date].append(student_id)
        save_data(data)
        print(f"Attendance marked for student with ID {student_id} on {current_date}.")
    else:
        print(f"Attendance already marked for student with ID {student_id} on {current_date}.")

def view_attendance(date=None):
    data = load_data()
    if date:
        if date in data:
            print(f"Attendance for {date}:")
            for student_id in data[date]:
                print(f"- Student ID: {student_id}")
        else:
            print(f"No attendance data available for {date}.")
    else:
        for date, students in data.items():
            print(f"Attendance for {date}:")
            for student_id in students:
                print(f"- Student ID: {student_id}")

def main():
    print("University Attendance App")
    while True:
        print("\n1. Mark Attendance\n2. View Attendance\n3. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            student_id = input("Enter student ID: ")
            mark_attendance(student_id)
        elif choice == "2":
            date = input("Enter date (YYYY-MM-DD) to view attendance (Press Enter for today's attendance): ")
            view_attendance(date)
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
