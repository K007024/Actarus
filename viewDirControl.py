# coding: utf-8

import Tkinter as Tk
import tkFileDialog

class ViewDirControl(Tk.Frame):

    def __init__(self, parent, title):
        Tk.Frame.__init__(self, parent)
        self.parent = parent
        self.title = title
        self.build()

    def build(self):
        self.grid()
        self.lbTitle = Tk.Label(self, text=self.title).grid(column=0, row=0, sticky='EW')
        self.txtVar = Tk.StringVar()
        self.entry = Tk.Entry(self, textvariable=self.txtVar).grid(column=1, row=0, sticky='EW')
        self.btn = Tk.Button(self, text='Open', command=self.open).grid(column=2, row=0, sticky='EW')
        self.lbCap = Tk.Label(self, text='-1 go').grid(column=3, row=0, sticky='EW')

    def open(self):
        dirPath = tkFileDialog.askdirectory()
        if dirPath:
            self.txtVar.set(dirPath)

if __name__ == '__main__':
    root = ViewDirControl(None, "This")
    root.title = 'That'
    root.mainloop()