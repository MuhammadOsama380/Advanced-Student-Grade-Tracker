# 🎓 Advanced Student Grade Tracker

**Author:** Muhammad Osama  
**Course:** Python Programming (Fanshawe College)  
**LinkedIn:** [muhammad-osama-872328202](https://www.linkedin.com/in/muhammad-osama-872328202)  
**GitHub:** [MuhammadOsama380](https://github.com/MuhammadOsama380)

## 📖 Project Overview
The Advanced Student Grade Tracker is a **Python-based command-line application** that manages student academic records.  
It allows users to **add, update, and visualize** student performance while automatically calculating GPAs and saving data persistently using JSON.

## 🧠 Features
✅ Add and update student profiles  
✅ Auto-calculate GPA (0.0–4.0 scale)  
✅ Visualize grade distribution using Matplotlib  
✅ Rank students by GPA  
✅ Save and load data with JSON persistence  
✅ Simple menu-driven interface  


## 🧩 Data Example
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
  }
}



---

### 5️⃣ **Code Features / Core Functions**
Explain what your key functions do — this helps professors and recruiters understand your coding logic.

```markdown
## ⚙️ Core Functions
- `load_data()` → Loads existing student records from JSON  
- `save_data()` → Saves updated records to disk  
- `add_student()` → Adds new student info and scores  
- `update_scores()` → Updates course marks  
- `calculate_gpa()` → Computes GPA for each student  
- `rank_students()` → Lists students in GPA order  
- `plot_grade_distribution()` → Displays grade histogram  


## 🚀 How to Run
```bash
# Clone this repository
git clone https://github.com/MuhammadOsama380/Advanced-Student-Grade-Tracker.git
cd Advanced-Student-Grade-Tracker

# Install dependencies
pip install -r requirements.txt

# Run the program
python src/Muhammad_Osama_Project_Code.py



---

### 7️⃣ **Example Output**
Show what happens when you run it.

```markdown
## 💻 Example Output
=== Advanced Student Grade Tracker ===  
1. Add New Student  
2. Update Student Scores  
3. Calculate All GPAs  
4. Show Grade Distribution  
5. Rank Students  
6. Save and Exit  

**Sample Ranking Output:**
1. Uzair  | GPA: 3.75  
2. Osama  | GPA: 3.13  
3. Sultan | GPA: 2.8


## 🧰 Tools & Libraries
- Python 3.x  
- Matplotlib  
- JSON  


## 🪪 License
This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.
