

---



```markdown
# 📋 Student Info Collection Web App

This is a simple **Flask-based web application** that collects user-submitted information via a form and stores it in a CSV file. The app is ideal for learning Flask, handling form data, and basic file operations in Python.

---

## 🧩 Features

- Built using **Flask**
- Collects user inputs:
  - Name
  - Email
  - Phone number
  - College
  - Course
  - Career objective
- Saves all data into `students.csv`
- HTML templates for:
  - Home
  - Form display
  - Submission confirmation

---

## 📁 Project Structure

```

project/
├── main.py              # Flask application
├── students.csv         # Saved form submissions
├── templates/
│   ├── home.html        # Landing page
│   ├── ind.html         # Form page
│   └── submit.html      # Success page
└── README.md

````

---

## 🚀 How to Run

1. Clone this repo:
   ```bash
   git clone https://github.com/Shadinbm/student-info-form.git
   cd student-info-form
````

2. Make sure Flask is installed:

   ```bash
   pip install flask
   ```

3. Run the app:

   ```bash
   python main.py
   ```

4. Open your browser and go to:

   ```
   http://127.0.0.1:5000/
   ```

---

## 🌐 Routes

| Route         | Functionality                                                |
| ------------- | ------------------------------------------------------------ |
| `/`           | Loads `home.html`                                            |
| `/x`          | Loads the form (`ind.html`)                                  |
| `/submitform` | Accepts POST request, saves form data, returns `submit.html` |

---

## 📧 Contact

**Author**: Muhammed Shadin Bm
📬 **Email**: [bmshadin43@gmail.com](mailto:bmshadin43@gmail.com)
🔗 **LinkedIn**: [muhammed-shadin-bm](https://www.linkedin.com/in/muhammed-shadin-bm-23871432b)

---

> 💡 *A beginner-friendly Flask project for learning form handling and server-side storage.*

```


Let me know!
```
