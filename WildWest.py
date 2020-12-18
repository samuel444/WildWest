# Imports
import pygame
import random
pygame.init()

# Variables that create the pygame window
global windowSize
global window
windowSize = [1700, 950]
window = pygame.display.set_mode(windowSize)

# Function that creates the main menu
def menuTime():

    # Creating a list for all the images for the main menu
    menuImages = [pygame.image.load('assets/images/background.png'),pygame.image.load('assets/images/controlsBack.png'),pygame.image.load('assets/images/start.png'),pygame.image.load('assets/images/PressStart.png'),pygame.image.load('assets/images/controls.png'),pygame.image.load('assets/images/pressControls.png'),pygame.image.load('assets/images/quit.png'),pygame.image.load('assets/images/pressQuit.png')]
    menuImages = [pygame.transform.scale(menuImages[0], (windowSize)),pygame.transform.scale(menuImages[1], (1700, 950)),pygame.transform.scale(menuImages[2], (1300, 160)),pygame.transform.scale(menuImages[3], (1300, 160)),pygame.transform.scale(menuImages[4], (1300, 160)),pygame.transform.scale(menuImages[5], (1300, 160)),pygame.transform.scale(menuImages[6], (1300, 160)),pygame.transform.scale(menuImages[7], (1300, 160))]

    # Initializing some variables 
    menuFinish = False
    mouseDown = False
    controlScreen = False

    # Main menu loop
    while not menuFinish:

        # Create background
        window.blit(menuImages[0], (0,0))

        # Display the buttons
        window.blit(menuImages[2], (200, 160))
        window.blit(menuImages[4], (200, 400))
        window.blit(menuImages[6], (200, 640))

        # Receive the x and y coordinates of the mouse
        mouseX, mouseY = pygame.mouse.get_pos()

        # Finding out if the mouse is hovering over or pressing a button
        if mouseX > 200 and mouseX < 1500 and not(controlScreen):
            if mouseY > 160 and mouseY < 320:
                window.blit(menuImages[3], (200, 160))

                # If the button is pressed, it calls the game function and stop the main menu loop
                if mouseDown:
                    game()
                    menuFinish = True

            if mouseY > 640 and mouseY < 800:
                window.blit(menuImages[7], (200, 640))

                # Checks if the quit button is pressed, if so it stops the loop
                if mouseDown:
                    menuFinish = True

            if mouseY > 400 and mouseY < 560:
                window.blit(menuImages[5], (200, 400))

                # Will check if the control button is pressed
                if mouseDown:
                    controlScreen = True
        
        # Check if the control button is pressed and therefore if the controls page should be displayed
        if controlScreen:

            # This displays the controls page
            window.blit(menuImages[1], (0,0))

            # Checks if the back button has been pressed
            if mouseX > 20 and mouseX < 200 and mouseY > 20 and mouseY < 200 and mouseDown:
                controlScreen = False

        # Displays everything onto the window
        pygame.display.flip()

        # Checks for events
        for event in pygame.event.get():

            # Checks if the exit button has been pressed, so it can quit
            if event.type == pygame.QUIT:
                menuFinish = True
            
            # Checks if the mouse has been pressed
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouseDown = True
            else:
                mouseDown = False

