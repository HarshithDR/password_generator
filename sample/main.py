import customtkinter as ctk
from home_page import Home_test
from gp_page import Gp_test

class App:
    def __init__(self, window):

        self.window = window
        self.window.title('Password generator')
        self.window.geometry('600x400')

        self.home_test_obj = Home_test(self.window, self.show_gp_test_fun)

        self.gp_test_obj = Gp_test(self.window, self.show_home_test_fun)

        #running home page
        self.show_home_test_fun()

    def show_home_test_fun(self):
        self.gp_test_obj.gp_test_frame.pack_forget()

        self.home_test_obj.home_test_frame.pack(pady=20,
                                            padx=20,
                                            fill="both",
                                            expand=True)

    def show_gp_test_fun(self, password=''):
        self.home_test_obj.home_test_frame.pack_forget()

        self.gp_test_obj.gp_label.configure(text = password)

        self.gp_test_obj.gp_password = password

        self.gp_test_obj.gp_test_frame.pack(pady=20,
                                            padx=20,
                                            fill="both",
                                            expand=True)

if __name__ == "__main__":
    ctk.set_appearance_mode('dark')
    window = ctk.CTk()
    app = App(window)
    window.mainloop()
