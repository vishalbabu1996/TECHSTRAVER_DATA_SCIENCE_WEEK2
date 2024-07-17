import tkinter as tk
from tkinter import ttk

# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(event):
    try:
        celsius = float(celsius_entry.get())
        fahrenheit = (celsius * 9/5) + 32
        fahrenheit_var.set(f"{fahrenheit:.2f}")
    except ValueError:
        if celsius_entry.get() == "":
            fahrenheit_var.set("")
        else:
            fahrenheit_var.set("Invalid Input")

# Function to convert Fahrenheit to Celsius
def fahrenheit_to_celsius(event):
    try:
        fahrenheit = float(fahrenheit_entry.get())
        celsius = (fahrenheit - 32) * 5/9
        celsius_var.set(f"{celsius:.2f}")
    except ValueError:
        if fahrenheit_entry.get() == "":
            celsius_var.set("")
        else:
            celsius_var.set("Invalid Input")

# Create the main window
root = tk.Tk()
root.title("Temperature Converter")

# Variables to hold the input and output values
celsius_var = tk.StringVar()
fahrenheit_var = tk.StringVar()

# Create and place the Celsius input widgets
celsius_label = ttk.Label(root, text="Celsius:")
celsius_label.grid(column=0, row=0, padx=10, pady=10)

celsius_entry = ttk.Entry(root, textvariable=celsius_var)
celsius_entry.grid(column=1, row=0, padx=10, pady=10)
celsius_entry.bind("<KeyRelease>", celsius_to_fahrenheit)

# Create and place the Fahrenheit input widgets
fahrenheit_label = ttk.Label(root, text="Fahrenheit:")
fahrenheit_label.grid(column=0, row=1, padx=10, pady=10)

fahrenheit_entry = ttk.Entry(root, textvariable=fahrenheit_var)
fahrenheit_entry.grid(column=1, row=1, padx=10, pady=10)
fahrenheit_entry.bind("<KeyRelease>", fahrenheit_to_celsius)

# Run the main loop
root.mainloop()