# This function is for the main game
def game():

    # Loading all of the characters and enemy sprites
    sprites = [[pygame.image.load('assets/images/shooting1.png'),pygame.image.load('assets/images/shooting3.png'),pygame.image.load('assets/images/shooting2.png'),pygame.image.load('assets/images/shootingWalk.png'),pygame.image.load('assets/images/almostShootingWalk.png'),pygame.image.load('assets/images/walk.png')],[pygame.image.load('assets/images/rogue.png'),pygame.image.load('assets/images/rogueWalk.png'),pygame.image.load('assets/images/rogueAttack.png')]]
    sprites = [[pygame.transform.scale(sprites[0][0], (96,156)),pygame.transform.scale(sprites[0][1], (90,156)),pygame.transform.scale(sprites[0][2], (60,156)),pygame.transform.scale(sprites[0][3], (96,156)),pygame.transform.scale(sprites[0][4], (90,156)),pygame.transform.scale(sprites[0][5], (72,156)),],[pygame.transform.scale(sprites[1][0], (75,150)),pygame.transform.scale(sprites[1][1], (75,150)),pygame.transform.scale(sprites[1][2], (135,150)),]]
    flippedSprites = [[pygame.transform.flip(sprites[0][0], True, False),pygame.transform.flip(sprites[0][1], True, False),pygame.transform.flip(sprites[0][2], True, False),pygame.transform.flip(sprites[0][3], True, False),pygame.transform.flip(sprites[0][4], True, False),pygame.transform.flip(sprites[0][5], True, False)],[pygame.transform.flip(sprites[1][0], True, False),pygame.transform.flip(sprites[1][1], True, False),pygame.transform.flip(sprites[1][2], True, False)]]
    
    # Loading all the images that will be used
    images = [pygame.image.load('assets/images/skull.png'),pygame.image.load('assets/images/background.png'),pygame.image.load('assets/images/revolver.png'),pygame.image.load('assets/images/pain.png')]
    images = [pygame.transform.scale(images[0], (40, 40)),pygame.transform.scale(images[1], (windowSize)),pygame.transform.scale(images[2], (150, 210)),pygame.transform.scale(images[3], (windowSize))]
    
    # Loading the fonts we are going to use
    fonts = [pygame.font.Font('assets/fonts/plasdrip.ttf', 140),pygame.font.Font('assets/fonts/stencilfont.ttf', 55)]

    # Loading all the colours in
    colours = [pygame.color.Color('#000000'),pygame.color.Color('#8A0303'),pygame.color.Color('#745A23'),pygame.color.Color('#ffffff')]

    # List for all the player attributes
    character = [800, 8, 820, 7440, 7440, 'r', 0, sprites[0][2]]

    # Timers for use in program
    timers = [0,0,120,0,50]

    # Initialising some lists to use in the program
    timingsSpawns = [250, 230, 210, 200, 190, 180, 170, 170, 160, 156, 155, 150, 145, 140, 135, 130, 128, 125, 120, 120, 120, 118, 115, 115, 110, 110, 105, 100, 100, 100, 100, 100, 97, 95, 93, 91, 90, 88, 86, 87, 87, 87, 85, 83, 80, 78, 78, 78, 78, 75, 72, 70, 70, 70, 65, 65, 60, 59, 58, 57, 56, 56, 56, 55, 54, 53, 52, 52, 51, 50, 50, 50, 50, 50, 48, 45, 45, 45, 45, 44, 44, 44, 43, 42, 41, 41, 41, 40, 39, 39, 38, 38, 37, 37, 36, 35, 35, 35, 35, 34, 33, 32, 32, 32, 32, 31, 31, 31]
    enemies = []
    bullets = []
    toDel = []
    toDelEnemy = []

    # Making the clock command
    clock = pygame.time.Clock()

    # Adding in the gravity constant
    gravity = 3

    # Initialising the kills and timing between spawns variables
    kills = 0
    timeBetweenSpawns = 250

    # Make it false to begin the program
    finished = False

    # Pygame window code
    while not finished:

        # Creating the text that displays the currents kills
        killText = fonts[1].render(str(kills), False, colours[3])

        # Adding onto the timer that will spawn enemies every interval
        timers[0] += 1

        # Checking if the timer has reached the interval
        if timers[0] >= timeBetweenSpawns:

            # Resets timer
            timers[0] = 0

            # Picks if the enemy is going to come from the right or the left
            place = random.randrange(1,3)
            if place == 1:
                place = [-80, 'r']
            else:
                place = [1720, 'l']

            # Adding information into the list that display all the enemy's attributes
            enemies.append([place[0], 7550, place[1], 0, 7550, 0, False, 0])

        # Places the background into the pygame
        window.blit(images[1], (0,0))

        # Creates the text that shows the amount of bullets remaining
        ammo = fonts[0].render(str(character[1]) + '/8', False, colours[1])

        # Making the health bar
        pygame.draw.rect(window, colours[0], (795, 35, 810, 60))
        pygame.draw.rect(window, colours[1], (800, 40, character[0], 50))

        # Creating all of the floors to be jumped on to
        pygame.draw.rect(window, colours[2], (0, 900, windowSize[0], 50))
        pygame.draw.rect(window, colours[2], (500, 590, 200, 50))
        pygame.draw.rect(window, colours[2], (1000, 590, 200, 50))
        pygame.draw.rect(window, colours[2], (750, 350, 200, 50))

        # Displaying the kill counter
        window.blit(images[0], (805, 45))
        window.blit(killText, (850, 35))

        # Variable to check if a key is being pressed and if so what
        keys = pygame.key.get_pressed()

        # Checking if the key, r, is being pressed
        if keys[pygame.K_r]:

            # Checking that the magazine isn't already full
            if character[1] < 8:

                # Increasing the reloading timer
                timers[1] += 1

                # Sets a variable to tell the program that the player is currently reloading
                reloading = True

                # This checks if the r key has 'just' been pressed, therefore will make the character put away his gun
                if not(rIsPressed):
                    timers[2] = 100

                # Checks if enough time has passed to add a bullet on a magazine
                if timers[1] >= 18:

                    # Resets the timer then increases the amount of bullets by 1
                    timers[1] = 0
                    character[1] += 1
            
            # Sets the variable to show that r has been pressed
            rIsPressed = True
        else:

            # Resets the reloading timer, show that r isn't being presed and that the character isn't reloading
            timers[1] = 0
            rIsPressed = False
            reloading = False
        
        # Checks for the current state the character should be in depending on the timers
        # Either, shooting, not shooting or taking out the weapon
        if timers[2] == 5:
            if character[7] == sprites[0][4] or character[7] == flippedSprites[0][4]:
                character[7] = sprites[0][3]
            elif character[7] == sprites[0][1] or character[7] == flippedSprites[0][1]:
                character[7] = sprites[0][0]
        if timers[2] == 100:
            if character[7] == sprites[0][0] or character[7] == flippedSprites[0][0]:
                character[7] = sprites[0][1]
            elif character[7] == sprites[0][3] or character[7] == flippedSprites[0][3]:
                character[7] = sprites[0][4]
        if timers[2] == 105:
            if character[7] == sprites[0][1] or character[7] == flippedSprites[0][1]:
                character[7] = sprites[0][2]
            elif character[7] == sprites[0][4] or character[7] == flippedSprites[0][4]:
                character[7] = sprites[0][5]
        if timers[2] == 0:
                if character[7] == sprites[0][5] or character[7] == flippedSprites[0][5]:
                    character[7] = sprites[0][4]
                if character[7] == sprites[0][2] or character[7] == flippedSprites[0][2]:
                    character[7] = sprites[0][1]

        # Checks if the key 'd' is being pressed
        if keys[pygame.K_d]:

            # Changing the direction of the character to right
            character[5] = 'r'

            # Checking if the timer shows that the character should have the walking sprite
            if timers[3] > 0 and timers[3] < 15:

                # Now checks what state it could be in, and if it is standing, then it will change it to it's firing state but walking
                if character[7] == sprites[0][2]:
                    character[7] = sprites[0][5]
                elif character[7] == sprites[0][0]:
                    character[7] = sprites[0][3]
                elif character[7] == sprites[0][1]:
                    character[7] = sprites[0][4]
            
            # Resets the timer if it goes above 30
            if timers[3] > 30:
                timers[3] = 0

            # Increases the x coordinate of the character so it will move right
            character[2] += 7
        
        # Now the same but if it flipped the other way round
        # Checks if the key 'a' is being pressed
        if keys[pygame.K_a]:
            character[5] = 'l'
            if timers[3] > 0 and timers[3] < 15:
                if character[7] == flippedSprites[0][2]:
                    character[7] = sprites[0][5]
                elif character[7] == flippedSprites[0][0]:
                    character[7] = sprites[0][3]
                elif character[7] == flippedSprites[0][1]:
                    character[7] = sprites[0][4]
            if timers[3] > 30:
                timers[3] = 0
            character[2] -= 7

        # Changes the walking sprites to standing sprites if the timer has reached 15
        # Checks which state of firing the character was in, so it can change back to standing version    
        if timers[3] == 15 and (character[7] == flippedSprites[0][5] or character[7] == sprites[0][5]):
            character[7] = sprites[0][2]
        elif timers[3] == 15 and (character[7] == flippedSprites[0][3] or character[7] == sprites[0][3]):
            character[7] = sprites[0][0]
        elif timers[3] == 15 and (character[7] == flippedSprites[0][4] or character[7] == sprites[0][4]):
            character[7] = sprites[0][1]
        
        # Changes all of the sprites to the flipped version if the direction of the player is left
        if character[5] == 'l':
            if character[7] == sprites[0][1]:
                character[7] = flippedSprites[0][1]
            elif character[7] == sprites[0][0]:
                character[7] = flippedSprites[0][0]
            elif character[7] == sprites[0][3]:
                character[7] = flippedSprites[0][3]
            elif character[7] == sprites[0][4]:
                character[7] = flippedSprites[0][4]
            elif character[7] == sprites[0][5]:
                character[7] = flippedSprites[0][5]
            elif character[7] == sprites[0][2]:
                character[7] = flippedSprites[0][2]
        
        # Changes all of the flipped versions of sprites to the normal versions if the direction of the player is right
        if character[5] == 'r':
            if character[7] == flippedSprites[0][1]:
                character[7] = sprites[0][1]
            elif character[7] == flippedSprites[0][0]:
                character[7] = sprites[0][0]
            elif character[7] == flippedSprites[0][3]:
                character[7] = sprites[0][3]
            elif character[7] == flippedSprites[0][4]:
                character[7] = sprites[0][4]
            elif character[7] == flippedSprites[0][5]:
                character[7] = sprites[0][5]
            elif character[7] == flippedSprites[0][2]:
                character[7] = sprites[0][2]

        # Checks if the key 'w' has been pressed and that the player is touching the floor
        if keys[pygame.K_w] and character[3] > character[4] and character[3] < (character[4] + 10):

            # Changes the speed of the character vertically to -140
            character[6] = -140

            # Sets a timer to 0 to relax other commands to stop them from interfering
            timers[4] = 0
        
        # Checks if the key 's' is pressed and the player is touching the floor
        if keys[pygame.K_s] and (character[4] == 1940 or character[4] == 4340):

            # Sets it so the current floor for the character is the bottom one
            character[4] = 7740

            # Sets a timer to 0 to relax other commands to stop them from interfering
            timers[4] = 0
        
        # Changes the flooring by looking at what floor the character is currently above
        # Also checks that the timer hasn't has gone past, so it isn't interfering with anything
        if character[2] < 700 and character[2] > 450 and character[3] < 4440 and timers[4] > 32:
            character[4] = 4340
        if character[2] < 1200 and character[2] > 950 and character[3] < 4440 and timers[4] > 32:
            character[4] = 4340
        if character[2] < 950 and character[2] > 700 and character[3] < 3500 and timers[4] > 32:
            character[4] = 1940
        if not(character[2] < 950 and character[2] > 700 and character[3] < 3500 or character[2] < 1200 and character[2] > 950 and character[3] < 4440 or character[2] < 700 and character[2] > 450 and character[3] < 4440) and timers[4] > 32:
            character[4] = 7440

        # Checking if the character is touching the floor and is not interfering
        if character[3] > (character[4]) and timers[4] > 20:

            # Sets the speed of the vertical to 0
            character[6] = 0

            # Changes the y coordinate of the character to the current value of the flooring
            character[3] = character[4]

        # Changes the y coordinate by the current speed of the vertical
        character[3] += character[6]

        # Adds 1 onto the timer that changes the stance of the character
        timers[2] += 1

        # Adds gravity onto the vertical speed
        character[6] += gravity

        # Placing the character onto the pygame window
        window.blit(character[7], (character[2], (character[3]/10)))

        # Creating a for loop, this is to update and make every enemy on the window
        for j in range(len(enemies)):

            # This will check that an enemy isn't too close to the player, and that the enemy is not in the attacking motion
            if not((enemies[j][0] - 70) < character[2] and (enemies[j][0] + 80) > character[2] and enemies[j][4] > (character[4] - 200) and enemies[j][4] < (character[4] + 200)) and enemies[j][6] == False:
                    
                    # Checking if the player is ahead of the enemy or behind
                    if enemies[j][0] < character[2]:

                        # If they are ahead then the enemy will be facing the right and will move 3 to the right
                        enemies[j][2] = 'r'
                        enemies[j][0] += 3
                    else:
                        
                        # If they are behind the enemy, then the enemy will face left and move 3 to the right
                        enemies[j][2] = 'l'
                        enemies[j][0] -= 3

                    # Then the timer, that will determine if the enemy's sprite shuld be walking or not, will increase by 1
                    enemies[j][3] += 1
            else:

                # If the enemy is close to the player then it will change the variable to ture, this will tel; the program that it is in the middle of stabbing
                enemies[j][6] = True
            
            # Checking if the timer shows that the enemy should be walking or not, and that the enemy isn't currently attacking
            # This one checks if it look like it is still
            if enemies[j][3] < 20 and enemies[j][6] == False:

                # Checking the direction the enemy is facing to give the correct sprite
                if enemies[j][2] == 'l':
                    look = sprites[1][0]
                elif enemies[j][2] == 'r':
                    look = flippedSprites[1][0]
            
            # This one will check if it should look like it is walking
            elif enemies[j][3] <= 40:
                if enemies[j][2] == 'l':
                    look = sprites[1][1]
                elif enemies[j][2] == 'r':
                    look = flippedSprites[1][1]

            # This will check if the enemy is attacking
            if enemies[j][6]:

                # If the enemy is attacking then it will add 1 onto a timer
                # This timer will monitor how long the enemy will be attacking for
                enemies[j][7] += 1

                # This checks if the skin should be in the motion of attacking or just standing still
                if enemies[j][7] >= 5 and enemies[j][7] < 25:

                    # Checking what direction that the enemy should be attacking in
                    if enemies[j][2] == 'l':

                        # Changes to the attacking sprite in the corresponding direction
                        look = sprites[1][2]

                        # In this case, I will move the sprite in a direction so it doesn't appear to move backwards
                        enemies[j][0] -= 60

                        # Checking if the weapon is touching the player
                        if enemies[j][0] > character[2] and enemies[j][0] < (character[2] + 96) and (enemies[j][1] + 960) > character[3] and (enemies[j][1] + 960) < (character[3] + 1560):
                            
                            # If it is, then it will decrease the players health
                            character[0] -= 7
                    else:

                        # This is for the other direction, there is no need to change the enemies x coordinate for this
                        look = flippedSprites[1][2]
                        if (enemies[j][0] + 135) > character[2] and (enemies[j][0] + 135) < (character[2] + 96) and (enemies[j][1] + 960) > character[3] and (enemies[j][1] + 960) < (character[3] + 1560):
                            character[0] -= 7
                
                # This checks if the enemy should stop attacking
                elif enemies[j][7] == 25:

                    # Looking at the direction to make it put away the weapon and stand still
                    if enemies[j][2] == 'l':
                        look = sprites[1][0]
                    else:
                        look = flippedSprites[1][0]
                    
                    # Tells the program that the enemy is no longer attacking
                    enemies[j][6] = False

                    # Setting the attacking timer back to 0
                    enemies[j][7] = 0
            
            # This checks if the walking timer on the enmy has reached the end
            if enemies[j][3] == 40:

                # If so, it resets the timer
                enemies[j][3] = 0
            
            # Displaying the enemy onto the window
            window.blit(look, (enemies[j][0], (enemies[j][1] / 10)))

            # This  will revert the previously changed x coordinate of the enemy, back to the original, if the attacking motion was to the left
            if look == sprites[1][2]:
                enemies[j][0] += 60

            # Finding out which floor the enemy should be using
            if enemies[j][0] < 680 and enemies[j][0] > 450 and enemies[j][1] < 4550:
                enemies[j][4] = 4450
            if enemies[j][0] < 1180 and enemies[j][0] > 950 and enemies[j][1] < 4550:
                enemies[j][4] = 4450
            if enemies[j][0] < 930 and enemies[j][0] > 700 and enemies[j][1] < 2150:
                enemies[j][4] = 2050
            if not(enemies[j][0] < 930 and enemies[j][0] > 700 and enemies[j][1] < 2150 or enemies[j][0] < 1180 and enemies[j][0] > 950 and enemies[j][1] < 4550 or enemies[j][0] < 680 and enemies[j][0] > 450 and enemies[j][1] < 4550):
                enemies[j][4] = 7550
            
            # Adding the vertical speed onto the enemy
            enemies[j][1] += enemies[j][5]

            # Applying gravity onto the vertical speed
            enemies[j][5] += gravity

            # Checking if the enemy is touchig their current floor
            if enemies[j][1] > (enemies[j][4] + 10):

                # Setting the y of the enemy to the y of the floor
                enemies[j][1] = enemies[j][4]

                # Setting the vertical speed of the enemy to 0
                enemies[j][5] = 0

            # Choosing a random number for random enemy jumping
            jump = random.randrange(0, 200)

            # Checking if the random number is 1, and the enemy is touching a floor
            if (jump == 1 or (character[3] < (enemies[j][1] - 2500) and enemies[j][0] < 1300 and enemies[j][0] > 300)) and enemies[j][1] == enemies[j][4]:

                # Increases the vertical speed of the enemy to make it jump
                enemies[j][5] = -140
            
            # For loop that is going to check if any of the bullets are touching the enemy
            for k in range(len(bullets)):

                # Checking if the bullet is touching the enemy
                if bullets[k][0] >= enemies[j][0] and bullets[k][0] <= (enemies[j][0] + 75) and bullets[k][1] >= enemies[j][1] and bullets[k][1] <= (enemies[j][1] + 1500) and not(k in toDel):
                    
                    # If it is, then it adds that enemy and the bullet to a list that will delete them later
                    toDel.append(k)
                    toDelEnemy.append(j)

                    # Adds one onto the kills
                    kills += 1

                    # This will change the time between spawns
                    if kills < len(timingsSpawns):

                        # Changing it to the value on the list that kills has reached
                        timeBetweenSpawns = timingsSpawns[kills]
                    else:

                        # If the kills have surpassed the length of the list, then the time between spawns will be 30
                        timeBetweenSpawns = 30
        
        # A for loop that will update the current state of the bullets
        for i in range(len(bullets)):

            # Checking which direction the bullet is moving in
            if bullets[i][2] == 'r':

                # Changing the bullets x coordinate to move in that direction
                bullets[i][0] += 20
            else:
                bullets[i][0] -= 20
            
            # Creating the bullet and placing it on the window
            pygame.draw.rect(window, colours[0], (bullets[i][0], (bullets[i][1] / 10), 6, 6))

            # Checking if the bullets has left the screen
            if bullets[i][0] > windowSize[0] or bullets[i][0] < -6:

                # Adding that bullet to the list, to be deleted later
                toDel.append(i)

        # Setting the value update the program's locating
        minus = 0

        # Loops that will delete every list item until the list is empty
        while toDel != []:

            # Checking that there is a bullet on the screen to delete
            if bullets != []:

                # Deleting the bullets from the list of bullets on the screen
                del bullets[(toDel[0] - minus)]

            # Deleting the bullet from the, to be deleted, list
            del toDel[0]

            # Increasing the variable by 1
            minus += 1

        # Setting the variable to 0 again for another use
        minus = 0

        # Loop that deletes the enemies from the screen that have been killed
        while toDelEnemy != []:

            # Deletes the enemy from the enemies list
            del enemies[(toDelEnemy[0] - minus)]

            # Deletes the value used from the, enemies to be deleted, list
            del toDelEnemy[0]

            # Increasing the variable by 1
            minus += 1

        # Checking if the character has walked off the screen
        if character[2] > windowSize[0] or character[2] < -60:

            # Shows the red screen to show that the player has walked off the screen
            window.blit(images[3], (0,0))

            # Decreases player's health for walking off the screen
            character[0] -= 4

        # Making the revolver image next to the ammo
        window.blit(images[2], (20, 20))

        # Making the ammo left
        window.blit(ammo, (180, 70))

        # Placing everything made, on to the pygame window
        pygame.display.flip()

        # Adding onto some timers
        timers[3] += 1
        timers[4] += 1

        # Checking if an event has happened
        for event in pygame.event.get():

            # Checking if the event is pressing the exit button
            if event.type == pygame.QUIT:

                # Closing the loop and program
                finished = True

            # Creating a bullet
            # Checking if the mouse has been pressed
            if event.type == pygame.MOUSEBUTTONDOWN:

                # Checking the player isn't reloading and there are bullets in the magazinw
                if not(reloading) and character[1] > 0:

                    # Resetting the bullets timer
                    timers[2] = 0

                    # Removing one bullet from the magazine
                    character[1] -= 1

                    # Creating the y coordinate of the bullet, which is where the gun is
                    y1 = character[3] + 540

                    # Checking what direction the player is
                    if character[5] == 'r':
                        
                        # Creating the original x of the bullet, since the player is facing right, the gun is going to be on the other side of the sprite
                        x1 = character[2] + 96
                    else:
                        x1 = character[2]
                    
                    # Placing the bullet attributes in the bullets list
                    bullets.append([x1, y1, character[5]])
        
        # Checking that the player hasn't run out of health
        if character[0] <= 0:

            # If the player has, then the leaderboard function will be called, and give the function the amount of kills
            leaderboard(kills)

            # The game loop is finished
            finished = True
        
        # Making it run at 50 repetitions per second
        clock.tick(50)

