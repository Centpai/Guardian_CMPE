import tkinter as tk

# ------------------ Logic ------------------
def on_number_click(num):
    output.config(text=output["text"] + str(num))

def clear_output():
    output.config(text="")

def on_operator_click(op):
    current = output["text"]
    if current and current[-1] not in "+-×÷":
        output.config(text=current + op)

def calculate_result():
    try:
        expression = output["text"].replace("×", "*").replace("÷", "/")
        result = eval(expression)
        output.config(text=str(result))
    except:
        output.config(text="Error")

# ------------------ UI Setup ------------------
root = tk.Tk()
root.title("Calculator")
root.geometry("320x450")
root.configure(bg="#1e1e1e")
root.resizable(False, False)

# Display
output = tk.Label(
    root,
    text="",
    font=("Segoe UI", 26),
    bg="#2d2d2d",
    fg="white",
    anchor="e",
    padx=15,
    height=2
)
output.pack(fill="x", padx=10, pady=15)

# Button frame
btn_frame = tk.Frame(root, bg="#1e1e1e")
btn_frame.pack(expand=True, fill="both", padx=10, pady=10)

# Button style function
def create_btn(text, row, col, bg, cmd):
    btn = tk.Button(
        btn_frame,
        text=text,
        font=("Segoe UI", 16, "bold"),
        bg=bg,
        fg="white",
        bd=0,
        command=cmd,
        activebackground="#555"
    )
    btn.grid(row=row, column=col, sticky="nsew", padx=6, pady=6)

# Buttons layout
buttons = [
    ("7", 0, 0, "#3a3a3a"), ("8", 0, 1, "#3a3a3a"), ("9", 0, 2, "#3a3a3a"), ("÷", 0, 3, "#ff9500"),
    ("4", 1, 0, "#3a3a3a"), ("5", 1, 1, "#3a3a3a"), ("6", 1, 2, "#3a3a3a"), ("×", 1, 3, "#ff9500"),
    ("1", 2, 0, "#3a3a3a"), ("2", 2, 1, "#3a3a3a"), ("3", 2, 2, "#3a3a3a"), ("-", 2, 3, "#ff9500"),
    ("0", 3, 0, "#3a3a3a"), ("AC", 3, 1, "#ff3b30"), ("=", 3, 2, "#34c759"), ("+", 3, 3, "#ff9500"),
]

for text, r, c, color in buttons:
    if text.isdigit():
        create_btn(text, r, c, color, lambda t=text: on_number_click(t))
    elif text == "AC":
        create_btn(text, r, c, color, clear_output)
    elif text == "=":
        create_btn(text, r, c, color, calculate_result)
    else:
        create_btn(text, r, c, color, lambda t=text: on_operator_click(t))


for i in range(4):
    btn_frame.columnconfigure(i, weight=1)
    btn_frame.rowconfigure(i, weight=1)

root.mainloop()
