from PIL import Image, ImageDraw
import matplotlib.pyplot as plt
import numpy as np
import scipy.ndimage.filters as filters

#Generates Heat Map of where the user clicks on the screen while tracker is running. Takes various game templates as inputs
def generateMouseHeatmap(gameChoice):
    template = gameChoice
    mouseFile = open("mouseTracking.txt", "r")
    displayArray = np.empty([1080, 1920])
    for line in mouseFile:
        if "-" in line:
            continue
        x = int(line.split("#")[0])
        y = int(line.split("#")[1])
        displayArray[y][x] = displayArray[y][x] + 1

    mouseHeatmap = Image.open("heatmapTemplates/"+template+".png")
    mouseHeatmap.save("mouseHeatmap.png")
    plt.figure()
    img = plt.imread("mouseHeatmap.png")
    plt.imshow(img, alpha=1)
    plt.axis("off")

    xmin, xmax = plt.xlim()
    ymin, ymax = plt.ylim()

    smoothed = filters.gaussian_filter(displayArray, sigma=50)
    plt.imshow(smoothed, cmap="jet", alpha=.5, extent=(xmin,xmax,ymin,ymax))
    plt.savefig("mouseHeatmap.png", bbox_inches="tight", dpi=300)
    plt.close()


def keyUsageMap():
    keysDict = {}
    keysFile = open("keyTracking.txt", "r")
    for line in keysFile:
        key = line.split("=")[0]
        amount = line.split("=")[1]
        keysDict[str(key)] = int(amount)
    keysFile.close()
    keysDict = dict(sorted(keysDict.items(), key=lambda item: item[1]))
    first = str(list(keysDict)[-1])
    second = str(list(keysDict)[-2])
    third = str(list(keysDict)[-3])
    print(first, second, third)
    
keyUsageMap()
