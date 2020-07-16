from tkinter import *
from backend import Database

db = Database("books.db")

class Application(object):

    def __init__(self, frame):
        self.frame = frame
        self.frame.wm_title("Library")

        l1 = Label(frame, text="Title")
        l1.grid(row=0, column=0)

        l2 = Label(frame, text="Author")
        l2.grid(row=0, column=2)

        l3 = Label(frame, text="Year")
        l3.grid(row=1, column=0)

        l4 = Label(frame, text="ISBN")
        l4.grid(row=1, column=2)

        self.title_text = StringVar()
        self.e1 = Entry(frame, textvariable=self.title_text)
        self.e1.grid(row=0, column=1)

        self.author_text = StringVar()
        self.e2 = Entry(frame, textvariable=self.author_text)
        self.e2.grid(row=0, column=3)

        self.text_year = StringVar()
        self.e3 = Entry(frame, textvariable=self.text_year)
        self.e3.grid(row=1, column=1)

        self.text_isbn = StringVar()
        self.e4 = Entry(frame, textvariable=self.text_isbn)
        self.e4.grid(row=1, column=3)

        b1 = Button(frame, text="View all", width=15, command = self.view_command)
        b1.grid(row=3, column=3)

        b2 = Button(frame, text="Search entry", width=15, command = self.search_command)
        b2.grid(row=4, column=3)

        b3 = Button(frame, text="Add entry", width=15, command = self.add_command)
        b3.grid(row=5, column=3)

        b4 = Button(frame, text="Update Selected", width=15, command = self.update_command)
        b4.grid(row=6, column=3)

        b5 = Button(frame, text="Delete Selected", width=15, command = self.delete_command)
        b5.grid(row=7, column=3)

        b6 = Button(frame, text="Close", width=15, command = frame.destroy)
        b6.grid(row=8, column=3)

        self.lb = Listbox(frame, height=10, width=35)
        self.lb.grid(row=2, column=0, rowspan=10, columnspan=2)

        sb = Scrollbar(frame)
        sb.grid(row=2, column=2, rowspan=10)

        self.lb.configure(yscrollcommand = sb.set)
        sb.configure(command=self.lb.yview())

        self.lb.bind("<<ListboxSelect>>", self.get_selected_row)

    def view_command(self):
        self.lb.delete(0, END)
        for row in db.view_all():
            self.lb.insert(END, row)

    def search_command(self):
        self.lb.delete(0, END)
        for row in db.search(self.title_text.get(), self.author_text.get(), self.text_year.get(), self.text_isbn.get()):
            self.lb.insert(END, row)                    

    def add_command(self):
        db.insert(self.title_text.get(), self.author_text.get(), self.text_year.get(), self.text_isbn.get())
        self.lb.delete(0, END)
        self.lb.insert(END, (self.title_text.get(), self.author_text.get(), self.text_year.get(), self.text_isbn.get()))

    def get_selected_row(self, event):
        try:
            global selected_tuple
            index = self.lb.curselection()[0]
            selected_tuple = self.lb.get(index)
            self.e1.delete(0, END)
            self.e1.insert(0, selected_tuple[1])
            self.e2.delete(0, END)
            self.e2.insert(0, selected_tuple[2])
            self.e3.delete(0, END)
            self.e3.insert(0, selected_tuple[3])
            self.e4.delete(0, END)
            self.e4.insert(0, selected_tuple[4])
        except IndexError:
            pass

    def update_command(self):
        db.update(selected_tuple[0], self.title_text.get(), self.author_text.get(), self.text_year.get(), self.text_isbn.get())
        self.lb.delete(0,END)
        for row in db.view_all():
            self.lb.insert(END, row)

    def delete_command(self):
        db.delete(selected_tuple[0])


root = Tk(className="Library")
Application(root)
root.mainloop()