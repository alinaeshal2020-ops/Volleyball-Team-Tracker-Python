A Python-based Graphical User Interface (GUI) application designed to track and manage player statistics for a volleyball team. This project was created for my Digital Technologies Advanced Programming assessment.

## 📝 Project Overview
This program allows a team manager to easily record player performance, store data permanently, and automatically calculate end-of-season awards. It uses **Tkinter** for the visual dashboard and **Matplotlib** to generate visual PDF reports.

## Features
*   **Team Management:** Add, search, view, and delete players from the roster.
*   **Data Persistence:** Player data is automatically saved to and loaded from a `players.txt` file using Python file handling (`.strip()` and `.split()`).
*   **Algorithm Design:** Automatically calculates the **Best Attacker** (most spikes), **Best Defender** (most blocks), and **Team MVP** (highest combined stats) using `for` loops and conditional logic.
*   **Input Validation:** Prevents program crashes by checking for empty inputs, blocking commas (which would break the text file format), and ensuring stats are entered as integers using `try/except` blocks.
*   **PDF Generation:** Uses `matplotlib` to generate a downloadable bar chart of the team's overall performance.

## 🗂️ Project Structure (Modular Programming)
The code is split into manageable, modular files to separate the visual interface from the background algorithms:
*   `main.py`: Contains the Tkinter GUI, layout formatting (using Frames), and button commands. **(Run this file to start the app)**.
*   `team_manager.py`: Contains all the background logic, algorithms, list manipulation, and file reading/writing.
*   `players.txt`: The text file acting as the database to store player information permanently.
*   `Team_Report.pdf`: Generated automatically when the user clicks "Generate PDF Graph".

## How to Run the Program

**1. Prerequisites**
Python comes with Tkinter pre-installed, but you will need to install Matplotlib to generate the PDF reports. Open your terminal or command prompt and run:
```bash
pip install matplotlib
2. Running the App
Open the project folder in your IDE (like Visual Studio Code) and run main.py:
code
Bash
python main.py
(Make sure you run main.py and not team_manager.py, as the manager file only contains the background functions!)

Concepts Demonstrated (Assessment Criteria)
Computational Thinking: Breaking down a sports management system into inputs, algorithms, and outputs.
Data Structures: Utilizing 2D lists to hold player stats in memory while the program runs.
Decision Making: Complex if/elif/else structures for user validation and error handling.
Iteration: Using for loops to search for specific players, delete records, and calculate highest scores.
Modular Programming: Using def functions across multiple Python files to keep code clean and readable.

Technologies Used
Python 3 (Core Logic & File Handling)
Tkinter (Standard GUI Library)
Matplotlib (Data Visualization & PDF Export)
Created for the Year 10/12 Digital Technologies Advanced Programming Project.
