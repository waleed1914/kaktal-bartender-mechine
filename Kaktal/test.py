from functools import partial
import tkinter as tk
from tkinter import ttk
import customtkinter
import tkinter
from PIL import Image, ImageTk

from messagebox import CustomMessageBox 

class Test(customtkinter.CTkFrame):

    def __init__(self, root, controller):
        super().__init__(root)

        self.controller = controller

        # ============ create frame for top ============
        self.grid_columnconfigure(0, weight=1)
        # self.grid_rowconfigure(0, weight=1)

        # make the background white
        self.configure(bg_color="white")
        self.configure(fg_color="white")

        # add a label to the frame
        self.home_label = customtkinter.CTkLabel(master=self, text="HOME", font=("Helvetica", 40), bg_color="white", fg_color="white", text_color="#265BAA")
        self.home_label.grid(row=0, column=0, sticky="nsew", pady=10)
        

        self.f_one = -1
        self.f_two = -1
        self.f_three = -1


        # Create a frame for the self.canvas with non-zero row&column weights
        self.frame_canvas = tkinter.Frame(self)
        self.frame_canvas.grid(row=2, column=0, pady=(20, 20), sticky='nw')
        # self.frame_canvas.grid_rowconfigure(0, weight=1)
        # self.frame_canvas.grid_columnconfigure(0, weight=1)
        # Set grid_propagate to False to allow 5-by-5 self.buttons resizing later
        # self.frame_canvas.grid_propagate(False)

        # Add a self.canvas in that frame
        self.canvas = tkinter.Canvas(self.frame_canvas, bg="white")
        self.canvas.grid(row=0, column=0, sticky="news")

        # Link a scrollbar to the self.canvas
        style = ttk.Style()
        style.theme_use('clam')
        style.layout('My.Vertical.TScrollbar', 
             [('Vertical.Scrollbar.trough',
               {'children': [('Vertical.Scrollbar.thumb', 
                              {'expand': '1', 'sticky': 'nswe'})],
                'sticky': 'ns'})]) 

        style.configure("My.Vertical.TScrollbar", gripcount=0, background="#93cddd", 
                troughcolor='#4f81bd', borderwidth=2, bordercolor='#385d8a',
                lightcolor='#385d8a', darkcolor='#385d8a',
                arrowsize=80)  
        
        style.map("My.Vertical.TScrollbar", background=[('active', "#385d8a")], arrowcolor=[('selected', "red")])

               
        # add a container for the self.buttons
        self.container_buttons = customtkinter.CTkFrame(master=self, bg_color="white", fg_color="light pink", height=200)
        self.container_buttons.grid(row=3, column=0, sticky="nsew", pady=15, padx=20)

        # add a rounded button for save profile
        self.button_search = customtkinter.CTkButton(master=self.container_buttons, command=self.add_ui, text="SEARCH", font=("Helvetica", 35), bg_color="light pink", fg_color="#00b0f0", text_color="black", hover_color="#00b0f0",  width=300, height=80)
        self.button_search.grid(row=0, column=7, sticky="ew", pady=40, padx=840, rowspan=3)
        

        # # use pickle to save the records
        import pickle
        # with open("records.pickle", "wb") as f:
        #     pickle.dump(self.records, f)

        # use pickle to load the records
        with open("records.pickle", "rb") as f:
            self.records = pickle.load(f)

        self.f_records = self.search()
        self.f_records = self.custom_sort(self.f_records)


        ### sort the records to display favoirte profiles first
        

        rows = len(self.f_records)

        self.unstar_image = Image.open("images/unstar.png")
        self.star_image = Image.open("images/fav.png")
        

        self.name_label = customtkinter.CTkLabel(master=self.container_buttons, text="FIND", font=("Helvetica", 35), bg_color="light pink", fg_color="light pink", text_color="black")
        self.name_label.grid(row=0, column=1, sticky="nsew", pady=10, padx=40, rowspan=3)

        # add up1.png as a button to the container
        self.up1_image = customtkinter.CTkImage(Image.open("images/up1.png"), size=(45, 30))
        # self.fav_image = self.fav_image.create_scaled_photo_image(1.5, "orange")
        # create a button with the image
        self.button_up1 = customtkinter.CTkButton(master=self.container_buttons, command=self.up2_one, image=self.up1_image, width=40, height=40, bg_color="light pink", fg_color="light pink", hover_color="light pink", text_color="white", text="", font=("Helvetica", 10))
        self.button_up1.grid(row=0, column=3, sticky="nsew", padx=10)

        self.f_value1 = customtkinter.CTkLabel(master=self.container_buttons, text="0", font=("Helvetica", 35), bg_color="light pink", fg_color="light pink", text_color="black")
        self.f_value1.grid(row=1, column=3, sticky="nsew", padx=20)

        # add down1.png as a button to the container
        self.down1_image = customtkinter.CTkImage(Image.open("images/down1.png"), size=(45, 30))
        # self.fav_image = self.fav_image.create_scaled_photo_image(1.5, "orange")
        # create a button with the image
        self.button_down1 = customtkinter.CTkButton(master=self.container_buttons, command=self.down2_one, image=self.down1_image, width=40, height=40, bg_color="light pink", fg_color="light pink", hover_color="light pink", text_color="white", text="", font=("Helvetica", 10))
        self.button_down1.grid(row=2, column=3, sticky="nsew", padx=10)


        # add up1.png as a button to the container
        self.up1_image = customtkinter.CTkImage(Image.open("images/up1.png"), size=(45, 30))
        # self.fav_image = self.fav_image.create_scaled_photo_image(1.5, "orange")
        # create a button with the image
        self.button_up2 = customtkinter.CTkButton(master=self.container_buttons, command=self.up2_two, image=self.up1_image, width=40, height=40, bg_color="light pink", fg_color="light pink", hover_color="light pink", text_color="white", text="", font=("Helvetica", 10))
        self.button_up2.grid(row=0, column=4, sticky="nsew", padx=10)

        self.f_value2 = customtkinter.CTkLabel(master=self.container_buttons, text="0", font=("Helvetica", 35), bg_color="light pink", fg_color="light pink", text_color="black")
        self.f_value2.grid(row=1, column=4, sticky="nsew", padx=20)

        # add down1.png as a button to the container
        self.down2_image = customtkinter.CTkImage(Image.open("images/down1.png"), size=(45, 30))
        # self.fav_image = self.fav_image.create_scaled_photo_image(1.5, "orange")
        # create a button with the image
        self.button_down2 = customtkinter.CTkButton(master=self.container_buttons,  command=self.down2_two, image=self.down1_image, width=40, height=40, bg_color="light pink", fg_color="light pink", hover_color="light pink", text_color="white", text="", font=("Helvetica", 10))
        self.button_down2.grid(row=2, column=4, sticky="nsew", padx=10)


        # add up1.png as a button to the container
        self.up1_image = customtkinter.CTkImage(Image.open("images/up1.png"), size=(45, 30))
        # self.fav_image = self.fav_image.create_scaled_photo_image(1.5, "orange")
        # create a button with the image
        self.button_up3 = customtkinter.CTkButton(master=self.container_buttons, command=self.up2_three , image=self.up1_image, width=40, height=40, bg_color="light pink", fg_color="light pink", hover_color="light pink", text_color="white", text="", font=("Helvetica", 10))
        self.button_up3.grid(row=0, column=5, sticky="nsew", padx=10)

        self.f_value3 = customtkinter.CTkLabel(master=self.container_buttons, text="0", font=("Helvetica", 35), bg_color="light pink", fg_color="light pink", text_color="black")
        self.f_value3.grid(row=1, column=5, sticky="nsew", padx=20)

        # add down1.png as a button to the container
        self.down1_image = customtkinter.CTkImage(Image.open("images/down1.png"), size=(45, 30))
        # self.fav_image = self.fav_image.create_scaled_photo_image(1.5, "orange")
        # create a button with the image
        self.button_down3 = customtkinter.CTkButton(master=self.container_buttons, command=self.down2_three, image=self.down1_image, width=40, height=40, bg_color="light pink", fg_color="light pink", hover_color="light pink", text_color="white", text="", font=("Helvetica", 10))
        self.button_down3.grid(row=2, column=5, sticky="nsew", padx=10)


        # add a label to the frame
        self.label = customtkinter.CTkLabel(master=self.container_buttons, text="", font=("Helvetica", 35), bg_color="light pink", fg_color="light pink", text_color="#265BAA")
        self.label.grid(row=1, column=6, sticky="nsew", pady=0, padx=150)

        
        #################################################################################################################################
        #################################################################################################################################
        #################################################################################################################################

        
        # add a container for the self.buttons
        self.container_buttons = customtkinter.CTkFrame(master=self, bg_color="white", fg_color="light green", height=200)
        self.container_buttons.grid(row=4, column=0, sticky="nsew", pady=0, padx=20)

        self.name_label = customtkinter.CTkLabel(master=self.container_buttons, text="NEW", font=("Helvetica", 35), bg_color="light green", fg_color="light green", text_color="black")
        self.name_label.grid(row=0, column=1, sticky="nsew", pady=60, padx=40, rowspan=3)

        # add up1.png as a button to the container
        self.up1_image = customtkinter.CTkImage(Image.open("images/up1.png"), size=(45, 30))
        # self.fav_image = self.fav_image.create_scaled_photo_image(1.5, "orange")
        # create a button with the image
        self.button_up1 = customtkinter.CTkButton(master=self.container_buttons, command=self.up_one, image=self.up1_image, width=40, height=40, bg_color="light green", fg_color="light green", hover_color="light green", text_color="white", text="", font=("Helvetica", 10))
        self.button_up1.grid(row=0, column=3, sticky="nsew", padx=10)

        self.value1 = customtkinter.CTkLabel(master=self.container_buttons, text="0", font=("Helvetica", 35), bg_color="light green", fg_color="light green", text_color="black")
        self.value1.grid(row=1, column=3, sticky="nsew", padx=20)

        # add down1.png as a button to the container
        self.down1_image = customtkinter.CTkImage(Image.open("images/down1.png"), size=(45, 30))
        # self.fav_image = self.fav_image.create_scaled_photo_image(1.5, "orange")
        # create a button with the image
        self.button_down1 = customtkinter.CTkButton(master=self.container_buttons, command=self.down_one, image=self.down1_image, width=40, height=40, bg_color="light green", fg_color="light green", hover_color="light green", text_color="white", text="", font=("Helvetica", 10))
        self.button_down1.grid(row=2, column=3, sticky="nsew", padx=10)


        # add up1.png as a button to the container
        self.up1_image = customtkinter.CTkImage(Image.open("images/up1.png"), size=(45, 30))
        # self.fav_image = self.fav_image.create_scaled_photo_image(1.5, "orange")
        # create a button with the image
        self.button_up2 = customtkinter.CTkButton(master=self.container_buttons, command=self.up_two, image=self.up1_image, width=40, height=40, bg_color="light green", fg_color="light green", hover_color="light green", text_color="white", text="", font=("Helvetica", 10))
        self.button_up2.grid(row=0, column=4, sticky="nsew", padx=10)

        self.value2 = customtkinter.CTkLabel(master=self.container_buttons, text="0", font=("Helvetica", 35), bg_color="light green", fg_color="light green", text_color="black")
        self.value2.grid(row=1, column=4, sticky="nsew", padx=20)

        # add down1.png as a button to the container
        self.down2_image = customtkinter.CTkImage(Image.open("images/down1.png"), size=(45, 30))
        # self.fav_image = self.fav_image.create_scaled_photo_image(1.5, "orange")
        # create a button with the image
        self.button_down2 = customtkinter.CTkButton(master=self.container_buttons,  command=self.down_two, image=self.down1_image, width=40, height=40, bg_color="light green", fg_color="light green", hover_color="light green", text_color="white", text="", font=("Helvetica", 10))
        self.button_down2.grid(row=2, column=4, sticky="nsew", padx=10)


        # add up1.png as a button to the container
        self.up1_image = customtkinter.CTkImage(Image.open("images/up1.png"), size=(45, 30))
        # self.fav_image = self.fav_image.create_scaled_photo_image(1.5, "orange")
        # create a button with the image
        self.button_up3 = customtkinter.CTkButton(master=self.container_buttons, command=self.up_three , image=self.up1_image, width=40, height=40, bg_color="light green", fg_color="light green", hover_color="light green", text_color="white", text="", font=("Helvetica", 10))
        self.button_up3.grid(row=0, column=5, sticky="nsew", padx=10)

        self.value3 = customtkinter.CTkLabel(master=self.container_buttons, text="0", font=("Helvetica", 35), bg_color="light green", fg_color="light green", text_color="black")
        self.value3.grid(row=1, column=5, sticky="nsew", padx=20)

        # add down1.png as a button to the container
        self.down1_image = customtkinter.CTkImage(Image.open("images/down1.png"), size=(45, 30))
        # self.fav_image = self.fav_image.create_scaled_photo_image(1.5, "orange")
        # create a button with the image
        self.button_down3 = customtkinter.CTkButton(master=self.container_buttons, command=self.down_three, image=self.down1_image, width=40, height=40, bg_color="light green", fg_color="light green", hover_color="light green", text_color="white", text="", font=("Helvetica", 10))
        self.button_down3.grid(row=2, column=5, sticky="nsew", padx=10)


        # add a label to the frame
        self.profile_label = customtkinter.CTkLabel(master=self.container_buttons, text="Drink already exists", font=("Helvetica", 35), bg_color="light green", fg_color="light green", text_color="light green")
        self.profile_label.grid(row=1, column=6, sticky="nsew", pady=0, padx=262)

        # add a rounded button for save profile
        self.button_save = customtkinter.CTkButton(master=self.container_buttons, command=self.create, text="CREATE", font=("Helvetica", 35), bg_color="light green", fg_color="#00b0f0", text_color="black", hover_color="#00b0f0",  width=300, height=80)
        self.button_save.grid(row=0, column=7, sticky="ew", pady=0, padx=320, rowspan=3)

        
        # add a container for the self.buttons
        self.container_buttons = customtkinter.CTkFrame(master=self, bg_color="white", fg_color="white", height=200)
        self.container_buttons.grid(row=5, column=0, sticky="nsew", pady=15, padx=20)

        # add a label to the frame
        self.label = customtkinter.CTkLabel(master=self.container_buttons, text="", font=("Helvetica", 35), bg_color="white", fg_color="white", text_color="white")
        self.label.grid(row=1, column=2, sticky="nsew", pady=30, padx=550)

        # add a rounded button for save profile
        self.button_save = customtkinter.CTkButton(master=self.container_buttons, command=self.shutdown, text="SHUTDOWN", font=("Helvetica", 35), bg_color="white", fg_color="light pink", text_color="black", hover_color="light pink",  width=300, height=80)
        self.button_save.grid(row=1, column=4, sticky="ew", pady=30, padx=50, rowspan=3)

        # add a rounded button for save profile
        self.button_save = customtkinter.CTkButton(master=self.container_buttons, command=self.clean, text="CLEAN/PRIME", font=("Helvetica", 35), bg_color="white", fg_color="light green", text_color="black", hover_color="light green",  width=300, height=80)
        self.button_save.grid(row=1, column=5, sticky="ew", pady=30, padx=50, rowspan=3)
        
        self.one = 0
        self.two = 0
        self.three = 0


        self.f_one = -1
        self.f_two = -1
        self.f_three = -1


        self.down2_one()
        self.down2_two()
        self.down2_three()


        self.profile_exists()

        
        self.add_ui()



    def event():
        print("Event")

    def run_profile(self, profile):
        CustomMessageBox(self.master, command=lambda: self.start_profile(profile), message=f"Do you want to run {profile}?")

    def start_profile(self, profile):
        self.controller.show_frame("running")
        self.controller.frames["running"].run_profile(profile)

    def edit_profile(self, profile):
        self.controller.frames["edit"].edit_profile(profile)

    def add_ui(self):
        # self.load_state()


        # Create a frame for the self.canvas with non-zero row&column weights
        self.frame_canvas = tkinter.Frame(self, bg="green")
        self.frame_canvas.grid(row=2, column=0, pady=(0, 0), sticky='nw')
        self.frame_canvas.grid_rowconfigure(0, weight=1)
        self.frame_canvas.grid_columnconfigure(0, weight=1)
        # Set grid_propagate to False to allow 5-by-5 self.buttons resizing later
        self.frame_canvas.grid_propagate(False)

        # Add a self.canvas in that frame
        self.canvas = tkinter.Canvas(self.frame_canvas, bg="white")
        self.canvas.grid(row=0, column=0, sticky="news", padx=0)



        self.vsb = ttk.Scrollbar(self.frame_canvas, orient="vertical", style="My.Vertical.TScrollbar", command=self.canvas.yview)


        # vsb = tkinter.Scrollbar(self.frame_canvas, orient="vertical", width=80,command=self.canvas.yview)
        self.vsb.grid(row=0, column=1, sticky='ns')
        self.canvas.configure(yscrollcommand=self.vsb.set)

        # Create a frame to contain the self.buttons
        self.frame_buttons = tkinter.Frame(self.canvas, bg="white", width=10)

        self.canvas.create_window((0, 0), window=self.frame_buttons, anchor='nw')

        import pickle
    
        with open("records.pickle", "rb") as f:
            self.records = pickle.load(f)

        self.f_records = self.search()
        self.f_records = self.custom_sort(self.f_records)

        rows = len(self.f_records)

        self.buttons = [customtkinter.CTkFrame(None, width=100, height=100) for j in range(rows)]
        self.images = [customtkinter.CTkImage(self.unstar_image) for j in range(rows)]

        for i in range(0, rows):
            # self.buttons[i] = customtkinter.CTkFrame(frame_buttons, bg_color="red", width=100, height=100)
            # self.buttons[i].grid(row=i, column=0, sticky='news')
            self.buttons[i] = customtkinter.CTkFrame(master=self.frame_buttons, bg_color="white", fg_color="light blue", height=100)
            self.buttons[i].grid(row=i+1, column=0, sticky="nsew", pady=10, padx=30)

            # add fav.png as a button to the container
            self.images[i] = customtkinter.CTkImage(self.unstar_image, size=(100, 100))
            # self.fav_image = self.fav_image.create_scaled_photo_image(1.5, "orange")
            # create a button with the image
            self.button_fav = customtkinter.CTkButton(master=self.buttons[i], image=self.images[i], width=100, height=100, bg_color="light blue", fg_color="light blue", hover_color="light blue", text_color="white", text="", font=("Helvetica", 10), command=partial(self.fav, self.f_records[i]['name']))
            self.button_fav.grid(row=0, column=0, sticky="nsew", padx=10)

            self.name_label = customtkinter.CTkLabel(master=self.buttons[i], text=f"{(self.f_records[i]['name'])}", font=("Helvetica", 35), bg_color="light blue", fg_color="light blue", text_color="black")
            self.name_label.grid(row=0, column=1, sticky="nsew", pady=10, padx=40)

            self.space_label = customtkinter.CTkLabel(master=self.buttons[i], text=f"", font=("Helvetica", 35), bg_color="light blue", fg_color="light blue", text_color="black")
            self.space_label.grid(row=0, column=2, sticky="nsew", pady=10, padx=530)
            
            # add a rounded button for save profile
            self.button_edit = customtkinter.CTkButton(master=self.buttons[i], text="EDIT", font=("Helvetica", 35), bg_color="light blue", fg_color="#00b0f0", text_color="black", hover_color="#00b0f0", width=160, height=70, command=partial(self.edit_profile, self.f_records[i]['name']))
            self.button_edit.grid(row=0, column=3, sticky="ew", pady=10, padx=0)

            # add a rounded button for save profile
            self.button_save = customtkinter.CTkButton(master=self.buttons[i], text="RUN", font=("Helvetica", 35), bg_color="light blue", fg_color="#00b0f0", text_color="black", hover_color="#00b0f0", width=160, height=70, command=partial(self.run_profile, self.f_records[i]['name']))
            self.button_save.grid(row=0, column=4, sticky="ew", pady=10, padx=15)

            try:
                if (self.f_records[i]['fav'] == 0):
                    self.images[i].configure(light_image=self.unstar_image)
                else:
                    self.images[i].configure(light_image=self.star_image)
            except:
                self.images[i].configure(light_image=self.unstar_image)
        # Update self.buttons frames idle tasks to let tkinter calculate self.buttons sizes
        self.frame_buttons.update_idletasks()

        # Resize the self.canvas frame to show exactly 5-by-5 self.buttons and the scrollbar
        # try:
        first5columns_width = 1920
        # except:
        #     first5columns_width = 70
        # try:
        first5rows_height = sum([125 for i in range(4)])
        # except:
        #     first5rows_height = 70

        self.frame_canvas.config(width=first5columns_width + self.vsb.winfo_width(),
                            height=first5rows_height)

        # Set the self.canvas scrolling region
        self.canvas.config(scrollregion=self.canvas.bbox("all"))

        
        self.one = -1
        self.two = -1
        self.three = -1


        self.up_one()
        self.up_two()
        self.up_three()


        self.profile_exists()

    def clean(self):
        print("cleaning")
        self.controller.show_frame("clean")

    def shutdown(self):
        CustomMessageBox(self.master, message="Are you sure you want to shutdown?", command=self.start_shutdown)

    def start_shutdown(self):
        self.controller.show_frame("splash")
        self.controller.frames["splash"].shutdown()

    def up_one(self):
        if self.one < 9:
            self.one += 1
            self.value1.configure(text=f"{self.one}")
            self.profile_exists()

    def down_one(self):
        if self.one > 0:
            self.one -= 1
            self.value1.configure(text=f"{self.one}")
            self.profile_exists()

    def up_two(self):
        if self.two < 9:
            self.two += 1
            self.value2.configure(text=f"{self.two}")
            self.profile_exists()

    def down_two(self):
        if self.two > 0:
            self.two -= 1
            self.value2.configure(text=f"{self.two}")
            self.profile_exists()

    def up_three(self):
        if self.three < 9:
            self.three += 1
            self.value3.configure(text=f"{self.three}")
            self.profile_exists()
    
    def down_three(self):
        if self.three > 0:
            self.three -= 1
            self.value3.configure(text=f"{self.three}")
            self.profile_exists()

    def up2_one(self):
        if self.f_one < 9:
            self.f_one += 1
            self.f_value1.configure(text=f"{self.f_one}")
            # self.profile_exists()

    def down2_one(self):
        if self.f_one > 0:
            self.f_one -= 1
            self.f_value1.configure(text=f"{self.f_one}")
            # self.profile_exists()
        else:
            self.f_one = -1
            self.f_value1.configure(text="-")

    def up2_two(self):
        if self.f_two < 9:
            self.f_two += 1
            self.f_value2.configure(text=f"{self.f_two}")
            # self.profile_exists()

    def down2_two(self):
        if self.f_two > 0:
            self.f_two -= 1
            self.f_value2.configure(text=f"{self.f_two}")
            # self.profile_exists()
        else:
            self.f_two = -1
            self.f_value2.configure(text="-")

    def up2_three(self):
        if self.f_three < 9:
            self.f_three += 1
            self.f_value3.configure(text=f"{self.f_three}")
            # self.profile_exists()
    
    def down2_three(self):
        if self.f_three > 0:
            self.f_three -= 1
            self.f_value3.configure(text=f"{self.f_three}")
            # self.profile_exists()
        else:
            self.f_three = -1
            self.f_value3.configure(text="-")

    def create(self):
        name = f"Drink {self.one}{self.two}{self.three}"
        if not self.profile_exists():
            self.controller.frames['add'].add_profile(name)

    def profile_exists(self):
        name = f"Drink {self.one}{self.two}{self.three}"
        exists = False
        # check if the name is already in the records
        for record in self.records:
            if record['name'] == name:
                exists = True
                break

        if exists:
            self.profile_label.configure(text_color="red")
        else: 
            self.profile_label.configure(text_color="light green")
        return exists

    def fav(self, name):
        for i in range(len(self.f_records)):
            if self.f_records[i]['name'] == name:
                if self.f_records[i]['fav'] == True:
                    self.f_records[i]['fav'] = False
                    self.images[i].configure(light_image=self.unstar_image)
                else:
                    self.f_records[i]['fav'] = True
                    self.images[i].configure(light_image=self.star_image)
               
        for i in range(len(self.records)):
            if self.records[i]['name'] == name:
                if self.records[i]['fav'] == True:
                    self.records[i]['fav'] = False
                else:
                    self.records[i]['fav'] = True
                break
        # save the records 
        import pickle
        with open('records.pickle', 'wb') as f:
            pickle.dump(self.records, f)


    def search(self):
        print("searching")
        fitlered_records = []

        if self.f_one == -1 and self.f_two == -1 and self.f_three == -1:
            self.home_label.configure(text="Home")
            self.button_search.configure(text="Search")
        else:
            self.home_label.configure(text=f"Search {self.f_value1._text}{self.f_value2._text}{self.f_value3._text}")
            self.button_search.configure(text="Back")

        for record in self.records:
            # get last 3 characters of the name
            name = record['name'][-3:]
            if self.f_one != -1:
                if name[0] != str(self.f_one):
                    continue
            if self.f_two != -1:
                if name[1] != str(self.f_two):
                    continue
            if self.f_three != -1:
                if name[2] != str(self.f_three):
                    continue
            fitlered_records.append(record.copy())
        
        self.f_one = -1
        self.f_two = -1
        self.f_three = -1
        try:
            if self.f_value1:
                self.f_value1.configure(text="-")
            if self.f_value2:
                self.f_value2.configure(text="-")
            if self.f_value3:
                self.f_value3.configure(text="-")
        except:
            pass

        return fitlered_records.copy()

    def custom_sort(self, records):
        print("sorting the records")

        # sort the records by fav key
        records2 = sorted(records, key=lambda x: (not x['fav'], x['name']))
        print(records2)

        return records2