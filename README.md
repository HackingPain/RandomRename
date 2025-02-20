# Random File Renamer with GUI

This Python script provides a graphical interface to randomly rename files in a selected folder. It generates unique random alphanumeric strings (with a customizable length) for renaming while preserving the original file extensions. The script also displays log messages during the renaming process.

---

## Features

- **Graphical User Interface:**  
  - Uses Tkinter to let you select a folder and specify the random string length.
  - Provides real-time log output in a scrolled text widget.

- **Randomized File Naming:**  
  - Generates a random alphanumeric string for each file.
  - Preserves the original file extension.

- **Collision Prevention:**  
  - Checks for existing filenames to avoid collisions.

- **Error Handling:**  
  - Validates folder paths and input values.
  - Displays error messages for common issues.

---

## Requirements

- **Python 3.x**
- **Tkinter:** Bundled with most Python installations on Windows.
- Standard Python libraries: `os`, `random`, `string`, `tkinter`, `logging`

---

## Installation and Setup

1. **Install Python 3.x:**  
   Download and install Python from [python.org](https://www.python.org/downloads/).

2. **Verify Tkinter:**  
   Tkinter is usually included with your Python installation. If not, refer to your operating system’s documentation.

3. **Download the Script:**  
   Clone or download the `random_rename.py` file to your computer.

---

## Usage

1. **Run the Script:**
   - Open a command prompt or terminal.
   - Navigate to the directory containing `random_rename.py`.
   - Run the script:
     ```bash
     python random_rename.py
     ```

2. **Using the GUI:**
   - **Select Folder:** Click the **Browse** button to choose the folder with files you want to rename.
   - **Set Random String Length:** Change the default length (10) if desired.
   - **Rename Files:** Click the **Rename Files** button to start the process.  
     - The log area will display messages about each file renamed.
   - **Exit:** Click the **Exit** button to close the application.

---

## Improvements and Notes

- **Error Handling:**  
  The script includes error handling to manage issues like invalid folder paths and renaming errors.

- **Collision Checking:**  
  It checks for existing filenames to ensure each new name is unique.

- **Logging:**  
  Uses Python’s `logging` module to report progress, which is helpful for debugging and tracking operations.

---

## References

Python Software Foundation. (n.d.). *Tkinter — Python interface to Tcl/Tk*. Retrieved from https://docs.python.org/3/library/tkinter.html

Python Software Foundation. (n.d.). *logging — Logging facility for Python*. Retrieved from https://docs.python.org/3/library/logging.html

Python Software Foundation. (n.d.). *random — Generate pseudo-random numbers*. Retrieved from https://docs.python.org/3/library/random.html
