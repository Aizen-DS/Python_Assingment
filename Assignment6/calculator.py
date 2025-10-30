import tkinter as tk
from tkinter import messagebox

# Create the main window
root = tk.Tk()
root.title("Aizen's Calculator")
root.geometry("320x450")
root.resizable(False, False)
root.config(bg="#1e1e1e")

# Entry field
expression = ""
input_text = tk.StringVar()

# Functions
def btn_click(item):
    global expression
    expression += str(item)
    input_text.set(expression)

def btn_clear():
    global expression
    expression = ""
    input_text.set("")

def btn_equal():
    global expression
    try:
        result = str(eval(expression))
        input_text.set(result)
        expression = result
    except ZeroDivisionError:
        messagebox.showerror("Error", "Division by zero not allowed!")
        expression = ""
        input_text.set("")
    except Exception:
        messagebox.showerror("Error", "Invalid Input!")
        expression = ""
        input_text.set("")

# Display Frame
frame_display = tk.Frame(root, width=312, height=50, bd=0, highlightbackground="#6b6b6b", highlightthickness=2)
frame_display.pack(pady=20)

# Input field
input_field = tk.Entry(frame_display, font=('calibri', 20, 'bold'), textvariable=input_text,
                       width=50, bg="#2b2b2b", fg="#ffffff", bd=0, justify=tk.RIGHT)
input_field.grid(row=0, column=0)
input_field.pack(ipady=10)

# Buttons Frame
frame_buttons = tk.Frame(root, bg="#1e1e1e")
frame_buttons.pack()

# Button layout
buttons = [
    ['C', '/', '*', '-'],
    ['7', '8', '9', '+'],
    ['4', '5', '6', ''],
    ['1', '2', '3', '='],
    ['0', '.', '', '']
]

# Create buttons dynamically
for row_index, row_values in enumerate(buttons):
    for col_index, value in enumerate(row_values):
        if value == "":
            continue
        elif value == "C":
            tk.Button(frame_buttons, text=value, fg="#ff4d4d", bg="#3c3c3c",
                      font=('calibri', 18, 'bold'), width=5, height=2, bd=0,
                      command=btn_clear).grid(row=row_index, column=col_index, padx=5, pady=5)
        elif value == "=":
            tk.Button(frame_buttons, text=value, fg="#00ff99", bg="#3c3c3c",
                      font=('calibri', 18, 'bold'), width=5, height=2, bd=0,
                      command=btn_equal).grid(row=row_index, column=col_index, padx=5, pady=5)
        else:
            tk.Button(frame_buttons, text=value, fg="#ffffff", bg="#3c3c3c",
                      font=('calibri', 18, 'bold'), width=5, height=2, bd=0,
                      command=lambda val=value: btn_click(val)).grid(row=row_index, column=col_index, padx=5, pady=5)

root.mainloop()
