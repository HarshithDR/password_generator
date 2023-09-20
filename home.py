import customtkinter as ctk
import tkinter as tk

# creating howe window
home_Window = ctk.CTk()
home_Window.title('Password generator')
home_Window.geometry('600x400')

# ctk.set_appearance_mode('dark')

menu_frame = ctk.CTkFrame(home_Window)
menu_frame.pack(side = ctk.TOP)
menu_frame.pack_propagate(False)
menu_frame.configure(height=50)

button = ctk.CTkButton(menu_frame,text = '☰')
button.pack(side = ctk.LEFT)

#creating home screen frame
home_frame = ctk.CTkFrame(master=home_Window, corner_radius=20)
home_frame.pack(pady = 20,padx=20, fill = "both", expand=True)



home_Window.mainloop()


