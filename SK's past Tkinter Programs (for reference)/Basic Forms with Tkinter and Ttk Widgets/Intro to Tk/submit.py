import tkinter as tk
def sub(name_inp, num_inp, color_inp, info_inp):
        name=name_inp.get()
        number=num_inp.get()
        selected_idx=color_inp.curselection()
        if selected_idx:
            color=color_inp.get(selected_idx)
        else:
            color=""
        infop = info_inp.get("1.0", tk.END)
        message = (f"Thnks for taking the survey, {name}. \n Enjoy your {number} {color} bananas")
        
