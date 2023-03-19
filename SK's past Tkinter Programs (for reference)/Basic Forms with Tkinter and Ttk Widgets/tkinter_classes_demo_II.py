import tkinter as tk
root = tk.Tk()
class LabelInput(tk.Frame):
    def __init__(
        self, parent, label, inp_cls, inp_args, *args, **kwargs
    ):
        super().__init__(parent, *args, **kwargs)
        self.label = tk.Label(self, text=label, anchor="w")
        self.input = inp_cls(self, **inp_args)
        self.columnconfigure(1, weight=1)
        self.label.grid(sticky=tk.E + tk.W)
        self.input.grid(row=0, column=1, sticky=tk.E + tk.W)
li1 = LabelInput(root, "Name", tk.Entry, {"bg": "red"})
li1.grid()
age_var = tk.IntVar(root, value=21)
li2 = LabelInput(root, "Age", tk.Spinbox, {"textvariable": age_var, "from_": 10, "to": 150})
li2.grid()

class MyForm(tk.Frame):
    def __init__(self, parent, data_var, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.data_var = data_var
root.mainloop()
