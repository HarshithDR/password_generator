import customtkinter as ctk
import encryptor

class Home_test:
    def __init__(self, window, show_gp_test_callback_fun):
        self.window = window
        self.show_gp_test_callback_fun = show_gp_test_callback_fun

        # creating home screen frame
        self.home_test_frame = ctk.CTkFrame(master=window, corner_radius=20)

        # creating input area
        self.home_label = ctk.CTkLabel(master=self.home_test_frame,
                                       text="Enter the keys to generate password",
                                       font=('TkHeadingFont', 15, "bold"),
                                       pady=10,
                                       text_color='#FF7900')

        # creating input area
        self.entry_1 = ctk.CTkEntry(self.home_test_frame, placeholder_text="Master Key", show='•')
        self.entry_2 = ctk.CTkEntry(self.home_test_frame, placeholder_text="Number", show='•')
        self.entry_3 = ctk.CTkEntry(self.home_test_frame, placeholder_text="Application", show='•')

        # checkbox to show/hide password
        self.show_password_var = ctk.StringVar(value=False)
        self.show_password_checkbox = ctk.CTkCheckBox(self.home_test_frame,
                                                      text="Show Password",
                                                      variable=self.show_password_var,
                                                      onvalue=True,
                                                      offvalue=False,
                                                      command=self.toggle_password_visibility)

        # Create a Submit button
        self.submit_button = ctk.CTkButton(self.home_test_frame,
                                           text="Submit",
                                           command=self.onSubmit)

        # packing everything
        self.home_label.pack()
        self.entry_1.pack(padx=30, pady=10)
        self.entry_2.pack(padx=10, pady=10)
        self.entry_3.pack(padx=20, pady=10)
        self.show_password_checkbox.pack(padx=10, pady=10)
        self.submit_button.pack(pady=10)

    def toggle_password_visibility(self):
        # Toggle password visibility based on checkbox state
        show_password = self.show_password_var.get()
        show_char = '' if show_password else '•'
        self.entry_1.configure(show=show_char)
        self.entry_2.configure(show=show_char)
        self.entry_3.configure(show=show_char)

    def generatePassword(self):
        self.key1 = self.entry_1.get()
        self.key2 = self.entry_2.get()
        self.key3 = self.entry_3.get()

        self.password = encryptor.encrypt_string(self.key1 + self.key2 + self.key3)[7:23]

        if self.checkbox_upper.get() == 'on':
            self.password = self.password + 'A'

        if self.checkbox_special.get() == 'on':
            self.password = self.password + '@'

        return self.password

    def onSubmit(self):
        self.genpassword = self.generatePassword()
        self.home_test_frame.pack_forget()
        self.show_gp_test_callback_fun(self.genpassword)
