from sortFunctions import *

pygame.init()
win = pygame.display.set_mode((width, height))
lineWidth = 1
makeArray(lineWidth)

a = 0
b = len(array)

finishedSort = False
def getMin(startPos):
    global array
    minNum = array[0]
    minNumIndex = 0
    for num in range(startPos,len(array)):
        redLines.append([array[num], num])
        if array[num] < minNum:
            minNum = array[num]
            minNumIndex = num
    return minNum, minNumIndex
clock = pygame.time.Clock()
while True:
    win.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    greenLines = []
    redLines = []
    # Sort Algorithm
    if not(finishedSort):
        minValue, minValueIndex = getMin(a)
        swap(minValueIndex, a)
        greenLines.append([minValue, minValueIndex])
        a += 1
        if a >= len(array):
            finishedSort = True
            redLines = []
            greenLines = []
    drawArray(array, win, redLines, greenLines, lineWidth)
    pygame.display.update()
    # clock.tick(10)