# Function for the leaderboard
def leaderboard(eliminations):

    # Opening the file that has the leaderbaord on it
    file = open('assets/leaderboard.txt', 'r')

    # Reading all of the file and storing it in the contents variable
    contents = file.read()

    # Making the contents variable a list with the scores
    contents = contents.split(',')

    # Creating the colour white
    white = pygame.color.Color('#ffffff')

    # Importing the font to be used
    font = pygame.font.Font('assets/fonts/stencilfont.ttf', 130)

    # List with all the texts to be used
    texts = [font.render(str(eliminations) + ' KILLS', False, white),font.render(contents[0] + ' KILLS', False, white),font.render(contents[1] + ' KILLS', False, white),font.render(contents[2] + ' KILLS', False, white),font.render(contents[3] + ' KILLS', False, white),font.render(contents[4] + ' KILLS', False, white)]
    
    # Loading in the leaderboard picture and chnaging it to the same size as the window
    leaderboard = pygame.image.load('assets/images/leaderboard.png')
    leaderboard = pygame.transform.scale(leaderboard, (windowSize[0], windowSize[1]))

    # Updating the leaderboard with the results of the game just playes
    if int(contents[0]) < int(eliminations):

        # Making a variable to temporarily hold information
        placeHolder = contents[0]

        # Switching that place in the leaderboard with the new score
        contents[0] = eliminations

        # Making that old place the new result to compare with
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

    # Opening the file again, but this time to write into it
    file = open('assets/leaderboard.txt', 'w')

    # Writing the new leaderboard into the file
    file.write(str(contents[0]) + ',' + str(contents[1]) + ',' + str(contents[2]) + ',' + str(contents[3]) + ',' + str(contents[4]))

    # Closing the file
    file.close()

    # Initialising some variables
    stage = False
    mouseDown = False

    # Initialising the variable to start the while loop
    resultsFinish = False
    
    # Loop that holds the leaderboard window
    while not resultsFinish:

        # Placing the leaderbard template into the window
        window.blit(leaderboard, (0,0))

        # Placing all the leadrboards contents in
        window.blit(texts[1], (450, 175))
        window.blit(texts[2], (450, 287))
        window.blit(texts[3], (450, 397))
        window.blit(texts[4], (450, 510))
        window.blit(texts[5], (450, 624))
        window.blit(texts[0], (450, 746))

        # Displaying everything
        pygame.display.flip()

        # Checking if the mouse has just been pressed
        if stage and mouseDown:

            # Calls the menu function to restart the program again
            menuTime()

            # Finish the leaderboard loop
            resultsFinish = True
        
        # Checking for any events in pygame
        for event in pygame.event.get():

            # Checking if this event was presing the exit
            if event.type == pygame.QUIT:

                # Closing the leaderboard loop and therefore the program
                resultsFinish = True
            
            # Checking if the mouse is being pressed
            if event.type == pygame.MOUSEBUTTONDOWN:

                # If the mouse is being pressed, then the variable gets set to true
                mouseDown = True
            else:

                # If not, the variable is set to false
                mouseDown = False

                # Variable that makes it so the mouse has to be let go of first in order to go back to the menu
                stage = True

# Calling the menu function to start the game
menuTime()

