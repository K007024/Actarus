# coding: utf-8

import Tkinter as Tk
import viewDirControl

class ViewMain(Tk.Tk):

    def __init__(self, parent):
        Tk.Tk.__init__(self, parent)
        self.parent = parent
        self.build()

    def build(self):
        self.grid()
        self.src = viewDirControl.ViewDirControl(self, "Source").grid(column=0, row=0, columnspan=2, sticky='E')
        self.dst = viewDirControl.ViewDirControl(self, "Destination").grid(column=0, row=1, columnspan=2, sticky='E')

        self.btnCalc = Tk.Button(self, text="Check HDD Capacity").grid(column=0, row=2, sticky='W')
        self.btnGo = Tk.Button(self, text="Goldorak").grid(column=1, row=2, sticky='E')

if __name__ == '__main__' :
    root = ViewMain(None)
    root.title = 'That'
    root.mainloop()