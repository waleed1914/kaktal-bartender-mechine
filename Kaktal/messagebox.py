import tkinter as tk
import customtkinter

class CustomMessageBox:
    def __init__(self, root, command=None, message="Are you sure you want to shutdown?"):
        self.root = root
        self.top = tk.Toplevel(self.root)
        self.top.geometry("500x200+720+400")
        self.top.overrideredirect(True)
        self.top.title("Confirmation")
        self.top.configure(bg='#4f81bd')
        # self.top.grab_set()
        self.command = command
        
        self.msg = tk.Message(self.top, text=message, bg='#4f81bd', fg='black', font=('Helvetica', 20), width=400)
        self.msg.pack(pady=20)

        self.yes_button = customtkinter.CTkButton(self.top, text="Yes", text_color="black", font=("Helvetica", 22), bg_color='#4f81bd', fg_color="#00B050", hover_color="#00B050", command=lambda: self.on_yes(), height=40)
        self.yes_button.pack(side='left', padx=10, pady=10)

        self.no_button = customtkinter.CTkButton(self.top, text="No", text_color="black", font=("Helvetica", 22), bg_color='#4f81bd', fg_color="#FF0000", hover_color="#FF0000", command=lambda: self.on_no(), height=40)
        self.no_button.pack(side='right', padx=10, pady=10)

        self.bring_to_top()

    def on_yes(self):
        print("Yes button clicked")
        # self.top.grab_release()
        self.top.destroy()
        
        if self.command:
            self.command()

    def on_no(self):
        print("No button clicked")
        # self.top.grab_release()
        self.top.destroy()
        
    def bring_to_top(self):
        self.top.attributes("-topmost", True)
        self.top.update()
        self.top.attributes("-topmost", False)

# def shutdown():
#     import time
#     for i in range(10):
#         print(i)
#         time.sleep(1)

# root = tk.Tk()
# CustomMessageBox(root, command=shutdown)
# root.mainloop()
