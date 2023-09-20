import tkinter as tk
from page1 import Page1
from page2 import Page2

class MultiPageApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry('400x300')

        self.page1 = Page1(self.root, self.show_page2)
        self.page2 = Page2(self.root, self.show_page1)

        self.show_page1()

    def show_page1(self):
        self.page2.page2.pack_forget()
        self.page1.page1.pack()

    def show_page2(self):
        self.page1.page1.pack_forget()
        self.page2.page2.pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = MultiPageApp(root)
    root.mainloop()
