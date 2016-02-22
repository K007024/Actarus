# coding: utf-8

import Tkinter as Tk
import tkFileDialog

import os
import win32com.client as com

class ViewDirControl(Tk.Frame):

    def __init__(self, parent, title):
        Tk.Frame.__init__(self, parent)
        self.parent = parent
        self.title = title
        self.build()

    def build(self):
        self.grid()
        self.lbTitle = Tk.Label(self, text=self.title).grid(column=0, row=0, sticky='EW')
        self.txtPath = Tk.StringVar()
        self.entry = Tk.Entry(self, textvariable=self.txtPath).grid(column=1, row=0, sticky='EW')
        self.btn = Tk.Button(self, text='Open', command=self.open).grid(column=2, row=0, sticky='EW')

        self.lbSize = Tk.Label(self, text='0 go')
        self.lbSize.grid(column=3, row=0, sticky='EW')

    def open(self):
        dirPath = tkFileDialog.askdirectory()
        if dirPath:
            self.txtPath.set(dirPath)
            self.lbSize.config(text='{:<10.2f} go'.format(self.get_size_fast(dirPath)/(1024*1024*1024.0)))

    def get_size(self, start_path):
        total_size = 0
        for dirpath, dirnames, filenames in os.walk(start_path):
            for f in filenames:
                fp = os.path.join(dirpath, f)
                total_size += os.path.getsize(fp)
        return total_size

    def get_size_fast(self, start_path):
        fso = com.Dispatch("Scripting.FileSystemObject")
        folder = fso.GetFolder(start_path)
        return folder.Size

if __name__ == '__main__':
    root = ViewDirControl(None, "This")
    root.title = 'That'
    root.mainloop()