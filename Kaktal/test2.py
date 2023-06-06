import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.withdraw()

answer = messagebox.askyesnocancel("Title", "Do you want to continue?")

if answer == True:
    print("Yes")
elif answer == False:
    print("No")
else:
    print("Cancel")