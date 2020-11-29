import tracker

import sys
import subprocess
import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

def trackingButton(instance):
    global trackingRunning
    if trackingRunning == False:
        tracker.initialise()
        trackingRunning = True
        print("completed")
    elif trackingRunning == True:
        tracker.halt()
        trackingRunning = False
        print("completed2")

def generateButton(instance):
    #NEEDS FINISHING
    return

class homePage(GridLayout):
    def __init__(self, **kwargs):
        super(homePage, self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text='Tracking'))
        self.trackBtn = Button(text='Enable')
        self.trackBtn.bind(on_press=trackingButton)
        self.add_widget(self.trackBtn)
        self.add_widget(Label(text='Usage Statistics'))
        self.genBtn = Button(text='Generate')
        self.genBtn.bind(on_press=generateButton)
        self.add_widget(self.genBtn)

class ProgramInterface(App):
    def build(self):
        return homePage()


trackingRunning = False
ProgramInterface().run()
