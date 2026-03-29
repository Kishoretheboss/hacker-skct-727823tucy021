# 🔍 Social Media OSINT Tracker

## 📌 Project Description

This project is a simple **Open Source Intelligence (OSINT) tool** that collects publicly available information from social media platforms (GitHub).
It allows users to enter a username and retrieve details like followers and repository count.

---

## 🎯 Objective

* To understand OSINT concepts
* To build a basic data collection tool using Python
* To demonstrate automation using a pipeline

---

## ⚙️ Tools & Technologies Used

* Python 3
* Kali Linux
* Git
* GitHub
* requests library

---

## 🚀 How to Run the Tool

1. Open terminal in project folder
2. Run the command:

```
python3 tool_main.py
```

3. Enter a GitHub username
4. View the output

---

## 🧪 Test Cases

| Test Case | Input            | Expected Output |
| --------- | ---------------- | --------------- |
| 1         | torvalds         | Valid user data |
| 2         | octocat          | Valid user data |
| 3         | randomuser123xyz | User not found  |

---

## ⚙️ Pipeline Execution

Run the following commands:

```
python3 setup_lab.py
python3 run_tool.py
python3 analyze_results.py
```

---

## 📂 Project Structure

```
SKCT_727823tucy021_SocialMediaOSINT/
│
├── tool_main.py
├── setup_lab.py
├── run_tool.py
├── analyze_results.py
├── pipeline_727823tucy021.yml
├── screenshots/
├── logs/
└── README.md
```

---

## ⚠️ Errors Faced

**Error:**

```
ModuleNotFoundError: No module named 'requests'
```

**Solution:**

```
pip3 install requests
```

---

## 📊 Output

The tool successfully fetches:

* Username
* Followers
* Public repositories

---

## 👨‍💻 Author

* Roll No: 727823tucy021

---

## 📅 Date

2026-03-29
