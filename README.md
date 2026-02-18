# 📌 Task Tracker CLI

A simple Command Line Task Tracker built using Python.  
This application helps users manage daily tasks by storing them in a JSON file and tracking their progress using task statuses.

---

## 🚀 Features

➕ Add new tasks  
✏️ Update existing tasks  
❌ Delete tasks  
📋 View all tasks  
✅ Mark tasks as Done  
🔄 Mark tasks as In Progress  
📂 View tasks by status:
  - Todo (Default)
  - In Progress
  - Done

---

## 🛠 Tech Stack

**Language:** Python  
**Type:** CLI (Command Line Interface)  
**Storage:** JSON File  

### Modules Used (Built-in Only)

datetime  
re  
time  
json  

Since only built-in modules are used, no external installation is required.

---

## 🐍 Python Version Requirement

✅ **Minimum Recommended Version:** Python 3.8+  
🧪 **Developed Using:** Python 3.13  

The program should work on most modern Python versions since it only uses built-in modules.

---

## 📂 How It Works

Tasks are stored in a JSON file  
Each task contains:
  - Task description  
  - Status (Todo / In Progress / Done)  
  - Timestamp (Created or Updated)  

Default status when creating a task = **Todo**

---

## ▶️ How To Run

### 1️⃣ Clone or Download Project
bash

git clone <your-repo-url>
cd task-tracker
