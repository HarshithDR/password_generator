import tkinter as tk


class Page1:
    def __init__(self, root, show_page2_callback):
        self.root = root
        self.show_page2_callback = show_page2_callback

        self.page1 = tk.Frame(self.root, bg='blue')
        self.label1 = tk.Label(self.page1, text='Page 1', font=('Helvetica', 12))
        self.button1 = tk.Button(self.page1, text='Next Page', command=self.show_page2)

        self.label1.pack(pady=10)
        self.button1.pack(pady=20)

    def show_page2(self):
        self.page1.pack_forget()
        self.show_page2_callback()
