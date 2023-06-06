import tkinter as tk

class CheckBox(tk.Frame):
    def __init__(self, master, text, value, command=None, size=20, font_size=12, fill_color="red", outline_color="red", active_outline_color="green", active_fill_color="green", outline_width=2):
        tk.Frame.__init__(self, master)

        self.config(bg="white")
        
        variable = tk.StringVar()
        self.value = value
        self.variable = variable
        self.command = command

        self.fill_color = fill_color
        self.outline_color = outline_color
        self.active_outline_color = active_outline_color
        self.active_fill_color = active_fill_color

        self.text = tk.Label(self, text=text, font=("Helvetica", font_size), bg="white")
        self.circle = tk.Canvas(self, width=size, height=size, bg="white", borderwidth=0, border=0, highlightcolor="white", highlightthickness=0, relief="flat")
        self.oval = self.circle.create_oval(size // 4, size // 4, size * 3 // 4, size * 3 // 4, fill=fill_color, outline=outline_color, width=outline_width)
        self.text.pack(side="left")
        self.circle.pack(side="right")
        self.circle.bind("<Button-1>", self._toggle)

    def _toggle(self, event=None):
        if self.variable.get() == self.value:
            self.variable.set("0")
            self.circle.itemconfig(self.oval, fill=self.fill_color, outline=self.outline_color)
        else:
            self.variable.set(self.value)
            self.circle.itemconfig(self.oval, fill=self.active_fill_color, outline=self.active_outline_color)
        if self.command:
            self.command()

    def select(self):
        self.variable.set(self.value)
        self.circle.itemconfig(self.oval, fill=self.active_fill_color, outline=self.active_outline_color)

    def deselect(self):
        print("deselect")
        self.variable.set("0")
        self.circle.itemconfig(self.oval, fill=self.fill_color, outline=self.outline_color)

    def get_state(self):
        return self.variable.get() == self.value

# import tkinter as tk

# root = tk.Tk()

# checkbox.pack()

# root.mainloop() 