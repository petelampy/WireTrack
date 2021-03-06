#Imports for key/mouse monitoring
import pynput
from pynput import mouse
from pynput import keyboard

#Creates empty keysDict
keysDict = {
}
keyReleased = True
haltListeners = False

#When the user presses a mouse button, the coordinates are saved to a file
def mousePress(x, y, button, pressed):
    if haltListeners == True:
        return False
    if pressed == True:
        f = open("mouseTracking.txt", "a")
        f.write(str(x)+"#"+str(y)+"\n")
        f.close()

#When the user presses a key, the number of times it has been pressed is logged in a dictionary   
def keyPress(key):
    global haltListeners
    global keyReleased
    if haltListeners == True:
        return False
    if keyReleased == False:
        return
    try:
        theKey = str(key.char)
    except AttributeError:
        theKey = str(key)
    if theKey in keysDict.keys():
        currentVal = keysDict[str(theKey)]
        currentVal += 1
        keysDict[theKey] = currentVal
    elif theKey not in keysDict.keys():
        keysDict[str(theKey)] = 1
    keyReleased = False

#Checks if a key has been released to prevent multiple additions to key press data
def keyRelease(key):
    global keyReleased
    if keyReleased == True:
        keyReleased = False
    if keyReleased == False:
        keyReleased = True
    return keyReleased

#Halts the listeners and writes the key dictionary to the document
def halt():
    global keysDict
    file = open("keyTracking.txt","w")
    file.truncate(0)
    for key, value in keysDict.items():
        file.write(str(key)+"="+str(value)+"\n")
    file.close()
    global haltListeners
    haltListeners = True

#Reads in the file to a keys dictionary and starts the mouse/key listeners
def initialise():
    global keysDict
    keysFile = open("keyTracking.txt", "r")
    for line in keysFile:
        key = line.split("=")[0]
        amount = line.split("=")[1]
        keysDict[str(key)] = int(amount)
    keysFile.close()
    mouseListener.start()
    keysListener.start()

#Defines mouseListener and keysListener
mouseListener = mouse.Listener(on_click=mousePress)
keysListener = keyboard.Listener(on_press=keyPress, on_release=keyRelease)
