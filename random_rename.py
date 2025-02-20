import os
import random
import string
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
import logging

# -------------------------------
# Helper Functions
# -------------------------------

def generate_random_string(length=10):
    """Generate a random alphanumeric string of the given length."""
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for _ in range(length))

def rename_files_in_folder(folder_path, length=10, logger=None):
    """
    Rename all files in folder_path using random names of specified length.
    Avoids name collisions by checking if a file with the new name exists.
    Logs the renaming process via the provided logger.
    """
    try:
        files = os.listdir(folder_path)
    except Exception as e:
        if logger:
            logger.error("Error accessing folder '%s': %s", folder_path, e)
        return

    for file_name in files:
        old_file_path = os.path.join(folder_path, file_name)
        if os.path.isfile(old_file_path):
            file_extension = os.path.splitext(file_name)[1]
            new_file_name = generate_random_string(length) + file_extension
            new_file_path = os.path.join(folder_path, new_file_name)

            # Ensure no collision exists
            while os.path.exists(new_file_path):
                new_file_name = generate_random_string(length) + file_extension
                new_file_path = os.path.join(folder_path, new_file_name)

            try:
                os.rename(old_file_path, new_file_path)
                if logger:
                    logger.info('Renamed: %s -> %s', old_file_path, new_file_path)
            except Exception as e:
                if logger:
                    logger.error("Failed to rename '%s': %s", old_file_path, e)

# -------------------------------
# Logging Handler for the GUI
# -------------------------------

class TextHandler(logging.Handler):
    """This class allows you to log to a Tkinter Text or ScrolledText widget."""
    def __init__(self, text_widget):
        super().__init__()
        self.text_widget = text_widget

    def emit(self, record):
        msg = self.format(record)
        self.text_widget.configure(state='normal')
        self.text_widget.insert(tk.END, msg + '\n')
        self.text_widget.configure(state='disabled')
        self.text_widget.yview(tk.END)

# -------------------------------
# GUI Application
# -------------------------------

class RenameGUI:
    def __init__(self, master):
        self.master = master
        master.title("Random File Renamer")
        master.geometry("600x400")
        master.resizable(False, False)

        # Folder selection frame
        self.folder_frame = tk.Frame(master)
        self.folder_frame.pack(pady=10, padx=10, fill=tk.X)

        self.folder_label = tk.Label(self.folder_frame, text="Folder:")
        self.folder_label.pack(side=tk.LEFT)

        self.folder_entry = tk.Entry(self.folder_frame, width=50)
        self.folder_entry.pack(side=tk.LEFT, padx=5)

        self.browse_button = tk.Button(self.folder_frame, text="Browse", command=self.browse_folder)
        self.browse_button.pack(side=tk.LEFT)

        # Random string length frame
        self.length_frame = tk.Frame(master)
        self.length_frame.pack(pady=5, padx=10, fill=tk.X)

        self.length_label = tk.Label(self.length_frame, text="Random String Length:")
        self.length_label.pack(side=tk.LEFT)

        self.length_entry = tk.Entry(self.length_frame, width=5)
        self.length_entry.insert(0, "10")
        self.length_entry.pack(side=tk.LEFT, padx=5)

        # Action buttons
        self.action_frame = tk.Frame(master)
        self.action_frame.pack(pady=10)

        self.rename_button = tk.Button(self.action_frame, text="Rename Files", command=self.rename_files)
        self.rename_button.pack(side=tk.LEFT, padx=5)

        self.exit_button = tk.Button(self.action_frame, text="Exit", command=master.quit)
        self.exit_button.pack(side=tk.LEFT, padx=5)

        # Log output area
        self.log_text = scrolledtext.ScrolledText(master, state='disabled', width=70, height=15)
        self.log_text.pack(pady=10, padx=10)

        # Set up logging to output to the text widget
        self.logger = logging.getLogger("RenameLogger")
        self.logger.setLevel(logging.INFO)
        text_handler = TextHandler(self.log_text)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        text_handler.setFormatter(formatter)
        self.logger.addHandler(text_handler)

    def browse_folder(self):
        folder_selected = filedialog.askdirectory()
        if folder_selected:
            self.folder_entry.delete(0, tk.END)
            self.folder_entry.insert(0, folder_selected)

    def rename_files(self):
        folder = self.folder_entry.get().strip()
        if not folder:
            messagebox.showerror("Error", "Please select a folder.")
            return

        if not os.path.isdir(folder):
            messagebox.showerror("Error", "The selected folder does not exist.")
            return

        try:
            length = int(self.length_entry.get().strip())
        except ValueError:
            messagebox.showerror("Error", "Random string length must be an integer.")
            return

        confirm = messagebox.askyesno("Confirm Rename", 
            f"Are you sure you want to rename all files in:\n{folder}\nwith random names of length {length}?")
        if not confirm:
            return

        self.logger.info("Starting renaming process in folder: %s", folder)
        rename_files_in_folder(folder, length, self.logger)
        self.logger.info("Renaming process complete.")

def main():
    root = tk.Tk()
    app = RenameGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
