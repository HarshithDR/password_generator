import customtkinter as ctk
import tkinter as tk

class Gp_test:
    def __init__(self, window, show_home_test_callback_fun):

        #extracting password from the main object
        self.gp_password = ""
        self.window = window
        self.show_home_test_callback_fun = show_home_test_callback_fun

        #creating gp frame
        self.gp_test_frame = ctk.CTkFrame(master=window, corner_radius=20, pady=20, padx=20, fill="both", expand=True)

        #creating label
        self,label = ctk.CTkLabel(master=self.gp_test_frame,
                             text="Enter the keys to generate password",
                             font=('TkHeadingFont', 15, "bold"),
                             pady=10,
                             text_color='#FF7900')

        #creating label for showing password
        self.gp_label = tk.Label(self.gp_test_frame, text="")


    def onBack(self):
        self.gp_test_frame.pack_forget()
        self.show_home_test_callback_fun()
