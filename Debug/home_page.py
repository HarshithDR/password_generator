import customtkinter as ctk
import encryptor

class MenuPanel(ctk.CTkFrame):
    def __init__(self,parent,start_pos,end_pos):
        super().__init__(master=parent)
        # general attributes
        self.start_pos = start_pos
        self.end_pos = end_pos
        self.height = abs(start_pos - end_pos)

        # animation logic
        self.pos = self.start_pos
        self.in_start_pos = True


        # layout
        self.place(relx=0.05, rely=self.start_pos,relwidth = 0.2,relheight = self.height)

    def animate(self):
        print(self.in_start_pos)
        if self.in_start_pos:
            self.animate_forward()
        else:
            self.animate_backwards()

    def animate_forward(self):
        if self.pos > self.end_pos:
            self.pos += 0.008
            self.place(relx=0.05, rely=self.pos,relwidth = 0.2,relheight = self.height)
            self.after(10, self.animate_forward)
        else:
            self.in_start_pos = False

    def animate_backwards(self):
        if self.pos < self.start_pos:
            self.pos -= 0.008
            self.place(relx=0.05, rely=self.pos, relwidth=0.2,relheight = self.height)
            self.after(10, self.animate_backwards)
        else:
            self.in_start_pos = True



class Home_test:
    def __init__(self, window, show_gp_test_callback_fun):
        self.window = window
        self.show_gp_test_callback_fun = show_gp_test_callback_fun

        # creating home screen frame
        self.home_test_frame = ctk.CTkFrame(master=window,
                                            corner_radius=20)




        #97888888888888888888888888888888
        self.animateMenu = MenuPanel(self.home_test_frame,1.0, 0.7)
        self.menu = ctk.CTkButton(self.home_test_frame,text = 'menu', command= self.animateMenu.animate).pack()

        #34-098562=====-0







        # creating label
        self.home_label = ctk.CTkLabel(master=self.home_test_frame,
                                       text="Enter the keys to generate password",
                                       font=('TkHeadingFont', 15, "bold"),
                                       pady=10,
                                       text_color='#FF7900')

        # creating input area
        self.entry_1 = ctk.CTkEntry(self.home_test_frame, placeholder_text="Master Key", show = '*')
        self.entry_2 = ctk.CTkEntry(self.home_test_frame, placeholder_text="Number", show = '*')
        self.entry_3 = ctk.CTkEntry(self.home_test_frame, placeholder_text="Application", show = '*')

        # Show/Hide password button
        self.password_visible = False
        self.toggle_password_button = ctk.CTkButton(self.home_test_frame,
                                                    text = "Show Password",
                                                    command= self.toggle_password_visibility)

        # checkboxes to include uppercase and special characters
        self.check_Uppercase = ctk.StringVar(value="on")
        self.checkbox_upper = ctk.CTkCheckBox(self.home_test_frame,
                                              text="Include Uppercase",
                                              variable=self.check_Uppercase,
                                              onvalue="on",
                                              offvalue="off")

        self.check_special_characters = ctk.StringVar(value="on")
        self.checkbox_special = ctk.CTkCheckBox(self.home_test_frame,
                                                text="Include Special Case",
                                                variable=self.check_special_characters,
                                                onvalue="on",
                                                offvalue="off")

        # Create a Submit button
        self.submit_button = ctk.CTkButton(self.home_test_frame,
                                           text="Submit",
                                           command=self.onSubmit)

        # packing everything
        self.home_label.pack()
        self.entry_1.pack(padx=30, pady=10)
        self.entry_2.pack(padx=10, pady=10)
        self.entry_3.pack(padx=20, pady=10)
        self.toggle_password_button.pack(pady=10)
        self.checkbox_upper.pack(pady=10)
        self.checkbox_special.pack(pady=10)
        self.submit_button.pack(pady=10)

    def toggle_password_visibility(self):
        self.password_visible = not self.password_visible
        show_char = '' if self.password_visible else '•'
        self.entry_1.configure(show = show_char)
        self.entry_2.configure(show = show_char)
        self.entry_3.configure(show = show_char)
        self.toggle_password_button.configure(text = "Hide Password" if self.password_visible else "Show Password")

    def generatePassword(self):
        self.key1 = self.entry_1.get()
        self.key2 = self.entry_2.get()
        self.key3 = self.entry_3.get()

        self.password = encryptor.encrypt_string(self.key1 + self.key2 + self.key3)[7:23]
        # print(self.password)

        if self.checkbox_upper.get() == 'on':
            self.password = self.password + 'A'

        if self.checkbox_special.get() == 'on':
            self.password = self.password + '@'

        return self.password

    def onSubmit(self):
        self.genpassword = self.generatePassword()
        self.home_test_frame.pack_forget()
        self.show_gp_test_callback_fun(self.genpassword)
