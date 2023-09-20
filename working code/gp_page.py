import customtkinter as ctk
import pyperclip as pc

class Gp_test:
    def __init__(self, window, show_home_test_callback_fun):
        #extracting password from the main object
        self.gp_password = ""
        self.window = window
        self.show_home_test_callback_fun = show_home_test_callback_fun

        #creating gp frame
        self.gp_test_frame = ctk.CTkFrame(master=window,
                                          corner_radius=20)

        #creating label
        self.label = ctk.CTkLabel(master=self.gp_test_frame,
                                  corner_radius=12,
                                  text="Generated Password",
                                  font=('TkHeadingFont', 15, "bold"),
                                  pady=10,
                                  text_color='#FF7900')

        #creating label for showing password
        self.gp_label = ctk.CTkLabel(self.gp_test_frame,
                                 text=self.gp_password,
                                 bg_color = '#FF7900',
                                 corner_radius = 10,
                                 text_color = '#FFFFFF')

        self.cpButton = ctk.CTkButton(self.gp_test_frame,
                                      text = 'Copy',
                                      command= self.copyClipboard)

        self.backButton = ctk.CTkButton(self.gp_test_frame,
                                        text = 'Back',
                                        command=self.onBack)

        self.copy_label = ctk.CTkLabel(self.gp_test_frame, text="")


        #packing objects
        self.label.pack()
        self.gp_label.pack()
        self.copy_label.pack()
        self.cpButton.pack()
        self.backButton.pack()

    def copyClipboard(self):
        pc.copy(self.gp_password)
        # print(self.gp_password)
        self.copy_label.configure(text = 'copied')


    def onBack(self):
        self.gp_test_frame.pack_forget()
        self.copy_label.configure(text='')
        self.show_home_test_callback_fun()
