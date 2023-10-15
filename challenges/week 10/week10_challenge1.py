import tkinter as tk
from tkinter import messagebox


class Book:
    def __init__(self, item_name, author, publisher, num_pages, is_ebook =False, is_hardcopy =False):
        self.item_name =item_name
        self.author =author
        self.publisher =publisher
        self.num_pages =num_pages
        self.is_ebook =is_ebook
        self.is_hardcopy =is_hardcopy

    def get_details(self):
        return self.item_name, self.author, self.publisher, self.num_pages, self.is_ebook, self.is_hardcopy


class gui:
    def __init__(self):
        self.window =tk.Tk()
        self.window.title('Book Information Entry')

        tk.Label(self.window, text ='Item Name:').grid(row =0)
        tk.Label(self.window, text ='Author:').grid(row =1)
        tk.Label(self.window, text ='Publisher:').grid(row =2)
        tk.Label(self.window, text ='Number of Pages:').grid(row =3)
        tk.Label(self.window, text ='Is eBook:').grid(row =4)
        tk.Label(self.window, text ='Is Hardcopy:').grid(row =5)

        self.e1 =tk.Entry(self.window)
        self.e2 =tk.Entry(self.window)
        self.e3 =tk.Entry(self.window)
        self.e4 =tk.Entry(self.window)
        self.e5 =tk.Entry(self.window)
        self.e6 =tk.Entry(self.window)

        self.e1.grid(row =0, column =1)
        self.e2.grid(row =1, column =1)
        self.e3.grid(row =2, column =1)
        self.e4.grid(row =3, column =1)
        self.e5.grid(row =4, column =1)
        self.e6.grid(row =5, column =1)

        tk.Button(self.window, text ='Quit', command =self.window.quit).grid(row =6, column =0, sticky =tk.W, pady =4)
        tk.Button(self.window, text ='Show', command =self.show_entry_fields).grid(row =6, column =1, sticky =tk.W, pady =4)

        self.window.mainloop()

    def show_entry_fields(self):
        is_ebook =True if self.e5.get() =='True' else False
        is_hardcopy =True if self.e6.get() =='True' else False
        book =Book(self.e1.get(), self.e2.get(), self.e3.get(), int(self.e4.get()), is_ebook, is_hardcopy)
        messagebox.showinfo('Book Information', book.get_details())

gui()