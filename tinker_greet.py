import tkinter as tk

def greet():
    name = entry.get()
    if name:
        greeting_label.config(text=f"Hello, {name}!")
    else:
        greeting_label.config(text="Hello, Guest!")

root = tk.Tk()
root.title("Greeting App")

tk.Label(root, text="Enter your name:").pack(pady=5)

entry = tk.Entry(root)
entry.pack(pady=5)

greet_button = tk.Button(root, text="Greet Me", command=greet)
greet_button.pack(pady=5)

greeting_label = tk.Label(root, text="")
greeting_label.pack(pady=5)

root.mainloop()
