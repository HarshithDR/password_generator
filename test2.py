import customtkinter as ctk
import tkinter as tk


def onSubmit():
    text1 = entry_1.get()
    text2 = entry_2.get()
    text3 = entry_3.get()

    # Display the entered text
    result_label.configure(text=f"You entered: {text1}, {text2}, {text3}")
    # print(text3)

# creating howe window
home_Window = ctk.CTk()
home_Window.title('Password generator')
home_Window.geometry('600x400')

ctk.set_appearance_mode('dark')

#creating home screen frame
home_frame = ctk.CTkFrame(master=home_Window, corner_radius=20)
home_frame.pack(pady = 20,padx=20, fill = "both", expand=True)

#creating label
label = ctk.CTkLabel(master= home_frame,
                     text="Enter the keys to generate password",
                     font= ('TkHeadingFont',15,"bold"),
                     pady = 10,
                     text_color= '#FF7900')
label.pack()

#creating input area
entry_1 = ctk.CTkEntry(home_frame, placeholder_text="key 1")
entry_2 = ctk.CTkEntry(home_frame, placeholder_text="key 2")
entry_3 = ctk.CTkEntry(home_frame, placeholder_text="key 3")

entry_1.pack(padx = 30,pady = 10)
entry_2.pack(padx = 10,pady = 10)
entry_3.pack(padx = 20,pady = 10)

# Create a Submit button
submit_button = ctk.CTkButton(home_frame, text="Submit", command=onSubmit)
submit_button.pack()

# Create a label to display the result
result_label = ctk.CTkLabel(home_frame, text="")
result_label.pack()



home_Window.mainloop()




