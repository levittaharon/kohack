import tkinter as tk
class tkinterApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        #        super.__init__(*args, **kwargs)
        container = tk.Frame(self)
        container.pack(side = "top", fill= "both", expand=True)
        container.grid_columnconfigure(0, weight=1)
        container.grid_rowconfigure(0, weight=1)
        self.frames = {}
        for f in (Start, Two, Three):
            self.frames[f] = f(container, self)
            self.frames[f].grid(row=0, column=0, sticky="nsew")
        self.show_frame(Start)
    def show_frame(self, cont):
        self.frames[cont].tkraise()

class Start(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        label = tk.Label(self, text="Start")
        label.grid(padx=10, pady=10)
        button = tk.Button(self, text="Two", command = lambda: controller.show_frame(Two))
        button.grid()
        button2 = tk.Button(self, text="Three", command = lambda: controller.show_frame(Three))
        button2.grid()

class Two(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        label = tk.Label(self, text="Two")
        label.grid(padx=10, pady=10)
        button = tk.Button(self, text="Start", command = lambda: controller.show_frame(Start))
        button.grid()
        button2 = tk.Button(self, text="Three", command = lambda: controller.show_frame(Three))
        button2.grid()

class Three(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        label = tk.Label(self, text="Three")
        label.grid(padx=10, pady=10)
        button = tk.Button(self, text="Two", command = lambda: controller.show_frame(Two))
        button.grid()
        button2 = tk.Button(self, text="Start", command = lambda: controller.show_frame(Start))
        button2.grid()

tkinterApp().mainloop()