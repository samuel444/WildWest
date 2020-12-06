import pygame
pygame.init()
windowSize = [1700, 950]
window = pygame.display.set_mode(windowSize)
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
reloading = 101
finished = False
health = 800
bullets = []
bulletsLeft = 8
toDel = []
x = 820
y = 7440
flooring = 7440
timing = 50
gravity = 3
speed = 0
time = 0
direction = 'r'
show = stand
while not finished:
    health -= 1
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
        del bullets[(toDel[0] - minus)]
        del toDel[0]
        minus += 1
    
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
    clock.tick(50)
pygame.quit()
        
    
