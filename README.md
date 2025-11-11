# Advanced Student Grade Tracker

**Author:** Muhammad Osama  
**Course:** Python Programming (Fanshawe College)  
**Institution:** Fanshawe College  
**LinkedIn:** [muhammad-osama-872328202](https://www.linkedin.com/in/muhammad-osama-872328202)  
**GitHub:** [MuhammadOsama380](https://github.com/MuhammadOsama380)

---

## Project Overview
The **Advanced Student Grade Tracker** is a **Python-based command-line application** designed to manage and analyze student academic records. It allows users to **add, update, and visualize** student performance, automatically calculate GPAs, and store all records persistently using JSON files. This project demonstrates essential programming concepts such as **file handling, data serialization, modularization, dictionary manipulation, control flow, and data visualization with Matplotlib**.

---

## Features
- Add new student records with name, courses, and scores  
- Update or delete existing records  
- Automatically calculate GPA (0.0–4.0 scale)  
- Visualize grade distribution using histograms  
- Rank students by GPA in descending order  
- Save and load data using JSON for persistent storage  
- Simple text-based menu-driven interface  

---

## Data Example
```json
{
  "1": {
    "Name": "Osama",
    "Courses": {
      "Python": 80.0,
      "JavaScript": 75.0,
      "DataScience": 80.0
    },
    "Attendance": "90%",
    "Remarks": "Good",
    "GPA": 3.13
  },
  "2": {
    "Name": "Uzair",
    "Courses": {
      "Python": 90.0,
      "JavaScript": 95.0,
      "DataScience": 96.0
    },
    "Attendance": "85%",
    "Remarks": "Excellent",
    "GPA": 3.75
  }
}
```

---

## Core Functions
| Function | Description |
|-----------|-------------|
| `load_data(filename)` | Loads existing student records from JSON |
| `save_data(records, filename)` | Saves updated data persistently |
| `generate_id(records)` | Generates a unique student ID |
| `add_student(records)` | Adds a new student and their scores |
| `update_scores(records)` | Updates course marks for an existing student |
| `calculate_gpa(records)` | Computes GPA from course averages |
| `plot_grade_distribution(records)` | Displays grade histogram using Matplotlib |
| `rank_students(records)` | Ranks students by GPA in descending order |

---

## Example Output
```
=== Advanced Student Grade Tracker ===
1. Add New Student
2. Update Student Scores
3. Calculate All GPAs
4. Show Grade Distribution
5. Rank Students
6. Save and Exit

Student Rankings by GPA:
1. Uzair  | GPA: 3.75
2. Osama  | GPA: 3.13
3. Sultan | GPA: 2.80
```

---

## Visualization
Matplotlib is used to plot a histogram of student scores to visualize grade distribution. This helps instructors and analysts identify performance patterns and outliers across all students.

---

## How to Run
```bash
# Clone the repository
git clone https://github.com/MuhammadOsama380/Advanced-Student-Grade-Tracker.git
cd Advanced-Student-Grade-Tracker

# Install dependencies
pip install -r requirements.txt

# Run the program
python src/Muhammad_Osama_Project_Code.py
```

---

## Future Enhancements
- Implement error handling and data validation  
- Add CSV/Excel data import and export support  
- Store data using SQLite or MySQL  
- Create a GUI using Tkinter or a web app using Flask  
- Generate automated PDF grade reports  
- Integrate analytics and class performance metrics  
- Include automated testing using pytest  

---

## Tools and Libraries
- **Python 3.x**  
- **Matplotlib** — for grade visualization  
- **JSON** — for data storage  
- **os / sys** — for file operations and menu navigation  

---

## Repository Structure
```
Advanced-Student-Grade-Tracker/
│
├── data/
│   └── advanced_grades.json
│
├── src/
│   └── Muhammad_Osama_Project_Code.py
│
├── reports/
│   └── Muhammad_Osama_Project_Report.pdf
│
├── README.md
├── requirements.txt
├── LICENSE
└── .gitignore
```

---

## License
This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

## Acknowledgements
Developed by **Muhammad Osama** as part of the **Python Programming** course at **Fanshawe College**.  
If you found this project useful, please consider giving it a ⭐ on GitHub or connecting with me on [LinkedIn](https://www.linkedin.com/in/muhammad-osama-872328202).
