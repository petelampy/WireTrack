import tracker
import generator

import sys
import subprocess
import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown

class homePage(GridLayout):
    def __init__(self, **kwargs):
        super(homePage, self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text="[color=ff3333]WireTrack[/color]", font_size="40sp", halign= "center", markup = True))
        self.add_widget(Label(text="[color=ff3333][i]Keyboard/Mouse Tracking System[/i][/color]", font_size="20sp", halign= "center", markup = True))
        self.add_widget(Label(text="Tracking"))
        self.trackBtn = Button(text="Enable")
        self.trackBtn.bind(on_press=self.trackingButton)
        self.add_widget(self.trackBtn)
        self.add_widget(Label(text="Usage Statistics"))
        self.genBtn = Button(text="Generate")
        self.genBtn.bind(on_press=self.generateButton)
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

    def generateButton(self, instance):
        generator.generateMouseHeatmap("LeagueOfLegends")


class ProgramInterface(App):
    def build(self):
        self.title = 'WireTrack'
        return homePage()


trackingRunning = False
ProgramInterface().run()
