import tkinter as tk
from tkinter import ttk
import random
import json
import os

window = tk.Tk()
window.title("Affirmation Generator")
window.geometry("500x400")
window.resizable(False, False)
window.configure(bg="#fefae0")

canvas = tk.Canvas(
    window,
    width=500,
    height=400,
    bg="#0b1d3a",
    highlightthickness=0
)
canvas.place(x=0, y=0)
# canvas.create_oval(50, 50, 550, 550, fill="#f3c5ff", outline="", stipple="gray50")

max_width = 450

frame = tk.Frame(window, bg="#0b1d3a", width=max_width, height=360)
# frame.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)
frame.place(relx=0.5, rely=0.5, anchor="center")
frame.grid_columnconfigure(0, weight=1)
frame.grid_propagate(False)
frame.lift()

stars = []

def create_stars(num=80):
    for _ in range(num):
        x = random.randint(0,600)
        y = random.randint(0,600)

        if 180 < x < 320 and 140 < y < 320:
            continue

        r = random.randint(1,2)
        star = canvas.create_oval (x-r, y-r, x+r, y+r, fill="white", outline="")
        stars.append(star)

def twinkle():
    for star in stars:
        color = random.choice(["white", "#d0d0d0", "#4c566a"])
        canvas.itemconfig(star, fill=color)
    window.after(500, twinkle)

create_stars(60)
twinkle()

af_file = "affirmations.json"

def load_af():
    if not os.path.exists(af_file):
        print("File not found!")
        return {"General": ["I am growing each day."]}
    with open(af_file, "r") as file:
        return json.load(file)
    
def save_af():
    with open(af_file, "w") as file:
        json.dump(affirmation_data, file, indent=4)

affirmation_data = load_af()

affirmation_frame = tk.Frame(
    frame,
    bg="#deffe1",
    bd=2,
    relief="groove"
)

affirmation_frame.grid(row=0, column=0, padx=10, pady=(30,40))

affirmation_label = tk.Label(
    affirmation_frame,
    text="Generate Affirmation",
    font=("Segoe Script", 14),
    wraplength=400,
    fg="#333333",
    bg="#deffe1",
    justify="center",
    height=5,
    anchor="center")

affirmation_label.pack(fill="both", expand=True, padx=10, pady=10)

def display_random_on_start():
    all_affirmations=[]

    for af_list in affirmation_data.values():
        all_affirmations.extend(af_list)

    if all_affirmations:
        random_af = random.choice(all_affirmations)
        affirmation_label.config(text=random_af)


selected_category = tk.StringVar()
categories = list(affirmation_data.keys()) or ["General"]
selected_category.set(categories[0])

style = ttk.Style()
style.theme_use("clam")

style.configure(
    "TCombobox",
    fieldbackground="#ffffff",
    background="#b9fbc0",
    foreground="#333333",
    font=("Helvetica", 11), 
    padding=5
)

style.map(
    "TCombobox",
    fieldbackground=[("readonly", "#ffffff")],
    background=[("active", "#a3c4f3")],
    foreground=[("disabled", "#999"), ("readonly", "#333")]
)

category_menu = ttk.Combobox(
    frame,
    textvariable=selected_category,
    values=categories,
    font=("Helvetica", 12),
    width=32,
    state="readonly"
)

category_menu.grid(
    row=1,
    column=0,
    pady=(0, 10),
    padx=20,
    sticky="ew"
)

def display_af():
    category = selected_category.get()
    if category in affirmation_data and affirmation_data[category]:
        selected = random.choice(affirmation_data[category])
        affirmation_label.config(text=selected)
    else: 
        affirmation_label.config(text="No affirmations in this category")

generate_button = tk.Button(
    frame,
    text="Generate Affirmation",
    command=display_af,
    font=("Helvetica", 12),
    bg="#b9fbc0",
    fg="#333333",
    padx=10,
    activebackground="#a3c4f3",
    width=32
)
generate_button.grid(
    row=2,
    column=0,
    pady=(0,8),
    padx=20,
    sticky="ew"
)

# entry_box = tk.Entry(
#     window,
#     width=40,
#     font=("Helvetica", 12)
# )d
# entry_box.pack(pady=10)

# def add_af():
#     new_affirmation = entry_box.get().strip()

#     if new_affirmation:
#         affirmation_data.append(new_affirmation)
#         save_af()
#         affirmation_label.config(text="Affirmation successfully added!")
#         entry_box.delete(0, tk.END)
#     else:
#         affirmation_label.config(text="Please enter a valid affirmation!")

# add_button = tk.Button(
#     window,
#     text="Add Affirmation",
#     command=add_af,
#     font=("Helvetica", 12),
#     bg="#606c38",
#     fg="white"
# )
# add_button.pack(pady=5)
display_random_on_start()
window.mainloop()