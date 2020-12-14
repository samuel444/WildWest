import pygame
import random
pygame.init()
global windowSize
global window
windowSize = [1700, 950]
window = pygame.display.set_mode(windowSize)
def menuTime():
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
                    game()
                    menuFinish = True
            if mouseY > 640 and mouseY < 800:
                window.blit(pressLeave, (200, 640))
                if mouseDown:
                    menuFinish = True
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
def game():
    font = pygame.font.Font('assets/fonts/plasdrip.ttf', 140)
    skull = pygame.image.load('assets/images/skull.png')
    skull = pygame.transform.scale(skull, (40, 40))
    backgroundImg = pygame.image.load('assets/images/background.png')
    revolver = pygame.image.load('assets/images/revolver.png')
    revolver = pygame.transform.scale(revolver, (150, 210))
    background = pygame.transform.scale(backgroundImg, (windowSize))
    shootingStand = pygame.image.load('assets/images/shooting1.png')
    almostShotStand = pygame.image.load('assets/images/shooting3.png')
    stand = pygame.image.load('assets/images/shooting2.png')
    shootingWalk = pygame.image.load('assets/images/shootingWalk.png')
    almostShotWalk = pygame.image.load('assets/images/almostShootingWalk.png')
    walk = pygame.image.load('assets/images/walk.png')
    pain = pygame.image.load('assets/images/pain.png')
    rogue = pygame.image.load('assets/images/rogue.png')
    rogueWalk = pygame.image.load('assets/images/rogueWalk.png')
    rogueAttack = pygame.image.load('assets/images/rogueAttack.png')
    rogue = pygame.transform.scale(rogue, (75, 150))
    rogueWalk = pygame.transform.scale(rogueWalk, (75, 150))
    rogueAttack = pygame.transform.scale(rogueAttack, (135, 150))
    flipRogue = pygame.transform.flip(rogue, True, False)
    flipRogueAttack = pygame.transform.flip(rogueAttack, True, False)
    flipRogueWalk = pygame.transform.flip(rogueWalk, True, False)
    pain = pygame.transform.scale(pain, (windowSize[0], windowSize[1]))
    flipWalk = pygame.transform.flip(walk, True, False)
    flipStand = pygame.transform.flip(stand, True, False)
    flipAlmostShotWalk = pygame.transform.flip(almostShotWalk, True, False)
    flipAlmostShotStand = pygame.transform.flip(almostShotStand, True, False)
    flipShootingWalk = pygame.transform.flip(shootingWalk, True, False)
    flipShootingStand = pygame.transform.flip(shootingStand, True, False)
    shootingStand = pygame.transform.scale(shootingStand, (96, 156))
    almostShotStand = pygame.transform.scale(almostShotStand, (90, 156))
    stand = pygame.transform.scale(stand, (60, 156))
    shootingWalk = pygame.transform.scale(shootingWalk, (96, 156))
    almostShotWalk = pygame.transform.scale(almostShotWalk, (90, 156))
    walk = pygame.transform.scale(walk, (72, 156))
    flipWalk = pygame.transform.scale(flipWalk, (72, 156))
    flipStand = pygame.transform.scale(flipStand, (60, 156))
    flipAlmostShotWalk = pygame.transform.scale(flipAlmostShotWalk, (90, 156))
    flipAlmostShotStand = pygame.transform.scale(flipAlmostShotStand, (90, 156))
    flipShootingWalk = pygame.transform.scale(flipShootingWalk, (96, 156))
    flipShootingStand = pygame.transform.scale(flipShootingStand, (96, 156))
    black = pygame.color.Color('#000000')
    blood = pygame.color.Color('#8A0303')
    platformColour = pygame.color.Color('#745A23')
    clock = pygame.time.Clock()
    shooting = 120
    kills = 0
    timeBetweenSpawns = 250
    timingsSpawns = [240, 190, 170, 160, 150, 140, 135, 130, 120, 115, 110, 100, 90, 80, 75, 70, 65, 60, 57, 55, 53, 51, 48, 45, 43, 41, 40, 39, 38, 37, 36, 35, 35, 34, 33, 32, 32, 31, 31, 30]
    spawnTimer = 0
    locations = []
    directions = []
    reloading = 101
    health = 800
    bullets = []
    bulletsLeft = 8
    toDel = []
    toDelEnemy = []
    x = 820
    y = 7440
    flooring = 7440
    timing = 50
    gravity = 3
    speed = 0
    time = 0
    direction = 'r'
    show = stand
    finished = False
    while not finished:
        spawnTimer += 1
        if spawnTimer >= timeBetweenSpawns:
            spawnTimer = 0
            place = random.randrange(1,3)
            if place == 1:
                place = [-80, 'r']
            else:
                place = [1720, 'l']
            locations.append([place[0], 7550, place[1], 0, 7550, 0, False, 0, 0])
        window.blit(background, (0,0))
        ammo = font.render(str(bulletsLeft) + '/8', False, blood)
        pygame.draw.rect(window, black, (795, 35, 810, 60))
        window.blit(skull, (1175, 45))
        pygame.draw.rect(window, blood, (800, 40, health, 50))
        pygame.draw.rect(window, platformColour, (0, 900, windowSize[0], 50))
        pygame.draw.rect(window, platformColour, (500, 590, 200, 50))
        pygame.draw.rect(window, platformColour, (1000, 590, 200, 50))
        pygame.draw.rect(window, platformColour, (750, 350, 200, 50))
        oldDirection = direction
        keys = pygame.key.get_pressed()
        if keys[pygame.K_r] and bulletsLeft < 8:
            reloading = 0
            shooting = 100
        if reloading == 100:
            bulletsLeft = 8
            shooting = 0
        reloading += 1
        if shooting == 5:
            if show == almostShotWalk or show == flipAlmostShotWalk:
                show = shootingWalk
            elif show == almostShotStand or show == flipAlmostShotStand:
                show = shootingStand
        if shooting == 100:
            if show == shootingStand or show == flipShootingStand:
                show = almostShotStand
            elif show == shootingWalk or show == flipShootingWalk:
                show = almostShotWalk
        if shooting == 105:
            if show == almostShotStand or show == flipAlmostShotStand:
                show = stand
            elif show == almostShotWalk or show == flipAlmostShotWalk:
                show = walk
        if shooting == 0:
                if show == walk or show == flipWalk:
                    show = almostShotWalk
                if show == stand or show == flipStand:
                    show = almostShotStand
        if keys[pygame.K_d]:
            direction = 'r'
            if time > 0 and time < 15:
                if show == stand:
                    show = walk
                elif show == shootingStand:
                    show = shootingWalk
                elif show == almostShotStand:
                    show = almostShotWalk
            if time > 30:
                time = 0
            x += 7
        if keys[pygame.K_a]:
            direction = 'l'
            if time > 0 and time < 15:
                if show == flipStand:
                    show = walk
                elif show == flipShootingStand:
                    show = shootingWalk
                elif show == flipAlmostShotStand:
                    show = almostShotWalk
            if time > 30:
                time = 0
            x -= 7
        if time == 15 and (show == flipWalk or show == walk):
            show = stand
        elif time == 15 and (show == flipShootingWalk or show == shootingWalk):
            show = shootingStand
        elif time == 15 and (show == flipAlmostShotWalk or show == almostShotWalk):
            show = almostShotStand
        if direction == 'l':
            if show == almostShotStand:
                show = flipAlmostShotStand
            elif show == shootingStand:
                show = flipShootingStand
            elif show == shootingWalk:
                show = flipShootingWalk
            elif show == almostShotWalk:
                show = flipAlmostShotWalk
            elif show == walk:
                show = flipWalk
            elif show == stand:
                show = flipStand
        if direction == 'r':
            if show == flipAlmostShotStand:
                show = almostShotStand
            elif show == flipShootingStand:
                show = shootingStand
            elif show == flipShootingWalk:
                show = shootingWalk
            elif show == flipAlmostShotWalk:
                show = almostShotWalk
            elif show == flipWalk:
                show = walk
            elif show == flipStand:
                show = stand
        if keys[pygame.K_w] and y > flooring and y < (flooring + 10):
            speed = -140
            timing = 0
        if keys[pygame.K_s] and (flooring == 1940 or flooring == 4340):
            flooring = 7740
            timing = 0
        if x < 700 and x > 450 and y < 4440 and timing > 32:
            flooring = 4340
        if x < 1200 and x > 950 and y < 4440 and timing > 32:
            flooring = 4340
        if x < 950 and x > 700 and y < 3500 and timing > 32:
            flooring = 1940
        if not(x < 950 and x > 700 and y < 3500 or x < 1200 and x > 950 and y < 4440 or x < 700 and x > 450 and y < 4440) and timing > 32:
            flooring = 7440
        if y > (flooring) and timing > 20:
            speed = 0
            y = flooring
        y += speed
        shooting += 1
        speed += gravity
        window.blit(show, (x, (y/10)))
        for j in range(len(locations)):
            if not((locations[j][0] - 70) < x and (locations[j][0] + 80) > x and locations[j][4] > (flooring - 200) and locations[j][4] < (flooring + 200)) and locations[j][6] == False:
                    if locations[j][0] < x:
                        locations[j][2] = 'r'
                        locations[j][0] += 3
                    else:
                        locations[j][2] = 'l'
                        locations[j][0] -= 3
                    locations[j][3] += 1
            else:
                locations[j][6] = True
            if locations[j][3] < 20 and locations[j][6] == False:
                if locations[j][2] == 'l':
                    look = rogue
                elif locations[j][2] == 'r':
                    look = flipRogue
            elif locations[j][3] <= 40:
                if locations[j][2] == 'l':
                    look = rogueWalk
                elif locations[j][2] == 'r':
                    look = flipRogueWalk
            if locations[j][6]:
                locations[j][7] += 1
                if locations[j][7] >= 15 and locations[j][7] < 35:
                    if locations[j][2] == 'l':
                        look = rogueAttack
                        locations[j][0] -= 60
                        if locations[j][0] > x and locations[j][0] < (x + 96) and (locations[j][1] + 960) > y and (locations[j][1] + 960) < (y + 1560):
                            health -= 7
                    else:
                        look = flipRogueAttack
                        if (locations[j][0] + 135) > x and (locations[j][0] + 135) < (x + 96) and (locations[j][1] + 960) > y and (locations[j][1] + 960) < (y + 1560):
                            health -= 7
                elif locations[j][7] == 35:
                    if locations[j][2] == 'l':
                        look = rogue
                        if locations[j][8] == 2:
                            locations[j][0] += 60
                            locations[j][8] = 0
                    else:
                        look = flipRogue
                    locations[j][6] = False
                    locations[j][7] = 0
            if locations[j][3] == 40:
                locations[j][3] = 0
            window.blit(look, (locations[j][0], (locations[j][1] / 10)))
            if look == rogueAttack:
                locations[j][0] += 60
            if locations[j][0] < 680 and locations[j][0] > 450 and locations[j][1] < 4550:
                locations[j][4] = 4450
            if locations[j][0] < 1180 and locations[j][0] > 950 and locations[j][1] < 4550:
                locations[j][4] = 4450
            if locations[j][0] < 930 and locations[j][0] > 700 and locations[j][1] < 2150:
                locations[j][4] = 2050
            if not(locations[j][0] < 930 and locations[j][0] > 700 and locations[j][1] < 2150 or locations[j][0] < 1180 and locations[j][0] > 950 and locations[j][1] < 4550 or locations[j][0] < 680 and locations[j][0] > 450 and locations[j][1] < 4550):
                locations[j][4] = 7550
            locations[j][1] += locations[j][5]
            locations[j][5] += gravity
            if locations[j][1] > (locations[j][4] + 10):
                locations[j][1] = locations[j][4]
                locations[j][5] = 0
            jump = random.randrange(0, 200)
            if (jump == 1 or (y < (locations[j][1] - 2500) and locations[j][0] < 1300 and locations[j][0] > 300)) and locations[j][1] == locations[j][4]:
                locations[j][5] = -140
            for k in range(len(bullets)):
                if bullets[k][0] >= locations[j][0] and bullets[k][0] <= (locations[j][0] + 75) and bullets[k][1] >= locations[j][1] and bullets[k][1] <= (locations[j][1] + 1500) and not(k in toDel):
                    toDel.append(k)
                    toDelEnemy.append(j)
                    kills += 1
                    if kills < 39:
                        timeBetweenSpawns = timingsSpawns[kills]
                    else:
                        timeBetweenSpawns = 30
        for i in range(len(bullets)):
            if bullets[i][2] == 'r':
                bullets[i][0] += 20
            else:
                bullets[i][0] -= 20
            pygame.draw.rect(window, black, (bullets[i][0], (bullets[i][1] / 10), 6, 6))
            if bullets[i][0] > windowSize[0] or bullets[i][0] < -6:
                toDel.append(i)
        minus = 0
        while toDel != []:
            if bullets != []:
                del bullets[(toDel[0] - minus)]
            del toDel[0]
            minus += 1
        minus = 0
        while toDelEnemy != []:
            del locations[(toDelEnemy[0] - minus)]
            del toDelEnemy[0]
            minus += 1
        if x > windowSize[0] or x < -60:
            window.blit(pain, (0,0))
            health -= 4
        window.blit(revolver, (20, 20))
        window.blit(ammo, (180, 70))
        pygame.display.flip()
        time += 1
        timing += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if reloading > 100 and bulletsLeft > 0:
                    shooting = 0
                    bulletsLeft -= 1
                    y1 = y + 540
                    if direction == 'r':
                        x1 = x + 96
                    else:
                        x1 = x
                    bullets.append([x1, y1, direction])
        if health <= 0:
            menuTime()
            finished = True
        clock.tick(50)
menuTime()

