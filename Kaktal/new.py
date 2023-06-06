import tkinter
from turtle import bgcolor
import customtkinter
from PIL import Image, ImageTk 
from datetime import date



customtkinter.set_appearance_mode("light")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

 
class Add(customtkinter.CTkFrame):

    WIDTH = 1280
    HEIGHT = 720

    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller

        # ============ create frame for top ============

        for i in range(10):
            self.grid_columnconfigure(i, weight=1)
        # self.grid_rowconfigure(0, weight=1)

        # make the background white
        self.configure(bg_color="white")
        self.configure(fg_color="white")

        # add a label to the frame
        self.title = customtkinter.CTkLabel(master=self, text="Add Profile", font=("helvetica", 40), bg_color="white", fg_color="white", text_color="#265BAA")
        self.title.grid(row=0, column=0, sticky="nsew", pady=50, padx=0, columnspan=10)

        # ROW 1

        # add image up.png on a button to the frame
        self.up1im = customtkinter.CTkImage(Image.open("images/up.png"), size=(100,90))
        self.button_up1 = customtkinter.CTkButton(master=self, image=self.up1im, command=self.up1, text="", fg_color="white", bg_color="white", text_color="white", hover_color="white", width=70)
        self.button_up1.grid(row=1, column=1, sticky="nsew", pady=5, padx=4)

        # add image up.png on a button to the frame
        self.up2im = customtkinter.CTkImage(Image.open("images/up.png"), size=(100,90))
        self.button_up2 = customtkinter.CTkButton(master=self, image=self.up2im, command=self.up2, text="", fg_color="white", bg_color="white", text_color="white", hover_color="white", width=70)
        self.button_up2.grid(row=1, column=3, sticky="nsew", pady=5, padx=4) 

        # add image up.png on a button to the frame
        self.up3im = customtkinter.CTkImage(Image.open("images/up.png"), size=(100,90))
        self.button_up3 = customtkinter.CTkButton(master=self, image=self.up3im, command=self.up3, text="", fg_color="white", bg_color="white", text_color="white", hover_color="white", width=70)
        self.button_up3.grid(row=1, column=5, sticky="nsew", pady=5, padx=4)

        # add image up.png on a button to the frame
        self.up4im = customtkinter.CTkImage(Image.open("images/up.png"), size=(100,90))
        self.button_up4 = customtkinter.CTkButton(master=self, image=self.up4im, command=self.up4, text="", fg_color="white", bg_color="white", text_color="white", hover_color="white", width=70)
        self.button_up4.grid(row=1, column=7, sticky="nsew", pady=5, padx=4)

        # add image up.png on a button to the frame
        self.up5im = customtkinter.CTkImage(Image.open("images/up.png"), size=(100,90))
        self.button_up5 = customtkinter.CTkButton(master=self, image=self.up5im, command=self.up5, text="", fg_color="white", bg_color="white", text_color="white", hover_color="white", width=70)
        self.button_up5.grid(row=1, column=9, sticky="nsew", pady=5, padx=4)

        # ROW 2
        # add a label with white background to the frame
        self.label1 = customtkinter.CTkLabel(master=self, text="1", font=("helvetica", 35),  bg_color="white", fg_color="white", text_color="black", width=70)
        self.label1.grid(row=2, column=0, sticky="nsew", pady=5, padx=4)

        # add a label with grey background to the frame
        self.station1 = customtkinter.CTkLabel(master=self, text="0", font=("helvetica", 35),  bg_color="white", fg_color="light blue", text_color="black", width=70, height=60)
        self.station1.grid(row=2, column=1, sticky="nsew", pady=5, padx=4)

        # add a label with grey background to the frame
        self.label3 = customtkinter.CTkLabel(master=self, text="2", font=("helvetica", 35),  bg_color="white", fg_color="white", text_color="black", width=70)
        self.label3.grid(row=2, column=2, sticky="nsew", pady=5, padx=4)

        # add a label with grey background to the frame
        self.station2 = customtkinter.CTkLabel(master=self, text="0", font=("helvetica", 35),  bg_color="white", fg_color="light blue", text_color="black", width=70, height=60)
        self.station2.grid(row=2, column=3, sticky="nsew", pady=5, padx=4)

        # add a label with grey background to the frame
        self.label5 = customtkinter.CTkLabel(master=self, text="3", font=("helvetica", 35),  bg_color="white", fg_color="white", text_color="black", width=70)
        self.label5.grid(row=2, column=4, sticky="nsew", pady=5, padx=4)

        # add a label with grey background to the frame
        self.station3 = customtkinter.CTkLabel(master=self, text="0", font=("helvetica", 35),  bg_color="white", fg_color="light blue", text_color="black", width=70, height=60)
        self.station3.grid(row=2, column=5, sticky="nsew", pady=5, padx=4)

        # add a label with grey background to the frame
        self.label7 = customtkinter.CTkLabel(master=self, text="4", font=("helvetica", 35),  bg_color="white", fg_color="white", text_color="black", width=70)
        self.label7.grid(row=2, column=6, sticky="nsew", pady=5, padx=4)

        # add a label with grey background to the frame
        self.station4 = customtkinter.CTkLabel(master=self, text="0", font=("helvetica", 35),  bg_color="white", fg_color="light blue", text_color="black", width=70, height=60)
        self.station4.grid(row=2, column=7, sticky="nsew", pady=5, padx=4)

        # add a label with grey background to the frame
        self.label9 = customtkinter.CTkLabel(master=self, text="5", font=("helvetica", 35),  bg_color="white", fg_color="white", text_color="black", width=70)
        self.label9.grid(row=2, column=8, sticky="nsew", pady=5, padx=4)

        # add a label with grey background to the frame
        self.label00 = customtkinter.CTkLabel(master=self, text="", font=("helvetica", 35), bg_color="white", fg_color="white", text_color="black", width=100)
        self.label00.grid(row=2, column=10, sticky="nsew", pady=5, padx=40)

        # add a label with grey background to the frame
        self.station5 = customtkinter.CTkLabel(master=self, text="0", font=("helvetica", 35),  bg_color="white", fg_color="light blue", text_color="black", width=70, height=60)
        self.station5.grid(row=2, column=9, sticky="nsew", pady=5, padx=4)

        # ROW 3
        # add image down.png on a button to the frame
        self.down1im = customtkinter.CTkImage(Image.open("images/down.png"), size=(100,90))
        self.button_down1 = customtkinter.CTkButton(master=self, image=self.down1im, command=self.down1, text="", fg_color="white", bg_color="white", text_color="white", hover_color="white", width=70)
        self.button_down1.grid(row=3, column=1, sticky="nsew", pady=5, padx=4)

        # add image down.png on a button to the frame
        self.down2im = customtkinter.CTkImage(Image.open("images/down.png"), size=(100,90))
        self.button_down2 = customtkinter.CTkButton(master=self, image=self.down2im, command=self.down2, text="", fg_color="white", bg_color="white", text_color="white", hover_color="white", width=70)
        self.button_down2.grid(row=3, column=3, sticky="nsew", pady=5, padx=4)

        # add image down.png on a button to the frame
        self.down3im = customtkinter.CTkImage(Image.open("images/down.png"), size=(100,90))
        self.button_down3 = customtkinter.CTkButton(master=self, image=self.down3im, command=self.down3, text="", fg_color="white", bg_color="white", text_color="white", hover_color="white", width=70)
        self.button_down3.grid(row=3, column=5, sticky="nsew", pady=5, padx=4)

        # add image down.png on a button to the frame
        self.down4im = customtkinter.CTkImage(Image.open("images/down.png"), size=(100,90))
        self.button_down4 = customtkinter.CTkButton(master=self, image=self.down4im, command=self.down4, text="", fg_color="white", bg_color="white", text_color="white", hover_color="white", width=70)
        self.button_down4.grid(row=3, column=7, sticky="nsew", pady=5, padx=4)

        # add image down.png on a button to the frame
        self.down5im = customtkinter.CTkImage(Image.open("images/down.png"), size=(100,90))
        self.button_down5 = customtkinter.CTkButton(master=self, image=self.down5im, command=self.down5, text="", fg_color="white", bg_color="white", text_color="white", hover_color="white", width=70)
        self.button_down5.grid(row=3, column=9, sticky="nsew", pady=5, padx=4)
        # ROW 1

        # add image up.png on a button to the frame
        self.up1im = customtkinter.CTkImage(Image.open("images/up.png"), size=(100,90))
        self.button_up1 = customtkinter.CTkButton(master=self, image=self.up1im, command=self.up6, text="", fg_color="white", bg_color="white", text_color="white", hover_color="white", width=70)
        self.button_up1.grid(row=4, column=1, sticky="nsew", pady=5, padx=4)

        # add image up.png on a button to the frame
        self.up2im = customtkinter.CTkImage(Image.open("images/up.png"), size=(100,90))
        self.button_up2 = customtkinter.CTkButton(master=self, image=self.up2im, command=self.up7, text="", fg_color="white", bg_color="white", text_color="white", hover_color="white", width=70)
        self.button_up2.grid(row=4, column=3, sticky="nsew", pady=5, padx=4) 

        # add image up.png on a button to the frame
        self.up3im = customtkinter.CTkImage(Image.open("images/up.png"), size=(100,90))
        self.button_up3 = customtkinter.CTkButton(master=self, image=self.up3im, command=self.up8, text="", fg_color="white", bg_color="white", text_color="white", hover_color="white", width=70)
        self.button_up3.grid(row=4, column=5, sticky="nsew", pady=5, padx=4)

        # add image up.png on a button to the frame
        self.up4im = customtkinter.CTkImage(Image.open("images/up.png"), size=(100,90))
        self.button_up4 = customtkinter.CTkButton(master=self, image=self.up4im, command=self.up9, text="", fg_color="white", bg_color="white", text_color="white", hover_color="white", width=70)
        self.button_up4.grid(row=4, column=7, sticky="nsew", pady=5, padx=4)

        # ROW 2
        # add a label with white background to the frame
        self.label1 = customtkinter.CTkLabel(master=self, text="6", font=("helvetica", 35),  bg_color="white", fg_color="white", text_color="black", width=70)
        self.label1.grid(row=5, column=0, sticky="nsew", pady=5, padx=4)

        # add a label with grey background to the frame
        self.station6 = customtkinter.CTkLabel(master=self, text="0", font=("helvetica", 35),  bg_color="white", fg_color="light blue", text_color="black", width=70, height=60)
        self.station6.grid(row=5, column=1, sticky="nsew", pady=5, padx=4)

        # add a label with grey background to the frame
        self.label3 = customtkinter.CTkLabel(master=self, text="7", font=("helvetica", 35),  bg_color="white", fg_color="white", text_color="black", width=70)
        self.label3.grid(row=5, column=2, sticky="nsew", pady=5, padx=4)

        # add a label with grey background to the frame
        self.station7 = customtkinter.CTkLabel(master=self, text="0", font=("helvetica", 35),  bg_color="white", fg_color="light blue", text_color="black", width=70, height=60)
        self.station7.grid(row=5, column=3, sticky="nsew", pady=5, padx=4)

        # add a label with grey background to the frame
        self.label5 = customtkinter.CTkLabel(master=self, text="8", font=("helvetica", 35),  bg_color="white", fg_color="white", text_color="black", width=70)
        self.label5.grid(row=5, column=4, sticky="nsew", pady=5, padx=4)

        # add a label with grey background to the frame
        self.station8 = customtkinter.CTkLabel(master=self, text="0", font=("helvetica", 35),  bg_color="white", fg_color="light blue", text_color="black", width=70, height=60)
        self.station8.grid(row=5, column=5, sticky="nsew", pady=5, padx=4)

        # add a label with grey background to the frame
        self.label7 = customtkinter.CTkLabel(master=self, text="9", font=("helvetica", 35),  bg_color="white", fg_color="white", text_color="black", width=70)
        self.label7.grid(row=5, column=6, sticky="nsew", pady=5, padx=4)

        # add a label with grey background to the frame
        self.station9 = customtkinter.CTkLabel(master=self, text="0", font=("helvetica", 35),  bg_color="white", fg_color="light blue", text_color="black", width=70, height=60)
        self.station9.grid(row=5, column=7, sticky="nsew", pady=5, padx=4)


        # ROW 3
        # add image down.png on a button to the frame
        self.down1im = customtkinter.CTkImage(Image.open("images/down.png"), size=(100,90))
        self.button_down1 = customtkinter.CTkButton(master=self, image=self.down1im, command=self.down6, text="", fg_color="white", bg_color="white", text_color="white", hover_color="white", width=70)
        self.button_down1.grid(row=6, column=1, sticky="nsew", pady=5, padx=4)

        # add image down.png on a button to the frame
        self.down2im = customtkinter.CTkImage(Image.open("images/down.png"), size=(100,90))
        self.button_down2 = customtkinter.CTkButton(master=self, image=self.down2im, command=self.down7, text="", fg_color="white", bg_color="white", text_color="white", hover_color="white", width=70)
        self.button_down2.grid(row=6, column=3, sticky="nsew", pady=5, padx=4)

        # add image down.png on a button to the frame
        self.down3im = customtkinter.CTkImage(Image.open("images/down.png"), size=(100,90))
        self.button_down3 = customtkinter.CTkButton(master=self, image=self.down3im, command=self.down8, text="", fg_color="white", bg_color="white", text_color="white", hover_color="white", width=70)
        self.button_down3.grid(row=6, column=5, sticky="nsew", pady=5, padx=4)

        # add image down.png on a button to the frame
        self.down4im = customtkinter.CTkImage(Image.open("images/down.png"), size=(100,90))
        self.button_down4 = customtkinter.CTkButton(master=self, image=self.down4im, command=self.down9, text="", fg_color="white", bg_color="white", text_color="white", hover_color="white", width=70)
        self.button_down4.grid(row=6, column=7, sticky="nsew", pady=5, padx=4)

        # ROW 1

        # add image up.png on a button to the frame
        self.up1im = customtkinter.CTkImage(Image.open("images/up.png"), size=(100,90))
        self.button_up1 = customtkinter.CTkButton(master=self, image=self.up1im, command=self.up10, text="", fg_color="white", bg_color="white", text_color="white", hover_color="white", width=70)
        self.button_up1.grid(row=7, column=1, sticky="nsew", pady=5, padx=4)

        # add image up.png on a button to the frame
        self.up2im = customtkinter.CTkImage(Image.open("images/up.png"), size=(100,90))
        self.button_up2 = customtkinter.CTkButton(master=self, image=self.up2im, command=self.up11, text="", fg_color="white", bg_color="white", text_color="white", hover_color="white", width=70)
        self.button_up2.grid(row=7, column=3, sticky="nsew", pady=5, padx=4) 

        # add image up.png on a button to the frame
        self.up3im = customtkinter.CTkImage(Image.open("images/up.png"), size=(100,90))
        self.button_up3 = customtkinter.CTkButton(master=self, image=self.up3im, command=self.up12, text="", fg_color="white", bg_color="white", text_color="white", hover_color="white", width=70)
        self.button_up3.grid(row=7, column=5, sticky="nsew", pady=5, padx=4)

        # add image up.png on a button to the frame
        self.up4im = customtkinter.CTkImage(Image.open("images/up.png"), size=(100,90))
        self.button_up4 = customtkinter.CTkButton(master=self, image=self.up4im, command=self.up13, text="", fg_color="white", bg_color="white", text_color="white", hover_color="white", width=70)
        self.button_up4.grid(row=7, column=7, sticky="nsew", pady=5, padx=4)

        # ROW 2
        # add a label with white background to the frame
        self.label1 = customtkinter.CTkLabel(master=self, text="10", font=("helvetica", 35),  bg_color="white", fg_color="white", text_color="black", width=70)
        self.label1.grid(row=8, column=0, sticky="nsew", pady=5, padx=4)

        # add a label with grey background to the frame
        self.station10 = customtkinter.CTkLabel(master=self, text="0", font=("helvetica", 35),  bg_color="white", fg_color="light blue", text_color="black", width=70, height=60)
        self.station10.grid(row=8, column=1, sticky="nsew", pady=5, padx=4)

        # add a label with grey background to the frame
        self.label3 = customtkinter.CTkLabel(master=self, text="11", font=("helvetica", 35),  bg_color="white", fg_color="white", text_color="black", width=70)
        self.label3.grid(row=8, column=2, sticky="nsew", pady=5, padx=4)

        # add a label with grey background to the frame
        self.station11 = customtkinter.CTkLabel(master=self, text="0", font=("helvetica", 35),  bg_color="white", fg_color="light blue", text_color="black", width=70, height=60)
        self.station11.grid(row=8, column=3, sticky="nsew", pady=5, padx=4)

        # add a label with grey background to the frame
        self.label5 = customtkinter.CTkLabel(master=self, text="12", font=("helvetica", 35),  bg_color="white", fg_color="white", text_color="black", width=70)
        self.label5.grid(row=8, column=4, sticky="nsew", pady=5, padx=4)

        # add a label with grey background to the frame
        self.station12 = customtkinter.CTkLabel(master=self, text="0", font=("helvetica", 35),  bg_color="white", fg_color="light blue", text_color="black", width=70, height=60)
        self.station12.grid(row=8, column=5, sticky="nsew", pady=5, padx=4)

        # add a label with grey background to the frame
        self.label7 = customtkinter.CTkLabel(master=self, text="13", font=("helvetica", 35),  bg_color="white", fg_color="white", text_color="black", width=70)
        self.label7.grid(row=8, column=6, sticky="nsew", pady=5, padx=4)

        # add a label with grey background to the frame
        self.station13 = customtkinter.CTkLabel(master=self, text="0", font=("helvetica", 35),  bg_color="white", fg_color="light blue", text_color="black", width=70, height=60)
        self.station13.grid(row=8, column=7, sticky="nsew", pady=5, padx=4)

        # # add a label with grey background to the frame
        # self.label9 = customtkinter.CTkLabel(master=self, text="Save Profile", font=("helvetica", 35, "bold"), bg_color="light blue", fg_color="light blue", text_color="black", width=70, height=60)
        # self.label9.grid(row=8, column=8, sticky="ew", pady=10, padx=4, rowspan=2, columnspan=2)


        self.button_container = customtkinter.CTkFrame(master=self, bg_color="white", fg_color="white")
        self.button_container.grid(row=5, column=8,sticky="news", pady=10, padx=50, rowspan=6, columnspan=4)
        self.button_container.grid_columnconfigure(0, weight=1)
        # self.button_container = self

        # add a rounded button for save profile
        self.button = customtkinter.CTkButton(master=self.button_container, text="SAVE", font=("helvetica", 35), bg_color="white", fg_color="light green", text_color="black", hover_color="#00b050", height=80, command=self.save)
        self.button.grid(row=7, column=0, sticky="ew", pady=20, padx=60, rowspan=1, columnspan=2)

        # add a rounded button for BACK profile
        self.button = customtkinter.CTkButton(master=self.button_container, text="BACK", font=("helvetica", 35), bg_color="white", fg_color="light blue", text_color="black", hover_color="#65aaff", height=80, command=self.start_app)
        self.button.grid(row=8, column=0, sticky="ew", pady=20, padx=60, rowspan=1, columnspan=2)

        # ROW 3
        # add image down.png on a button to the frame
        self.down1im = customtkinter.CTkImage(Image.open("images/down.png"), size=(100,90))
        self.button_down1 = customtkinter.CTkButton(master=self, image=self.down1im, command=self.down10, text="", fg_color="white", bg_color="white", text_color="white", hover_color="white", width=70)
        self.button_down1.grid(row=9, column=1, sticky="nsew", pady=5, padx=4)

        # add image down.png on a button to the frame
        self.down2im = customtkinter.CTkImage(Image.open("images/down.png"), size=(100,90))
        self.button_down2 = customtkinter.CTkButton(master=self, image=self.down2im, command=self.down11, text="", fg_color="white", bg_color="white", text_color="white", hover_color="white", width=70)
        self.button_down2.grid(row=9, column=3, sticky="nsew", pady=5, padx=4)

        # add image down.png on a button to the frame
        self.down3im = customtkinter.CTkImage(Image.open("images/down.png"), size=(100,90))
        self.button_down3 = customtkinter.CTkButton(master=self, image=self.down3im, command=self.down12, text="", fg_color="white", bg_color="white", text_color="white", hover_color="white", width=70)
        self.button_down3.grid(row=9, column=5, sticky="nsew", pady=5, padx=4)

        # add image down.png on a button to the frame
        self.down4im = customtkinter.CTkImage(Image.open("images/down.png"), size=(100,90))
        self.button_down4 = customtkinter.CTkButton(master=self, image=self.down4im, command=self.down13, text="", fg_color="white", bg_color="white", text_color="white", hover_color="white", width=70)
        self.button_down4.grid(row=9, column=7, sticky="nsew", pady=5, padx=4)


    def start_app(self):
        self.controller.show_frame("home")

    def up1(self):
        self.records['1'] += 0.5
        self.station1.configure(text=f"{self.records['1']}")
    
    def down1(self):
        if self.records['1'] > 0:
            self.records['1'] -= 0.5
            self.station1.configure(text=f"{self.records['1']}")

    def up2(self):
        self.records['2'] += 0.5
        self.station2.configure(text=f"{self.records['2']}")

    def down2(self):
        if self.records['2'] > 0:
            self.records['2'] -= 0.5
            self.station2.configure(text=f"{self.records['2']}")

    def up3(self):
        self.records['3'] += 0.5
        self.station3.configure(text=f"{self.records['3']}")

    def down3(self):
        if self.records['3'] > 0:
            self.records['3'] -= 0.5
            self.station3.configure(text=f"{self.records['3']}")

    def up4(self):
        self.records['4'] += 0.5
        self.station4.configure(text=f"{self.records['4']}")

    def down4(self):
        if self.records['4'] > 0:
            self.records['4'] -= 0.5
            self.station4.configure(text=f"{self.records['4']}")

    def up5(self):
        self.records['5'] += 0.5
        self.station5.configure(text=f"{self.records['5']}")

    def down5(self):
        if self.records['5'] > 0:
            self.records['5'] -= 0.5
            self.station5.configure(text=f"{self.records['5']}")

    def up6(self):
        self.records['6'] += 0.5
        self.station6.configure(text=f"{self.records['6']}")

    def down6(self):
        if self.records['6'] > 0:
            self.records['6'] -= 0.5
            self.station6.configure(text=f"{self.records['6']}")

    def up7(self):
        self.records['7'] += 0.5
        self.station7.configure(text=f"{self.records['7']}")

    def down7(self):
        if self.records['7'] > 0:
            self.records['7'] -= 0.5
            self.station7.configure(text=f"{self.records['7']}")

    def up8(self):
        self.records['8'] += 0.5
        self.station8.configure(text=f"{self.records['8']}")

    def down8(self):
        if self.records['8'] > 0:
            self.records['8'] -= 0.5
            self.station8.configure(text=f"{self.records['8']}")

    def up9(self):
        self.records['9'] += 0.5
        self.station9.configure(text=f"{self.records['9']}")

    def down9(self):
        if self.records['9'] > 0:
            self.records['9'] -= 0.5
            self.station9.configure(text=f"{self.records['9']}")

    def up10(self):
        self.records['10'] += 0.5
        self.station10.configure(text=f"{self.records['10']}")

    def down10(self):
        if self.records['10'] > 0:
            self.records['10'] -= 0.5
            self.station10.configure(text=f"{self.records['10']}")

    def up11(self):
        self.records['11'] += 0.5
        self.station11.configure(text=f"{self.records['11']}")

    def down11(self):
        if self.records['11'] > 0:
            self.records['11'] -= 0.5
            self.station11.configure(text=f"{self.records['11']}")

    def up12(self):
        self.records['12'] += 0.5
        self.station12.configure(text=f"{self.records['12']}")

    def down12(self):
        if self.records['12'] > 0:
            self.records['12'] -= 0.5
            self.station12.configure(text=f"{self.records['12']}")

    def up13(self):
        self.records['13'] += 0.5
        self.station13.configure(text=f"{self.records['13']}")

    def down13(self):
        if self.records['13'] > 0:
            self.records['13'] -= 0.5
            self.station13.configure(text=f"{self.records['13']}")

    def load(self, profile):
        import pickle
        with open('records.pickle', 'rb') as f:
            records = pickle.load(f)
        self.profile = profile
        
        self.records = {
                "name": profile,
                "fav": False,
                "1": 0,
                "2": 0,
                "3": 0,
                "4": 0,
                "5": 0,
                "6": 0,
                "7": 0,
                "8": 0,
                "9": 0,
                "10": 0,
                "11": 0,
                "12": 0,
                "13": 0,
            }

        self.title.configure(text=f"Add {self.records['name']}")

        self.station1.configure(text=f"{self.records['1']}")
        self.station2.configure(text=f"{self.records['2']}")
        self.station3.configure(text=f"{self.records['3']}")
        self.station4.configure(text=f"{self.records['4']}")
        self.station5.configure(text=f"{self.records['5']}")
        self.station6.configure(text=f"{self.records['6']}")
        self.station7.configure(text=f"{self.records['7']}")
        self.station8.configure(text=f"{self.records['8']}")
        self.station9.configure(text=f"{self.records['9']}")
        self.station10.configure(text=f"{self.records['10']}")
        self.station11.configure(text=f"{self.records['11']}")
        self.station12.configure(text=f"{self.records['12']}")
        self.station13.configure(text=f"{self.records['13']}") 


    def add_profile(self, profile):
        self.load(profile)
        self.controller.show_frame("add")

    def save(self):
        import pickle
        with open('records.pickle', 'rb') as f:
            records = pickle.load(f)
        edited = False
        for i in records:
            if i['name'] == self.records['name']:
                i = records
                edited = True
                break
        if not edited:
            records.append(self.records)

        
        with open('records.pickle', 'wb') as f:
            pickle.dump(records, f)
        self.start_app()
