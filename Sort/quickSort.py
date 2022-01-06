from sortFunctions import *

pygame.init()
win = pygame.display.set_mode((width, height))

lineWidht = 1

makeArray(lineWidht)
a = 0
b = 0
finishedSort = False

def quickSort(low, high):
    global array
    if low < high:
        pi = partion(low, high)

        quickSort(low, pi-1)
        quickSort(pi+1, high)

def partion(low, high):
    global array
    pivot = array[high]
    i = (low - 1)
    redLines = []
    greenLines = []
    for j in range(low, high+1):
        redLines.append([array[j], j])
        if array[j] < pivot:
            i += 1
            swap(i, j)
            greenLines.append([array[i], j])
        win.fill((0,0,0))
        drawArray(array, win, redLines, greenLines, lineWidht)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        pygame.display.update()
    swap(i+1, high)
    return i+1

quickSort(0, len(array)-1)
while True:
    win.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    # Sort Algorithm
    drawArray(array, win, redLines, greenLines, lineWidht)
    pygame.display.update()
