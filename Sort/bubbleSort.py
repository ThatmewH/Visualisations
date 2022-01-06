from sortFunctions import *

pygame.init()
win = pygame.display.set_mode((width, height))
lineWidth = 10
makeArray(lineWidth)

a = 0
b = 0
finishedSort = False

while True:
    win.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    # Sort Algorithm
    if not(finishedSort):
        if array[a] > array[a+1]:
            redLines = []
            greenLines = []
            swap(a, a+1)
            greenLines.append([array[a+1], a+1])
        else:
            a += 1
            # redLines.append([array[a], a])
            if a >= len(array)-1:
                a = 0
                b += 1
            if b >= len(array):
                finishedSort = True
                greenLines = []
                redLines = []
    drawArray(array, win, redLines, greenLines, lineWidth)
    pygame.display.update()
