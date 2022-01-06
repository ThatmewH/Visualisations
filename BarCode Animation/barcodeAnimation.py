import pygame, os
pygame.init()
width = 500
height = 500
win = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()


def drawBarcode(numImages, pos, barcodeDimensions, height):
    offset = 0
    for lineNum in range(barcodeDimensions[0], barcodeDimensions[1], numImages):
        offset += numImages
        pygame.draw.rect(win, (0, 0, 0), (pos[0] + offset - ((abs(barcodeDimensions[0]) + abs(barcodeDimensions[1])) // 2),pos[1] - (height//2), numImages - 1, height))

def drawImages(images):
    for imageNum in range(0, len(images)):
        surface = pygame.Surface((images[imageNum].get_width(), images[imageNum].get_height()))
        surface.fill((255, 255, 255))
        surface.set_colorkey((255, 255, 255))
        surface.blit(images[imageNum], (0, 0))
        for line in range(0, images[imageNum].get_width(), len(images)):
            pygame.draw.line(surface, (255, 255, 255), (line, 0), (line, images[imageNum].get_height()), len(images) - 1)
        win.blit(surface, (0 + imageNum, 0))
def getImages(dir):
    tempImages = []
    for imageName in os.listdir(dir):
        image = pygame.image.load(dir + "/" + imageName)
        image.set_colorkey((255, 255, 255))
        tempImages.append(image)
    return tempImages
images = getImages("images")

def makeBarcode(numImages, pos, barcodeDimensions, height):
    offset = 0
    surface = pygame.Surface(pos)
    surface.fill((255, 255, 255))
    surface.set_colorkey((255, 255, 255))
    for lineNum in range(barcodeDimensions[0], barcodeDimensions[1], numImages):
        offset += numImages
        pygame.draw.rect(surface, (0, 0, 0), (pos[0]+offset - ((abs(barcodeDimensions[0]) + abs(barcodeDimensions[1])) // 2), pos[1] - (height//2), numImages-1, height))
    return surface
while True:
    win.fill((255, 255, 255))
    clock.tick(300)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    drawImages(images)
    drawBarcode(len(images), pygame.mouse.get_pos(), (-200, 200), 400)

    pygame.display.flip()
