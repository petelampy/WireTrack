#Imports my 2 files
import tracker
import generator

#All them other imports you know
import os
os.environ["KIVY_NO_CONSOLELOG"] = "1"
import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
from kivy.uix.popup import Popup
from PIL import Image


#Creates the GUI window for my program
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

    #Handles whether the tracking program is enabled or disabled
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

    #Generates a heatmap from "generator.py" and opens it
    def generateButton(self, instance):
        generator.generateMouseHeatmap("LeagueOfLegends")
        img = Image.open("mouseHeatmap.png")
        img.show()

    #Retrieves key stats from "generator.py" and displays them in a popup
    def keystatsButton(self, instance):
        keyArr, averagePress = generator.keyUsageMap()
        newArr = []
        for x in keyArr:
            if "." in str(x):
                newArr.append(x.split(".")[1])
            else:
                newArr.append(x)
        content = Label(text="Your most used keys are:\n"+str(newArr[0])+"\n"+str(newArr[1])+"\n"+str(newArr[2])+"\n"+"\nYour average presses per key is: "+str(averagePress))
        popup = Popup(title='Keystroke Statistics',content=content,auto_dismiss=True, size=(400,400))
        content.bind(on_press=popup.dismiss)
        popup.open()
    

#Program interface app to create the window
class ProgramInterface(App):
    def build(self):
        self.title = 'WireTrack - Statistics Tracker'
        return homePage()

#runs the programinterface app
trackingRunning = False
ProgramInterface().run()
