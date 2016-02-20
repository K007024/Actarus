# coding: utf-8

import Tkinter
import ttk

import viewDirControl

class ViewMain:

    def __init__(self):
        self.root = Tkinter.Tk()
        self.buildMain()
        self.root.mainloop()

    def buildMain(self):
        self.pSrc = viewDirControl.ViewDirControl("Source")
        self.pDst = viewDirControl.ViewDirControl("Destination")

if __name__ == '__main__' :

    root = ViewMain()