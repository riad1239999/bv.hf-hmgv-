import tkinter as tk
from tkinter import simpledialog

def save_password():
    # Create the main window
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    # Ask for password input
    password = simpledialog.askstring("Password Input", 
                                    "Enter a Password (not your real password):", 
                                    show='*')

    if password:  # If user entered something and didn't cancel
        # Save to file
        with open("passlist.txt", "a") as f:  # 'a' for append mode
            f.write(password + "\n")
        print("Password saved to passlist.txt")
    else:
        print("No password entered.")

if __name__ == "__main__":
    save_password()