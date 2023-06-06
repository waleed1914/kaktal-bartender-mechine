import tkinter as tk
from turtle import bgcolor
import customtkinter
from PIL import Image, ImageTk 
from datetime import date
import time

import RPi.GPIO as GPIO

from radiobutton import CheckBox



customtkinter.set_appearance_mode("light")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

 
class Clean(customtkinter.CTkFrame):

    WIDTH = 1280
    HEIGHT = 720

    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller

        # ============ create frame for top ============

        # for i in range(10):
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(6, weight=1)

        # make the background white
        self.configure(bg_color="white")
        self.configure(fg_color="white")

        # add a label to the frame
        self.title = customtkinter.CTkLabel(master=self, text="Clean/Prime", font=("Helvetica", 50), bg_color="white", fg_color="white", text_color="Black")
        self.title.grid(row=0, column=0, sticky="nsew", pady=30, padx=0, columnspan=10)

        self.seconds_frame = customtkinter.CTkFrame(master=self, bg_color="white", fg_color="white")
        self.seconds_frame.grid(row=1, column=1, sticky="nsew", pady=0, padx=80, rowspan=3)

        self.select_all_frame = customtkinter.CTkFrame(master=self, bg_color="white", fg_color="white")
        self.select_all_frame.grid(row=1, column=0, sticky="nsew", pady=0, padx=0)

        self.select_all = CheckBox(master=self.select_all_frame, text="Select All On", value="1", size=125, font_size=30, outline_color="green", active_fill_color="green", outline_width=10, fill_color="white", command=self.select_all_on)
        self.select_all.grid(row=0, column=0, sticky="nsew", pady=0, padx=400)
        
        self.up1im = customtkinter.CTkImage(Image.open("images/up2.png"), size=(90,100))
        self.button_up1 = customtkinter.CTkButton(master=self.seconds_frame, image=self.up1im, command=self.up_arrow, text="", fg_color="white", bg_color="white", text_color="white", hover_color="white", width=70)
        self.button_up1.grid(row=0, column=1, sticky="nsew", pady=0, padx=0)

        self.seconds = 0

        self.sec_label = customtkinter.CTkLabel(master=self.seconds_frame, width=20, text="SEC", font=("Helvetica", 35), bg_color="white", fg_color="white", text_color="Black")
        self.sec_label.grid(row=1, column=0, sticky="nsew", pady=0, padx=0)
        
        self.sec_label2 = customtkinter.CTkLabel(master=self.seconds_frame, width=20, text="0", font=("Helvetica", 40), bg_color="white", fg_color="white", text_color="Black")
        self.sec_label2.grid(row=1, column=1, sticky="nsew", pady=0, padx=0)
        
        self.down1im = customtkinter.CTkImage(Image.open("images/down2.png"), size=(90,100))
        self.button_down1 = customtkinter.CTkButton(master=self.seconds_frame, image=self.down1im, command=self.down_arrow, text="", fg_color="white", bg_color="white", text_color="white", hover_color="white", width=70)
        self.button_down1.grid(row=2, column=1, sticky="nsew", pady=0, padx=0)

        self.content_frame = customtkinter.CTkFrame(master=self, bg_color="white", fg_color="white")
        self.content_frame.grid(row=2, column=0, sticky="nsew", pady=0, padx=0, rowspan=10)

        self.radio1 = CheckBox(master=self.content_frame, text="1", value="1", size=125, font_size=30, command=self.select_all.deselect)
        self.radio1.grid(row=0, column=0, sticky="nsew", pady=0, padx=40)

        self.radio2 = CheckBox(master=self.content_frame, text="2", value="1", size=125, font_size=30, command=self.select_all.deselect)
        self.radio2.grid(row=1, column=0, sticky="nsew", pady=0, padx=40)

        self.radio3 = CheckBox(master=self.content_frame, text="3", value="1", size=125, font_size=30, command=self.select_all.deselect)
        self.radio3.grid(row=2, column=0, sticky="nsew", pady=0, padx=40)

        self.radio4 = CheckBox(master=self.content_frame, text="4", value="1", size=125, font_size=30, command=self.select_all.deselect)
        self.radio4.grid(row=3, column=0, sticky="nsew", pady=0, padx=40)

        self.radio5 = CheckBox(master=self.content_frame, text="5", value="1", size=125, font_size=30, command=self.select_all.deselect)
        self.radio5.grid(row=4, column=0, sticky="nsew", pady=0, padx=40)

        self.radio6 = CheckBox(master=self.content_frame, text="6", value="1", size=125, font_size=30, command=self.select_all.deselect)
        self.radio6.grid(row=0, column=1, sticky="nsew", pady=0, padx=200)

        self.radio7 = CheckBox(master=self.content_frame, text="7", value="1", size=125, font_size=30, command=self.select_all.deselect)
        self.radio7.grid(row=1, column=1, sticky="nsew", pady=0, padx=200)

        self.radio8 = CheckBox(master=self.content_frame, text="8", value="1", size=125, font_size=30, command=self.select_all.deselect)
        self.radio8.grid(row=2, column=1, sticky="nsew", pady=0, padx=200)

        self.radio9 = CheckBox(master=self.content_frame, text="9", value="1", size=125, font_size=30, command=self.select_all.deselect)
        self.radio9.grid(row=3, column=1, sticky="nsew", pady=0, padx=200)

        self.radio10 = CheckBox(master=self.content_frame, text="10", value="1", size=125, font_size=30, command=self.select_all.deselect)
        self.radio10.grid(row=4, column=1, sticky="nsew", pady=0, padx=200)

        self.radio11 = CheckBox(master=self.content_frame, text="11", value="1", size=125, font_size=30, command=self.select_all.deselect)
        self.radio11.grid(row=0, column=2, sticky="nsew", pady=0, padx=40)

        self.radio12 = CheckBox(master=self.content_frame, text="12", value="1", size=125, font_size=30, command=self.select_all.deselect)
        self.radio12.grid(row=1, column=2, sticky="nsew", pady=0, padx=40)

        self.radio13 = CheckBox(master=self.content_frame, text="13", value="1", size=125, font_size=30, command=self.select_all.deselect)
        self.radio13.grid(row=2, column=2, sticky="nsew", pady=0, padx=40)


        # add a rounded button for save profile
        self.button_BACK = customtkinter.CTkButton(master=self.content_frame, command=self.stop_loop, text="BACK", font=("Helvetica", 35), bg_color="white", fg_color="light BLUE", text_color="BLACK", hover_color="light BLUE",  width=250, height=80)
        self.button_BACK.grid(row=5, column=1, sticky="nsew", pady=20, padx=250, columnspan=2)

        # self.start_button = customtkinter.CTkButton(master=self, text="Start", font=("Helvetica", 20), command=self.start, fg_color="white", bg_color="white", text_color="Black", hover_color="white", width=100)
        # self.start_button.grid(row=3, column=1, sticky="nsew", pady=0, padx=100)

        # add a rounded button for save profile
        self.button_start = customtkinter.CTkButton(master=self, command=self.run_profile, text="START", font=("Helvetica", 35), bg_color="white", fg_color="light green", text_color="green", hover_color="light green",  width=300, height=80)
        self.button_start.grid(row=4, column=1, sticky="nsew", pady=50, padx=60)

        # add a rounded button for save profile
        self.button_save = customtkinter.CTkButton(master=self, command=self.stop_loop, text="STOP", font=("Helvetica", 35), bg_color="white", fg_color="light pink", text_color="RED", hover_color="light PINK",  width=300, height=80)
        self.button_save.grid(row=5, column=1, sticky="nsew", pady=20, padx=60)

    def select_all_on(self):
        self.radio1.select()
        self.radio2.select()
        self.radio3.select()
        self.radio4.select()
        self.radio5.select()
        self.radio6.select()
        self.radio7.select()
        self.radio8.select()
        self.radio9.select()
        self.radio10.select()
        self.radio11.select()
        self.radio12.select()
        self.radio13.select()

    def start(self):
        print("start")

    def up_arrow(self):
        self.seconds += 1
        self.sec_label2.configure(text=self.seconds)

    def down_arrow(self):
        if self.seconds > 0:
            self.seconds -= 1
            self.sec_label2.configure(text=self.seconds)

    def select_all(self):
        print("select all")

    def back(self):
        self.start_app()

        
    def stop(self):
        self.should_run = False
    
    def show_frame(self):
        self.controller.show_frame("running")
        # self.after(5000, )
        
    
    def passEvent(self):
        self.controller.show_frame("home")
    

    def run_loop(self):
        while self.should_run:
            for i in range(len(self.station_List)):
                if self.station_List[i] > 0:
                    # print("station_ "+str(i+1)+" is running")
                    GPIO.output(self.stationList[i], GPIO.LOW)
                    # print(self.station_List[i])
                    self.station_List[i] -= 0.25
                    if self.station_List[i] <= 0:
                        GPIO.output(self.stationList[i], GPIO.HIGH)
                else:
                    GPIO.output(self.stationList[i], GPIO.HIGH)
            
            print(self.station_List)
            if not any(self.station_List):
                break
            time.sleep(0.25)
        
        for i in range(len(self.stationList)):
            GPIO.output(self.stationList[i], GPIO.HIGH)

    def start_loop(self):
        import threading 
        self.should_run = True
        loop_thread = threading.Thread(target=self.run_loop)
        loop_thread.start()

    def stop_loop(self):
        self.should_run = False
        
        self.passEvent()
        
    def run_profile(self):
        # init list with pin numbers
        station1=10
        station2=9
        station3=11
        station4=0
        station5=5
        station6=6
        station7=13
        station8=19
        station9=26
        station10=12
        station11=16
        station12=20
        station13=21
        station14=22

        GPIO.setup(station1, GPIO.OUT)
        GPIO.setup(station2, GPIO.OUT)
        GPIO.setup(station3, GPIO.OUT)
        GPIO.setup(station4, GPIO.OUT)
        GPIO.setup(station5, GPIO.OUT)
        GPIO.setup(station6, GPIO.OUT)
        GPIO.setup(station7, GPIO.OUT)
        GPIO.setup(station8, GPIO.OUT)
        GPIO.setup(station9, GPIO.OUT)
        GPIO.setup(station10, GPIO.OUT)
        GPIO.setup(station11, GPIO.OUT)
        GPIO.setup(station12, GPIO.OUT)
        GPIO.setup(station13, GPIO.OUT)
        GPIO.setup(station14, GPIO.OUT)
        
        self.stationList = [station1,station2,station3,station4,station5,station6,station7,station8,station9,station10,station11,station12,station13, station14]

        # enabled stations list from checkboxes
        self.enabledStations = [self.radio1.get_state(), self.radio2.get_state(), self.radio3.get_state(), self.radio4.get_state(), self.radio5.get_state(), self.radio6.get_state(), self.radio7.get_state(), self.radio8.get_state(), self.radio9.get_state(), self.radio10.get_state(), self.radio11.get_state(), self.radio12.get_state(), self.radio13.get_state(), True]

        # loop through pins and set mode and state to 'low'

        for i in self.stationList:
            GPIO.setup(i, GPIO.OUT)
            GPIO.output(i, GPIO.HIGH)
        
        
        self.station_List = []
        for i in range(len(self.stationList)):
            if not self.enabledStations[i]:
                self.station_List.append(0)
            else:
                self.station_List.append(self.seconds)
        self.start_loop()


# if __name__ == "__main__":
#     root = customtkinter.CTk()
#     root.geometry("1024x700")
#     root.title("Clean/Prime")
#     root.resizable(False, False)
#     root.configure(bg_color="white")
#     root.configure(fg_color="white")
#     root.grid_columnconfigure(0, weight=1)
#     root.grid_rowconfigure(0, weight=1)
#     app = Clean(root, root)
#     app.grid(row=0, column=0, sticky="nsew")
#     root.mainloop()
#     print("hello")