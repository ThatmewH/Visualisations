import random, pygame

array = []
width = 800
height = 600

redLines = []
greenLines = []

def makeArray(lineWidth=2):
    global array
    for line in range(width//lineWidth):
        # array.append(noise.pnoise1(line/height, 6)*height)
        array.append(random.randint(10, height))

def drawArray(array, win, redLines, greenLines, lineWidth=2):
    for x in range(len(array)):
        pygame.draw.line(win, (int((array[x]/height)*200),20,int((array[x]/height)*200)), (x*lineWidth,height), (x*lineWidth,height-array[x]), lineWidth)
    for redLine in redLines:
        pygame.draw.line(win, (255,0,0), (redLine[1]*lineWidth,height), (redLine[1]*lineWidth,height-redLine[0]), lineWidth)
    for greenLine in greenLines:
        pygame.draw.line(win, (0,255,0), (greenLine[1]*lineWidth,height), (greenLine[1]*lineWidth,height-greenLine[0]), lineWidth)


def rgbToHue(r, g, b):
    cMax = max(r, max(g, b))
    cMin = min(r, min(g, b))
    cDiff = cMax - cMin

    h = -1
    s = -1

    # Calculate Hue
    if cMax == cMin:
        h = 0
    elif cMax == r:
        h =  ((60 * ((g - b) / cDiff) + 360) % 360)
    elif cMax == g:
        h =  ((60 * ((b - r) / cDiff) + 120) % 360)
    elif cMax == b:
        h =  ((60 * ((r - g) / cDiff) + 240) % 360)
    else:
        h =  -1
    # Calcualte Saturation
    if cMax == 0:
        s = 0
    else:
        s = (cDiff / cMax) * 100
    # Calculate V
    v = cMax * 100
    return [h,s,v]
def swap(index1, index2):
    global array
    tempIndex1Value = array[index1]
    array[index1] = array[index2]
    array[index2] = tempIndex1Value
