import pygame
pygame.init()
windowSize = [1700, 950]
window = pygame.display.set_mode(windowSize)
file = open('assets/leaderboard.txt', 'r')
contents = file.read()
contents = contents.split(',')
white = pygame.color.Color('#ffffff')
font = pygame.font.Font('assets/fonts/stencilfont.ttf', 130)
kills = font.render(str(eliminations) + ' KILLS', False, white)
first = font.render(contents[0] + ' KILLS', False, white)
second = font.render(contents[1] + ' KILLS', False, white)
third = font.render(contents[2] + ' KILLS', False, white)
fourth = font.render(contents[3] + ' KILLS', False, white)
fifth = font.render(contents[4] + ' KILLS', False, white)
leaderboard = pygame.image.load('assets/images/leaderboard.png')
leaderboard = pygame.transform.scale(leaderboard, (windowSize[0], windowSize[1]))
if int(contents[0]) < int(eliminations):
    placeHolder = contents[0]
    contents[0] = eliminations
    eliminations = placeHolder
if int(contents[1]) < int(eliminations):
    placeHolder = contents[1]
    contents[1] = eliminations
    eliminations = placeHolder
if int(contents[2]) < int(eliminations):
    placeHolder = contents[2]
    contents[2] = eliminations
    eliminations = placeHolder
if int(contents[3]) < int(eliminations):
    placeHolder = contents[3]
    contents[3] = eliminations
    eliminations = placeHolder
if int(contents[4]) < int(eliminations):
    placeHolder = contents[4]
    contents[4] = eliminations
    eliminations = placeHolder
file = open('assets/leaderboard.txt', 'w')
file.write(str(contents[0]) + ',' + str(contents[1]) + ',' + str(contents[2]) + ',' + str(contents[3]) + ',' + str(contents[4]))
resultsFinish = False
stage = False
mouseDown = False
while not resultsFinish:
    window.blit(leaderboard, (0,0))
    window.blit(first, (450, 175))
    window.blit(second, (450, 287))
    window.blit(third, (450, 397))
    window.blit(fourth, (450, 510))
    window.blit(fifth, (450, 624))
    window.blit(kills, (450, 746))
    pygame.display.flip()
    if stage and mouseDown:
        #menuTime()
        resultsFinish = True
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            resultsFinish = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouseDown = True
        else:
            mouseDown = False
            stage = True
pygame.quit()
