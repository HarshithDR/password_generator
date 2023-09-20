
import customtkinter as ctk
import tkinter as tk
from tkinter import ttk

def switch_event():
    print("switch toggled, current value:", switch_var.get())

# window
window = ctk.CTk()
window.title('test')
window.geometry('600x400')

ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('blue')

#widgets
string_var = tk.StringVar(value= 'a custom string')
label = ctk.CTkLabel(
    window,
    text = 'Label',
    text_color = 'red',
    fg_color = 'white',
    corner_radius = 12,
    textvariable = string_var)
label.pack()

#button
button = ctk.CTkButton(window,
                       text = 'click here',
                       fg_color="#DB3E39",
                       hover_color= "#821D1A",
                       # command = lambda: print('button pressed')) #command can accept any command or can call function
                       command= lambda: ctk.set_appearance_mode('light'))
button.pack()

# #frame
frame = ctk.CTkFrame(window, fg_color= 'transparent')
frame.pack()

slider = ctk.CTkSlider(frame)
slider.pack(padx = 20, pady = 20)

switch_var = ctk.StringVar(value="on")
switch = ctk.CTkSwitch(window, text="Excercise Switch", command=switch_event, corner_radius= 34, switch_height= 23,
                                 variable=switch_var, onvalue="on", offvalue="off")
switch.pack()

#excercise
sw = ctk.CTkSwitch(window, text = 'excersice switch', )
sw.pack()

def radiobutton_event():
    print("radiobutton toggled, current value:", radio_var.get())

radio_var = tk.IntVar(value=0)
radiobutton_1 = ctk.CTkRadioButton(window, text="CTkRadioButton 1",
                                             command=radiobutton_event, variable= radio_var, value=1)
radiobutton_2 = ctk.CTkRadioButton(window, text="CTkRadioButton 2",
                                             command=radiobutton_event, variable= radio_var, value=2)
radiobutton_2.pack()


#run
window.mainloop()



# https://www.youtube.com/watch?v=vVRrOi5LGSo
# menu bar animation
#https://github.com/clear-code-projects/tkinter-complete/blob/main/3%20style/3_8_animated_widgets.py