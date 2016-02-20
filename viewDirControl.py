# coding: utf-8

class ViewDirControl:

    def __init__(self, name):
        self.name = name
        self.buildPanel()

    def buildPanel(self):
        print "build panel " + self.name