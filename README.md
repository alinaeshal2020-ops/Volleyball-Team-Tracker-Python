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

## ⚙️ How to Run the Program

### Step 1: Open the Project

- Download or clone this repository to your computer.
- Open the entire project folder inside **Visual Studio Code** (or your preferred Python IDE).

### Step 2: Install Matplotlib (Required for the PDF Report)

This program generates a downloadable PDF graph and requires the **Matplotlib** library.

1. Open a new terminal in VS Code:
   - Select **Terminal → New Terminal** from the top menu.
2. Copy and paste the following command into the terminal and press **Enter**:

```bash
pip install matplotlib
```

> **Note:** Depending on your Python setup, you may need to use:
>
> ```bash
> python -m pip install matplotlib
> ```

### Step 3: Launch the Application

1. Open the `main.py` file in your editor.
2. Click the **Run Python File** (▶) button in the top-right corner of Visual Studio Code.

> ⚠️ **Important:** Make sure you are running `main.py` and **not** `team_manager.py`.
>
> The `team_manager.py` file only contains the backend algorithms and data management logic. Running it directly will **not** launch the visual dashboard.

Created for the Year 10 Coding Programming Project.
