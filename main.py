import tkinter as tk
import random
import json
import os

af_list = "affirmations.json"

def load_af():
    if not os.path.exists(af_list):
        return []
    with open(af_list, "r") as file:
        return json.load(file)
    
def save_af():
    with open(af_list, "w") as file:
        json.dump(affirmations, file, indent=4)

window = tk.Tk()
window.title("Affirmation Generator")
window.geometry("400x500")
window.configure(bg="#fefae0")

affirmations = load_af()

affirmation_label = tk.Label(
    window,
    text="Generate Affirmation",
    font=("Helvetica", 14),
    wraplength=350,
    fg="#333")

affirmation_label.pack(pady=80)

def display_af():
    selected = random.choice(affirmations)
    affirmation_label.config(text=selected)

generate_button = tk.Button(
    window,
    text="Generate Affirmation",
    command=display_af,
    font=("Helvetica", 12),
    bg="#dda15e",
    fg="white"
)
generate_button.pack(pady=10)

entry_box = tk.Entry(
    window,
    width=40,
    font=("Helvetica", 12)
)
entry_box.pack(pady=10)

def add_af():
    new_affirmation = entry_box.get()

    if new_affirmation:
        affirmations.append(new_affirmation)
        save_af()
        affirmation_label.config(text="Affirmation successfully added!")
        entry_box.delete(0, tk.END)
    else:
        affirmation_label.config(text="Please enter a valid affirmation!")

add_button = tk.Button(
    window,
    text="Add Affirmation",
    command=add_af,
    font=("Helvetica", 12),
    bg="#606c38",
    fg="white"
)
add_button.pack(pady=5)








window.mainloop()