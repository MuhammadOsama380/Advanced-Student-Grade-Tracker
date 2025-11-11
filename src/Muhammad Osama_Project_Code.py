import json
import os
import matplotlib.pyplot as plt

# Load student records from a JSON file, or return empty dict if none exists
def load_data(filename):
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            return json.load(f)
    return {}

# Save student records to a JSON file

def save_data(records, filename):
    with open(filename, 'w') as f:
        json.dump(records, f, indent=4)
    print(f"Data saved to {filename}.")

# Generate a unique student ID based on existing records
def generate_id(records):
    if records:
        existing_ids = [int(i) for i in records.keys()]
        return str(max(existing_ids) + 1)
    return '1'

# Add a new student with ID, name, courses, scores, attendance, remarks
def add_student(records):
    sid = generate_id(records)
    name = input("Enter student name: ")
    records[sid] = {
        'Name': name,
        'Courses': {},  # course: score
        'Attendance': None,
        'Remarks': None,
        'GPA': None
    }
    # Enter courses and scores
    while True:
        course = input("Enter course name (or press Enter to stop): ")
        if not course:
            break
        score = float(input(f"Enter score for {course}: "))
        records[sid]['Courses'][course] = score
    # Enter attendance and remarks
    attendance = input("Enter attendance percentage (e.g., 85%): ")
    records[sid]['Attendance'] = attendance
    remarks = input("Enter any remarks: ")
    records[sid]['Remarks'] = remarks
    print(f"Added student {name} with ID {sid}.")

# Update an existing student's scores

def update_scores(records):
    sid = input("Enter student ID to update: ")
    if sid not in records:
        print("Student not found.")
        return
    while True:
        course = input("Enter course to update (or press Enter to stop): ")
        if not course:
            break
        score = float(input(f"Enter new score for {course}: "))
        records[sid]['Courses'][course] = score
    print(f"Updated scores for student ID {sid}.")

# Calculate GPA for each student (average score divided by 25 to scale to 4.0)
def calculate_gpa(records):
    for sid, rec in records.items():
        scores = list(rec['Courses'].values())
        if scores:
            avg_score = sum(scores) / len(scores)
            gpa = round(avg_score / 25, 2)
            rec['GPA'] = gpa
            print(f"ID {sid} | {rec['Name']} | GPA: {gpa}")
        else:
            print(f"ID {sid} | {rec['Name']} has no scores.")

# Plot grade distribution across all students

def plot_grade_distribution(records):
    all_scores = []
    for rec in records.values():
        all_scores.extend(rec['Courses'].values())
    if not all_scores:
        print("No scores available to plot.")
        return
    plt.figure()
    plt.hist(all_scores, bins=10)
    plt.title("Grade Distribution")
    plt.xlabel("Scores")
    plt.ylabel("Frequency")
    plt.show()

# Rank students by GPA in descending order
def rank_students(records):
    # ensure GPAs are up-to-date
    calculate_gpa(records)
    ranked = sorted(records.items(), key=lambda x: x[1].get('GPA', 0), reverse=True)
    print("\nStudent Rankings by GPA:")
    for idx, (sid, rec) in enumerate(ranked, start=1):
        print(f"{idx}. ID {sid} | {rec['Name']} | GPA: {rec.get('GPA')}")

# Main program loop

def main():
    filename = 'advanced_grades.json'
    records = load_data(filename)

    while True:
        print("\n=== Advanced Student Grade Tracker ===")
        print("1. Add New Student")
        print("2. Update Student Scores")
        print("3. Calculate All GPAs")
        print("4. Show Grade Distribution")
        print("5. Rank Students")
        print("6. Save and Exit")
        choice = input("Select an option: ")

        if choice == '1':
            add_student(records)
        elif choice == '2':
            update_scores(records)
        elif choice == '3':
            calculate_gpa(records)
        elif choice == '4':
            plot_grade_distribution(records)
        elif choice == '5':
            rank_students(records)
        elif choice == '6':
            save_data(records, filename)
            break
        else:
            print("Invalid option, please try again.")

if __name__ == '__main__':
    main()
