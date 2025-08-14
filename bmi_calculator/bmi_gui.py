import tkinter as tk
from tkinter import messagebox

def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())

        if weight <= 0 or height <= 0:
            raise ValueError("Weight and height must be greater than 0.")

        bmi = weight / (height ** 2)

        if bmi < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi < 24.9:
            category = "Normal weight"
        elif 25 <= bmi < 29.9:
            category = "Overweight"
        else:
            category = "Obese"

        result_label.config(text=f"BMI: {bmi:.2f}\nCategory: {category}")

    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numbers.")

root = tk.Tk()
root.title("BMI Calculator")
root.geometry("300x250")
root.resizable(False, False)

tk.Label(root, text="Weight (kg):").pack(pady=5)
weight_entry = tk.Entry(root)
weight_entry.pack()

tk.Label(root, text="Height (m):").pack(pady=5)
height_entry = tk.Entry(root)
height_entry.pack()

tk.Button(root, text="Calculate BMI", command=calculate_bmi).pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack()

root.mainloop()
