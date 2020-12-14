import pygame
pygame.init()
windowSize = [1700, 950]
window = pygame.display.set_mode(windowSize)
backgroundImg = pygame.image.load('assets/images/background.png')
background = pygame.transform.scale(backgroundImg, (windowSize))
controlsBackground = pygame.image.load('assets/images/controlsBack.png')
controlsBackground = pygame.transform.scale(controlsBackground, (1700, 950))
start = pygame.image.load('assets/images/start.png')
pressStart = pygame.image.load('assets/images/PressStart.png')
controls = pygame.image.load('assets/images/controls.png')
pressControls = pygame.image.load('assets/images/pressControls.png')
leave = pygame.image.load('assets/images/quit.png')
pressLeave = pygame.image.load('assets/images/pressQuit.png')
start = pygame.transform.scale(start, (1300, 160))
pressStart = pygame.transform.scale(pressStart, (1300, 160))
controls = pygame.transform.scale(controls, (1300, 160))
pressControls = pygame.transform.scale(pressControls, (1300, 160))
leave = pygame.transform.scale(leave, (1300, 160))
pressLeave = pygame.transform.scale(pressLeave, (1300, 160))
menuFinish = False
mouseDown = False
controlScreen = False
while not menuFinish:
    window.blit(background, (0,0))
    mouseX, mouseY = pygame.mouse.get_pos()
    window.blit(start, (200, 160))
    window.blit(controls, (200, 400))
    window.blit(leave, (200, 640))
    if mouseX > 200 and mouseX < 1500 and not(controlScreen):
        if mouseY > 160 and mouseY < 320:
            window.blit(pressStart, (200, 160))
            if mouseDown:
                menuFinish = True
                finished = False
        if mouseY > 640 and mouseY < 800:
            window.blit(pressLeave, (200, 640))
            if mouseDown:
                menuFinish = True
                finished = True
        if mouseY > 400 and mouseY < 560:
            window.blit(pressControls, (200, 400))
            if mouseDown:
                controlScreen = True
    if controlScreen:
        window.blit(controlsBackground, (0,0))
        if mouseX > 20 and mouseX < 200 and mouseY > 20 and mouseY < 200 and mouseDown:
            controlScreen = False
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            menuFinish = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouseDown = True
        else:
            mouseDown = False
pygame.quit()