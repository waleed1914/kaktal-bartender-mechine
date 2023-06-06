import tkinter
from turtle import bgcolor
import customtkinter
from PIL import Image, ImageTk 
from datetime import date



customtkinter.set_appearance_mode("light")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

 
class Home(customtkinter.CTkFrame):

    WIDTH = 1280
    HEIGHT = 720

    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller

        # ============ create frame for top ============

        self.grid_columnconfigure(0, weight=1)
        # self.grid_rowconfigure(0, weight=1)

        # make the background white
        self.configure(bg_color="white")
        self.configure(fg_color="white")

        # add a label to the frame
        self.label = customtkinter.CTkLabel(master=self, text="HOME", font=("Helvetica", 35, "bold"), bg_color="white", fg_color="white", text_color="#265BAA")
        self.label.grid(row=0, column=0, sticky="nsew", pady=0)

        #
        self.container_buttons_scrollable = customtkinter.CTkFrame(master=self, bg_color="light grey", fg_color="white", height=300)
        self.container_buttons_scrollable.grid(row=1, column=0, sticky="nsew", pady=20, padx=20)


        for i in range(2):
            # add a container for the buttons
            self.container_buttons = customtkinter.CTkFrame(master=self.container_buttons_scrollable, bg_color="white", fg_color="light grey", height=100)
            self.container_buttons.grid(row=i+1, column=0, sticky="nsew", pady=10, padx=20)

            # add fav.png as a button to the container
            self.fav_image = customtkinter.CTkImage(Image.open("images/fav.png"), size=(100, 100))
            # self.fav_image = self.fav_image.create_scaled_photo_image(1.5, "orange")
            # create a button with the image
            self.button_fav = customtkinter.CTkButton(master=self.container_buttons, image=self.fav_image, width=100, height=100, bg_color="light grey", fg_color="light grey", hover_color="light grey", text_color="white", text="", font=("Helvetica", 10, "bold"), command=self.event)
            self.button_fav.grid(row=0, column=0, sticky="nsew", padx=10)

            self.name_label = customtkinter.CTkLabel(master=self.container_buttons, text="Profile Name", font=("Helvetica", 30, "bold"), bg_color="light grey", fg_color="light grey", text_color="black")
            self.name_label.grid(row=0, column=1, sticky="nsew", pady=10, padx=40)

            
            # add a rounded button for save profile
            self.button_edit = customtkinter.CTkButton(master=self.container_buttons, text="Edit Profile", font=("Helvetica", 20, "bold"), bg_color="light grey", fg_color="#265BAA", text_color="white", hover_color="blue", width=160, height=40)
            self.button_edit.grid(row=0, column=2, sticky="ew", pady=10, padx=5)

            # add a rounded button for save profile
            self.button_save = customtkinter.CTkButton(master=self.container_buttons, text="Run Profile", font=("Helvetica", 20, "bold"), bg_color="light grey", fg_color="#265BAA", text_color="white", hover_color="blue", width=160, height=40)
            self.button_save.grid(row=0, column=3, sticky="ew", pady=10, padx=5)
            
        
        # add a container for the buttons
        self.container_buttons = customtkinter.CTkFrame(master=self, bg_color="white", fg_color="light grey", height=150)
        self.container_buttons.grid(row=3, column=0, sticky="nsew", pady=0, padx=20)



        self.name_label = customtkinter.CTkLabel(master=self.container_buttons, text="Name", font=("Helvetica", 30, "bold"), bg_color="light grey", fg_color="light grey", text_color="black")
        self.name_label.grid(row=0, column=1, sticky="nsew", pady=10, padx=40, rowspan=3)

        # add up1.png as a button to the container
        self.up1_image = customtkinter.CTkImage(Image.open("images/up1.png"), size=(15, 15))
        # self.fav_image = self.fav_image.create_scaled_photo_image(1.5, "orange")
        # create a button with the image
        self.button_up1 = customtkinter.CTkButton(master=self.container_buttons, image=self.up1_image, width=40, height=40, bg_color="light grey", fg_color="light grey", hover_color="light grey", text_color="white", text="", font=("Helvetica", 10, "bold"), command=self.event)
        self.button_up1.grid(row=0, column=3, sticky="nsew", padx=10)

        self.value1 = customtkinter.CTkLabel(master=self.container_buttons, text="0", font=("Helvetica", 30, "bold"), bg_color="light grey", fg_color="light grey", text_color="black")
        self.value1.grid(row=1, column=3, sticky="nsew", padx=20)

        # add down1.png as a button to the container
        self.down1_image = customtkinter.CTkImage(Image.open("images/down1.png"), size=(15, 15))
        # self.fav_image = self.fav_image.create_scaled_photo_image(1.5, "orange")
        # create a button with the image
        self.button_down1 = customtkinter.CTkButton(master=self.container_buttons, image=self.down1_image, width=40, height=40, bg_color="light grey", fg_color="light grey", hover_color="light grey", text_color="white", text="", font=("Helvetica", 10, "bold"), command=self.event)
        self.button_down1.grid(row=2, column=3, sticky="nsew", padx=10)


        # add up1.png as a button to the container
        self.up1_image = customtkinter.CTkImage(Image.open("images/up1.png"), size=(15, 15))
        # self.fav_image = self.fav_image.create_scaled_photo_image(1.5, "orange")
        # create a button with the image
        self.button_up2 = customtkinter.CTkButton(master=self.container_buttons, image=self.up1_image, width=40, height=40, bg_color="light grey", fg_color="light grey", hover_color="light grey", text_color="white", text="", font=("Helvetica", 10, "bold"), command=self.event)
        self.button_up2.grid(row=0, column=4, sticky="nsew", padx=10)

        self.value2 = customtkinter.CTkLabel(master=self.container_buttons, text="0", font=("Helvetica", 30, "bold"), bg_color="light grey", fg_color="light grey", text_color="black")
        self.value2.grid(row=1, column=4, sticky="nsew", padx=20)

        # add down1.png as a button to the container
        self.down2_image = customtkinter.CTkImage(Image.open("images/down1.png"), size=(15, 15))
        # self.fav_image = self.fav_image.create_scaled_photo_image(1.5, "orange")
        # create a button with the image
        self.button_down2 = customtkinter.CTkButton(master=self.container_buttons, image=self.down1_image, width=40, height=40, bg_color="light grey", fg_color="light grey", hover_color="light grey", text_color="white", text="", font=("Helvetica", 10, "bold"), command=self.event)
        self.button_down2.grid(row=2, column=4, sticky="nsew", padx=10)


        # add up1.png as a button to the container
        self.up1_image = customtkinter.CTkImage(Image.open("images/up1.png"), size=(15, 15))
        # self.fav_image = self.fav_image.create_scaled_photo_image(1.5, "orange")
        # create a button with the image
        self.button_up3 = customtkinter.CTkButton(master=self.container_buttons, image=self.up1_image, width=40, height=40, bg_color="light grey", fg_color="light grey", hover_color="light grey", text_color="white", text="", font=("Helvetica", 10, "bold"), command=self.event)
        self.button_up3.grid(row=0, column=5, sticky="nsew", padx=10)

        self.value3 = customtkinter.CTkLabel(master=self.container_buttons, text="0", font=("Helvetica", 30, "bold"), bg_color="light grey", fg_color="light grey", text_color="black")
        self.value3.grid(row=1, column=5, sticky="nsew", padx=20)

        # add down1.png as a button to the container
        self.down1_image = customtkinter.CTkImage(Image.open("images/down1.png"), size=(15, 15))
        # self.fav_image = self.fav_image.create_scaled_photo_image(1.5, "orange")
        # create a button with the image
        self.button_down3 = customtkinter.CTkButton(master=self.container_buttons, image=self.down1_image, width=40, height=40, bg_color="light grey", fg_color="light grey", hover_color="light grey", text_color="white", text="", font=("Helvetica", 10, "bold"), command=self.event)
        self.button_down3.grid(row=2, column=5, sticky="nsew", padx=10)


        # add a label to the frame
        self.label = customtkinter.CTkLabel(master=self.container_buttons, text="", font=("Helvetica", 20, "bold"), bg_color="light grey", fg_color="light grey", text_color="#265BAA")
        self.label.grid(row=1, column=6, sticky="nsew", pady=0, padx=120)

        # add a rounded button for save profile
        self.button_save = customtkinter.CTkButton(master=self.container_buttons, text="Create Profile", font=("Helvetica", 20, "bold"), bg_color="light grey", fg_color="#265BAA", text_color="white", hover_color="blue", width=160, height=40)
        self.button_save.grid(row=1, column=7, sticky="ew", pady=10, padx=5)

    

    def event():
        pass