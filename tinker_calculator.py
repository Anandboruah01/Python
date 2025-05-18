import tkinter as tk

def click_button(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + value)

def clear_entry():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Create main window
root = tk.Tk()
root.title("Simple Calculator")

# Entry widget for display
entry = tk.Entry(root, width=16, font=('Arial', 24), borderwidth=2, relief="solid", justify='right')
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Button layout
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

row_val = 1
col_val = 0

for button in buttons:
    action = lambda x=button: click_button(x) if x not in ['=', 'C'] else None
    if button == '=':
        btn = tk.Button(root, text=button, width=5, height=2, font=('Arial', 18), command=calculate)
    elif button == 'C':
        btn = tk.Button(root, text=button, width=5, height=2, font=('Arial', 18), command=clear_entry)
    else:
        btn = tk.Button(root, text=button, width=5, height=2, font=('Arial', 18), command=action)
    btn.grid(row=row_val, column=col_val, padx=5, pady=5)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

root.mainloop()
