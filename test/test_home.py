import customtkinter as ctk
import tkinter as tk
import encryptor

if __name__ == '__main__':
    #creating submit function
    def onSubmit():
        text1 = entry_1.get()
        text2 = entry_2.get()
        text3 = entry_3.get()
        password = encryptor.encrypt_string(text1+text2+text3)
        print()
        # Display the entered text
        result_label.config(text=f"generated password is:{password}")


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

    entry_1.pack(padx = 30, pady = 10)
    entry_2.pack(padx = 10, pady = 10)
    entry_3.pack(padx = 20, pady = 10)

    # Create a Submit button
    submit_button = ctk.CTkButton(home_frame, text="Submit", command=onSubmit)
    submit_button.pack(pady = 10)

    # def checkbox_event():
    #     print("checkbox toggled, current value:", check_var.get())
    #
    # check_var = customtkinter.StringVar(value="on")
    # checkbox = customtkinter.CTkCheckBox(app, text="CTkCheckBox", command=checkbox_event,
    #                                      variable=check_var, onvalue="on", offvalue="off")

    # Create a label to display the result
    result_label = tk.Label(home_frame, text="")
    result_label.pack()



    home_Window.mainloop()


