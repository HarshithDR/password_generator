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
        self.gp_page_label = ctk.CTkLabel(master=self.gp_test_frame,
                                  text="Generated Password",
                                  font=('TkHeadingFont', 15, "bold"),
                                  pady=10,
                                  text_color='#FF7900')

        #creating label for showing password
        self.gp_label = ctk.CTkLabel(self.gp_test_frame,
                                 text=self.gp_password,
                                 bg_color = '#003049',
                                 corner_radius = 20,
                                 text_color = '#FFFFFF')

        self.cpButton = ctk.CTkButton(self.gp_test_frame,
                                      text = 'Copy',
                                      command= self.copyClipboard)

        self.backButton = ctk.CTkButton(self.gp_test_frame,
                                        text = 'Back',
                                        command=self.onBack)

        self.copy_label = ctk.CTkLabel(self.gp_test_frame, text="")


        #packing objects
        self.gp_page_label.pack(pady = 10, anchor = 'center')
        self.gp_label.pack(pady = 10, anchor = 'center')
        self.copy_label.pack(pady = 10, anchor = 'center')
        self.cpButton.pack(pady = 10, anchor = 'center')
        self.backButton.pack(pady = 10, anchor = 'center')



    def copyClipboard(self):
        pc.copy(self.gp_password)
        # print(self.gp_password)
        self.copy_label.configure(text = 'copied')


    def onBack(self):
        self.gp_test_frame.pack_forget()
        self.copy_label.configure(text = '')
        self.show_home_test_callback_fun()

