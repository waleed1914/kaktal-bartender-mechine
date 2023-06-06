import customtkinter
from clean2 import Clean
from shutdown import Shutdown
from splash import Splash
from running import Running
from edit import Edit
from new import Add
from home import Home
from test import Test
import RPi.GPIO as GPIO
# import time


class Controller():
    def __init__(self):
        main = customtkinter.CTk()
        main.geometry("1920x1080")
        main.config(bg="white")
        # main.resizable(False, False)
        main.attributes("-fullscreen", True)
        container = customtkinter.CTkFrame(main)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
                    

        running = Running(container, self)
        edit = Edit(container, self)
        add = Add(container, self)
        test = Test(container, self)
        clean = Clean(container, self)
        shutdown = Shutdown(container, self)
        splash = Splash(container, self)

        self.frames = {
            "home": test,
            "running": running,
            "edit": edit,
            "add": add,
            "test": test,
            "clean": clean,
            "shutdown": shutdown,
            "splash": splash
        }


        GPIO.setmode(GPIO.BCM)

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
        stationList = [station1,station2,station3,station4,station5,station6,station7,station8,station9,station10,station11,station12,station13, station14]

        # loop through pins and set mode and state to 'low'

        for i in stationList:
            GPIO.setup(i, GPIO.OUT)
            GPIO.output(i, GPIO.HIGH)

        container.rowconfigure(0, weight=1)
        container.columnconfigure(0, weight=1)
        
        for frame in self.frames.values():
                frame.grid(row=0, column=0, sticky="nsew")
            

        self.show_frame("splash")
        main.mainloop()
    
    def get_frames(self):
        return self.frames


    def show_frame(self, frame_name):
        self.next_frame = self.frames[frame_name]
        self.next_frame.update()
        if frame_name == "home":
            self.next_frame.add_ui()
        self.next_frame.tkraise()


if __name__ == "__main__":
    Controller()