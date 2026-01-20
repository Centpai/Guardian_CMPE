import tkinter as tk
from tkinter import messagebox

# ========== MAIN WINDOW ==========
root = tk.Tk()
root.title("Electronics Engineering Helper")
root.geometry("460x380")
root.config(bg="#1e1e2e")
root.resizable(False, False)

# ========== COLORS & FONTS ==========
BG_COLOR = "#1e1e2e"
CARD_COLOR = "#2a2a3d"
ACCENT = "#4cafef"
TEXT_COLOR = "white"
BTN_COLOR = "#3b82f6"

FONT_TITLE = ("Segoe UI", 16, "bold")
FONT_LABEL = ("Segoe UI", 10)
FONT_ENTRY = ("Segoe UI", 10)
FONT_BTN = ("Segoe UI", 10, "bold")

# ========== FUNCTIONS ==========
def calculate_ohms_law():
    try:
        v = voltage_entry.get()
        i = current_entry.get()
        r = resistance_entry.get()

        # If one field is empty, compute it using Ohm’s law
        if v == "":
            voltage_entry.insert(0, round(float(i) * float(r), 2))
        elif i == "":
            current_entry.insert(0, round(float(v) / float(r), 2))
        elif r == "":
            resistance_entry.insert(0, round(float(v) / float(i), 2))
        else:
            messagebox.showinfo("Info", "Leave ONE field empty")
    except:
        messagebox.showerror("Error", "Invalid input. Please enter numbers only.")

def clear_all():
    voltage_entry.delete(0, tk.END)
    current_entry.delete(0, tk.END)
    resistance_entry.delete(0, tk.END)

# ========== HEADER ==========
header = tk.Label(
    root,
    text="⚡ Ohm’s Law Calculator",
    bg=ACCENT,
    fg="white",
    font=FONT_TITLE,
    pady=15
)
header.pack(fill="x")

# ========== OHM'S LAW CARD ==========
ohms_frame = tk.Frame(root, bg=CARD_COLOR, padx=30, pady=30)
ohms_frame.pack(pady=30)

tk.Label(
    ohms_frame,
    text="Enter any TWO values",
    bg=CARD_COLOR,
    fg=TEXT_COLOR,
    font=("Segoe UI", 12, "bold")
).grid(row=0, column=0, columnspan=2, pady=(0, 20))

# Helper function to create label + entry row
def create_row(text, row):
    tk.Label(
        ohms_frame,
        text=text,
        bg=CARD_COLOR,
        fg=TEXT_COLOR,
        font=FONT_LABEL
    ).grid(row=row, column=0, padx=10, pady=8, sticky="e")

    entry = tk.Entry(
        ohms_frame,
        font=FONT_ENTRY,
        width=18,
        justify="center"
    )
    entry.grid(row=row, column=1, padx=10, pady=8)
    return entry

# Input fields
voltage_entry = create_row("Voltage (V)", 1)
current_entry = create_row("Current (I)", 2)
resistance_entry = create_row("Resistance (Ω)", 3)

# Calculate Button
tk.Button(
    ohms_frame,
    text="Calculate",
    font=FONT_BTN,
    bg=BTN_COLOR,
    fg="white",
    width=22,
    command=calculate_ohms_law
).grid(row=4, column=0, columnspan=2, pady=20)

# Clear Button
tk.Button(
    root,
    text="Clear All",
    font=FONT_BTN,
    bg="#ef4444",
    fg="white",
    width=22,
    command=clear_all
).pack(pady=10)

# ========== RUN ==========
root.mainloop()
