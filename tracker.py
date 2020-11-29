import pynput
from pynput import mouse
from pynput import keyboard

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

    print(keysDict[str(theKey)])
    keyReleased = False

def keyRelease(key):
    global keyReleased
    if keyReleased == True:
        keyReleased = False
    if keyReleased == False:
        keyReleased = True
    return keyReleased

def halt():
    global haltListeners
    haltListeners = True

def initialise():
    global keysDict
    keysFile = open("keyTracking.txt", "r")
    for line in keysFile:
        key = line.split("=")[0]
        amount = line.split("=")[1]
        keysDict[str(key)] = int(amount)
    mouseListener = mouse.Listener(on_click=mousePress)
    mouseListener.start()

    keysListener = keyboard.Listener(on_press=keyPress, on_release=keyRelease)
    keysListener.start()
