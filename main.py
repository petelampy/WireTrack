import tracker

import sys
import subprocess
import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button


def generateButton(instance):
    #NEEDS FINISHING
    return

class homePage(GridLayout):
    def __init__(self, **kwargs):
        super(homePage, self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text='Tracking'))
        self.trackBtn = Button(text='Enable')
        self.trackBtn.bind(on_press=self.trackingButton)
        self.add_widget(self.trackBtn)
        self.add_widget(Label(text='Usage Statistics'))
        self.genBtn = Button(text='Generate')
        self.genBtn.bind(on_press=generateButton)
        self.add_widget(self.genBtn)

    def trackingButton(self, instance):
        global trackingRunning
        if trackingRunning == False:
            tracker.initialise()
            trackingRunning = True
            self.trackBtn.text = "Disable"
        elif trackingRunning == True:
            tracker.halt()
            trackingRunning = False
            self.trackBtn.text = "Enable"

class ProgramInterface(App):
    def build(self):
        return homePage()


trackingRunning = False
ProgramInterface().run()
