import tkinter as tk
from tkinter import messagebox

# Create the main window
root = tk.Tk()
root.title("Graphical Calculator")
root.geometry("400x500")
root.resizable(False, False)

# Colors
bg_color = "#2C3E50"
btn_color = "#1ABC9C"
text_color = "#ECF0F1"

# Configure the main window
root.configure(bg=bg_color)

# Calculator display
entry = tk.Entry(root, font=("Arial", 20), bg=text_color, fg=bg_color, bd=10, justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Click handler for buttons
def button_click(value):
    if value == "C":
        entry.delete(0, tk.END)
    elif value == "=":
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            messagebox.showerror("Error", "Invalid Input")
    else:
        entry.insert(tk.END, value)

# Button layout
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("C", 4, 0), ("0", 4, 1), ("=", 4, 2), ("+", 4, 3),
]

# Add buttons to the window
for (text, row, col) in buttons:
    button = tk.Button(root, text=text, font=("Arial", 18), bg=btn_color, fg=text_color,
                       width=5, height=2, command=lambda val=text: button_click(val))
    button.grid(row=row, column=col, padx=5, pady=5)

# Run the application
root.mainloop()
