import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog

class gui:
    def __init__(self):
        self.window =tk.Tk()
        self.window.title('Python File Reader/Writer')

        self.words =[]
        self.words_file ="words.txt"

        self.read_button =tk.Button(self.window, text ='Read', command =self.read_from_file)
        self.read_button.pack(side ='left')

        self.write_button =tk.Button(self.window, text ='Write', command =self.write_to_file)
        self.write_button.pack(side ='left')

        self.quit_button =tk.Button(self.window, text ='Quit', command =self.window.quit)
        self.quit_button.pack(side ='left')
        
        self.window.mainloop()

    def read_from_file(self):
        try:
            with open(self.words_file, 'r') as f:
                words =f.read().split()
                longest_word =max(words, key =len)
                avg_word_length =round(sum(len(word) for word in words) /len(words))

                messagebox.showinfo('Read File',
                                    f'File contains {len(words)} words.\nLongest word is: {longest_word}.\nAverage word length is: {avg_word_length}')
        except FileNotFoundError:
            messagebox.showinfo('Read File', 'No data to read. Please write to file first.')

    def write_to_file(self):
        num_words =simpledialog.askinteger('Write to File', 'How many words would you like to add?')

        for i in range(num_words):
            word =simpledialog.askstring('Write to File', f'Enter word no.{i +1}')
            self.words.append(word)

        with open(self.words_file, 'w') as f:
            f.write(' '.join(self.words))

        messagebox.showinfo('Write to File', 'Words written to file.')

gui()