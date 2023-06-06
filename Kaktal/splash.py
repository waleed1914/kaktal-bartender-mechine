import random
import tkinter
from turtle import bgcolor
import customtkinter
from PIL import Image, ImageTk 
from datetime import date



customtkinter.set_appearance_mode("light")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

 
class Splash(customtkinter.CTkFrame):

    WIDTH = 1300
    HEIGHT = 1080

    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller

        # ============ create frame for top ============

        self.grid_columnconfigure(0, weight=1)
        # self.grid_rowconfigure(0, weight=1)

        # make the background white
        self.configure(bg_color="white")
        self.configure(fg_color="white")

        random_number = random.randint(1, 8)
        self.logo = Image.open(f"images/Logos/{random_number}.png")
        
        self.logo = customtkinter.CTkImage(light_image=self.logo, dark_image=self.logo, size=(self.WIDTH * self.HEIGHT // self.logo.height, self.HEIGHT))
        self.label_logo = customtkinter.CTkLabel(master=self, image=self.logo, text="")
        self.label_logo.grid(row=0, column=0, sticky="nsew")

        # # add a label to the frame
        # self.label = customtkinter.CTkLabel(master=self, text="Splash Screen", font=("Helvetica", 35, "bold"), bg_color="white", fg_color="white", text_color="#265BAA")
        # self.label.grid(row=0, column=0, sticky="nsew", pady=100)

        # # add a label to the frame
        # self.label = customtkinter.CTkLabel(master=self, text="LOGO", font=("Helvetica", 30, "bold"), bg_color="white", fg_color="white", text_color="#265BAA")
        # self.label.grid(row=1, column=0, sticky="nsew", pady=50)

        # self.after(20000, self.show_frame)
        self.after(10000, self.show_frame)
    
    def show_frame(self):
        self.controller.show_frame("home")
    
    
    def restart(self):
        self.tkraise()
        print("restartt ...............................")
        self.after(3000, self.show_frame)

    def shutdown(self):
        self.tkraise()
        print("shut down ............................")
        self.after(3000, self.power_off)

    def power_off(self):
        self.controller.show_frame("shutdown")
        self.controller.frames["shutdown"].shutdown()
