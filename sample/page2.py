import tkinter as tk

class Page2:
    def __init__(self, root, show_page1_callback):
        self.root = root
        self.show_page1_callback = show_page1_callback

        self.page2 = tk.Frame(self.root, bg='green')
        self.label2 = tk.Label(self.page2, text='Page 2', font=('Helvetica', 12))
        self.button2 = tk.Button(self.page2, text='Previous Page', command=self.show_page1)

        self.label2.pack(pady=10)
        self.button2.pack(pady=20)

    def show_page1(self):
        self.page2.pack_forget()
        self.show_page1_callback()
