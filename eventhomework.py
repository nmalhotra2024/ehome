import tkinter as tk
from tkinter import messagebox

def convert():
    try:
        inches = float(entry.get())
        centimeters = inches * 2.54
        result_label.config(text=f"{centimeters:.2f} cm")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number.")

# Create main window
root = tk.Tk()
root.title("Inches to Centimeters Converter")
root.geometry("350x150")

# Input label and entry box
label = tk.Label(root, text="Enter length in inches:")
label.pack(pady=5)

entry = tk.Entry(root)
entry.pack(pady=5)

# Convert button
convert_btn = tk.Button(root, text="Convert", command=convert)
convert_btn.pack(pady=5)

# Result label
result_label = tk.Label(root, text="Result will appear here")
result_label.pack(pady=5)

# Run the application
root.mainloop()
