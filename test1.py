
import customtkinter as ctk

# window
window = ctk.CTk()
window.title('password manager')
window.geometry('600x400')

#widgets
label = ctk.CTkLabel(
    window,
    text = 'Label',
    text_color = 'red',
    fg_color = 'white',
    corner_radius = 12)
label.pack()

#button
button = ctk.CTkButton(window,
                       text = 'click here',
                       fg_color="#DB3E39",
                       hover_color= "#821D1A",
                       command = lambda: print('button pressed'))
button.pack()

#run
window.mainloop()
