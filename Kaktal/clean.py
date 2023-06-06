import time
import customtkinter
from PIL import Image, ImageTk 
from datetime import date

import RPi.GPIO as GPIO



customtkinter.set_appearance_mode("light")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

 
class Clean(customtkinter.CTkFrame):

    WIDTH = 1280
    HEIGHT = 720

    def __init__(self, master, controller):
        super().__init__(master)
        self.controller = controller
        self.should_run = True
        # ============ create frame for top ============

        self.grid_columnconfigure(0, weight=1)
        # self.grid_rowconfigure(0, weight=1)

        # make the background white
        self.configure(bg_color="white")
        self.configure(fg_color="white")

        # self.logo = ImageTk.PhotoImage(Image.open("images/logo_big.png"))
        # self.label_logo = customtkinter.CTkLabel(master=self, image=self.logo)
        # self.label_logo.grid(row=0, column=0, sticky="nsew")

        # add a label to the frame
        self.label = customtkinter.CTkLabel(master=self, text="CLEANING", font=("Helvetica", 35), bg_color="white", fg_color="white", text_color="black")
        self.label.grid(row=0, column=0, sticky="nsew", pady=20)

        # add a label to the frame
        self.label = customtkinter.CTkLabel(master=self, text="Install the pump heads to be cleaned onto your cleaning \nbottles.Fill your cleaning bottles with mild cleaning solution.\n\n When you press CLEAN below, All Dispensing Heads will \nenergize for 10 seconds. Perform cleaning evolutions as many \ntimes as desired.  Refill your cleaning bottles with fresh water \nand repeat multiple times to rinse the tubing clean.", anchor="center", font=("Helvetica", 22), bg_color="white", fg_color="white", text_color="black")
        self.label.grid(row=1, column=0, sticky="nsew", pady=50)

        # add a label to the frame
        self.label = customtkinter.CTkLabel(master=self, text="NOTE: PUT WASTE WATER COLLECTION CUP UNDER \nDISPENSING NOZZLES BEFORE CLEANING!", anchor="center", font=("Helvetica", 22), bg_color="white", fg_color="white", text_color="red")
        self.label.grid(row=2, column=0, sticky="nsew", pady=20)

        # add a rounded button for stopping profile
        self.button_container = customtkinter.CTkFrame(master=self, bg_color="white", fg_color="white")
        self.button_container.grid(row=3, column=0, sticky="nsew", pady=0, padx=25)

        # add a label to the frame
        # self.label = customtkinter.CTkLabel(master=self.button_container, text="", font=("Helvetica", 20), bg_color="white", fg_color="white", text_color="white")
        # self.label.grid(row=2, column=0, sticky="nsew", pady=0, padx=50)

        self.button_save = customtkinter.CTkButton(master=self.button_container, command=self.run_profile, text="START", font=("Helvetica", 20), bg_color="white", fg_color="light green", text_color="black", hover_color="light green",  width=250, height=70)
        self.button_save.grid(row=2, column=1, sticky="ew", pady=0, padx=30)

        self.button_save = customtkinter.CTkButton(master=self.button_container, command=self.stop_loop, text="STOP", font=("Helvetica", 20), bg_color="white", fg_color="light pink", text_color="black", hover_color="light pink",  width=250, height=70)
        self.button_save.grid(row=2, column=2, sticky="ew", pady=0, padx=50)

        self.button_save = customtkinter.CTkButton(master=self.button_container, command=self.stop_loop, text="RETURN\n TO  MENU", font=("Helvetica", 20), bg_color="white", fg_color="light blue", text_color="black", hover_color="light blue",  width=250, height=70)
        self.button_save.grid(row=2, column=3, sticky="ew", pady=0, padx=30)



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

    def start_loop(self):
        import threading 
        self.should_run = True
        loop_thread = threading.Thread(target=self.run_loop)
        loop_thread.start()

    def stop_loop(self):
        self.should_run = False
        
        self.passEvent()
        
    def run_profile(self):
        # self.profile = profile
        # print("Running profile: " + str(self.profile))
        # import pickle
        # with open('records.pickle', 'rb') as f:
        #     self.records = pickle.load(f)
        # self.should_run = True
        # record = self.records[self.profile]
        # print(record)
        # print("showing frame")
        # self.show_frame()
        # print("starting timer")

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

        # loop through pins and set mode and state to 'low'

        for i in self.stationList:
            GPIO.setup(i, GPIO.OUT)
            GPIO.output(i, GPIO.HIGH)
        
        
        self.station_List = [10 for i in range(len(self.stationList))]

        
        self.start_loop()
