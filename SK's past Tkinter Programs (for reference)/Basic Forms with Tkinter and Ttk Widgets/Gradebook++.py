import tkinter as tk
from tkinter import ttk
root = tk.Tk()

class InputLabel(tk.Frame):
    def __init__(self, parent, label, inp_cls, inp_args, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.label = tk.Label(self, text=label)
        self.input = inp_cls(self, **inp_args)
        self.columnconfigure(1, weight = 1)
        self.label.grid(sticky = tk.W +tk.E)
        self.input.grid(row=0, column = 1, sticky = tk.W +tk.E)

        

News = ttk.Notebook(root)
News.grid()
news_catalogue = ["CNN", "CBC", "BBC", "FOX", "NP", "REUTERS","NPR"]
news_tabs = {}
for i in news_catalogue:
    news_tabs[i] = tk.Frame(News, width=400, height=400)
    News.add(news_tabs[i], text=i)
News.grid()
root.mainloop()