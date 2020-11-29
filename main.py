import tracker
import generator

import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
from kivy.uix.popup import Popup
from PIL import Image

class homePage(GridLayout):
    def __init__(self, **kwargs):
        super(homePage, self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text="[color=ff3333]WireTrack[/color]", font_size="40sp", halign= "center", markup = True))
        self.add_widget(Label(text=" ", font_size="15sp", halign= "center", markup = True))
        self.add_widget(Label(text="Enable mouse and keyboard tracking"))
        self.trackBtn = Button(text="Enable")
        self.trackBtn.bind(on_press=self.trackingButton)
        self.add_widget(self.trackBtn)
        self.add_widget(Label(text="Generate Mouse Heatmap"))
        self.genBtn = Button(text="Generate")
        self.genBtn.bind(on_press=self.generateButton)
        self.add_widget(self.genBtn)
        self.add_widget(Label(text="View Keypress Statistics"))
        self.statBtn = Button(text="View")
        self.statBtn.bind(on_press=self.keystatsButton)
        self.add_widget(self.statBtn)

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
        img = Image.open("mouseHeatmap.png")
        img.show()

    def keystatsButton(self, instance):
        #Move this pop up somewhere else
        popup = Popup(title='Keystroke Statistics', content=Label(text="Hello world"), auto_dismiss=False)
        popup.open()

class ProgramInterface(App):
    def build(self):
        self.title = 'WireTrack - Statistics Tracker'
        return homePage()


trackingRunning = False
ProgramInterface().run()
