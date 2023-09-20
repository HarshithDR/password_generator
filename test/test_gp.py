import customtkinter as ctk
import tkinter as tk
import encryptor

def generatedPassword():
    home_Window = ctk.CTk()
    home_Window.title('Password generator')
    home_Window.geometry('600x400')

    ctk.set_appearance_mode('dark')

    home_Window.mainloop()

generatedPassword()