import pygame
from random import randint
def game():

    pygame.init()

    # Set up the drawing window
    screen_width = 800
    screen_height = int(screen_width * 0.8)

    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Monkey")

    #"grass" patch
    color = (0,250,0)
    pygame.draw.rect(screen, color, pygame.Rect(1, 540, 800, 800))
    pygame.display.flip()

    #monkey image
    x = 650
    y = 590
    scale = 0.2
    img = pygame.image.load("images/monke.png")
    img = pygame.transform.scale(img, (img.get_width() * scale, img.get_height() * scale))
    rect = img.get_rect()
    rect.center = (x, y)

    #banana image
    bananaX = 640
    bananaY = -3000
    banana_peel = pygame.image.load("images/bpeel.webp")
    banana_peel = pygame.transform.scale(banana_peel, (banana_peel.get_width() * scale, banana_peel.get_height() * scale))
    Brect = banana_peel.get_rect(center = (bananaX, bananaY))

    #road image setup
    scale1 = 2.8
    road = pygame.image.load("images/road.png")
    road = pygame.transform.scale(road, (road.get_width() * scale1, road.get_height() * scale1))

    #car images 
    scale2 = .15

    redCarX = -300
    redCarY = 80 
    redCar = pygame.image.load("images/redCar.png")
    redCar = pygame.transform.scale(redCar, (redCar.get_width() * scale2, redCar.get_height() * scale2))
    Rrect = redCar.get_rect(center = (redCarX, redCarY))

    goldCarX = -300
    goldCarY = 80
    goldCar = pygame.image.load("images/goldCar.png")
    goldCar = pygame.transform.scale(goldCar, (goldCar.get_width() * scale2, goldCar.get_height() * scale2))
    GdRect = goldCar.get_rect(center = (goldCarX, goldCarY))

    greenCarX = -300
    greenCarY = 450
    greenCar = pygame.image.load("images/greenCar.png")
    greenCar = pygame.transform.scale(greenCar, (greenCar.get_width() * scale2, greenCar.get_height() * scale2))
    GnRect = greenCar.get_rect(center = (greenCarX, greenCarY))

    greyCarX = -300
    greyCarY = 260
    greyCar = pygame.image.load("images/greyCar.png")
    greyCar = pygame.transform.scale(greyCar, (greyCar.get_width() * scale2, greyCar.get_height() * scale2))
    GyRect = greyCar.get_rect(center = (greyCarX, greyCarY))

    #Base variables for lives, speed, and score
    speed = 3
    inRound = 3
    score = 0
    while inRound > 0:

        #for the second while loop
        run = True

        #Banana peel y values that correspond with each of the 3 lanes
        banana1Y = 410
        banana2Y = 220
        banana3Y = 50

        #Resets the x values for the cars 
        GnRect.x = -300
        Rrect.x = -300
        GyRect.x = -300
        GdRect.x = -300

        #The text on the screen base info
        White = (250, 250, 250)
        Black = (0, 0, 0)
        font = pygame.font.Font('font/Pixeltype.ttf', 80)
        livesNum = font.render(f"Lives {inRound}", True, White, Black)
        textRect = livesNum.get_rect()
        textRect.center = (400, 590)

        scoreNum = font.render(f"Score: {score}", True, White, Black)
        textRect1 = scoreNum.get_rect()
        textRect1.center = (150, 590)

        font1 = pygame.font.Font(None, 80)
        firstNum = font1.render("1", True, White, Black)
        textRect2 = firstNum.get_rect(center = (640, 410))

        secondNum = font1.render("2", True, White, Black)
        textRect3 = secondNum.get_rect(center = (640, 220))

        thirdNum = font1.render("3", True, White, Black)
        textRect4 = thirdNum.get_rect(center = (640, 50))



        #random num generator that helps determine which lane will send a car
        randomCar = randint(1,3)
        #random num generator that helps determine which lane the gold car will go down
        randomGoldCar = randint(1, 3)
        while run:

            #collision variables to detect collisions
            collideRed = pygame.Rect.colliderect(Rrect, Brect)
            collideGreen = pygame.Rect.colliderect(GnRect, Brect)
            collideGrey = pygame.Rect.colliderect(GyRect, Brect)
            collideGold = pygame.Rect.colliderect(GdRect, Brect)

            #Displays the road image properly
            screen.blit(road, (0, -50))

            #Once the speed hits 12 it will send a gold car down a lane and it is worth 10 points
            if speed == 12:
                randomCar = 4
                if randomGoldCar == 1 and GdRect.x <= 800:
                    GdRect.x += speed
                elif randomGoldCar == 2 and GdRect.x <= 800:
                    GdRect.y = 250
                    GdRect.x += speed
                elif randomGoldCar == 3 and GdRect.x <= 800:
                    GdRect.y = 460
                    GdRect.x += speed

            #the functionality from the random num generator above
            if randomCar == 1 and GnRect.x <= 800:
                GnRect.x += speed
            elif randomCar == 2 and Rrect.x <= 800:
                Rrect.x += speed
            elif randomCar == 3 and GyRect.x <= 800:
                GyRect.x += speed
            elif GnRect.x > 800 or Rrect.x > 800 or GyRect.x > 800:
                run = False
                inRound -= 1  
            


            #if statements that check to see if there was a collision and then increase score and round
            #also reset the banana peel after collision
            if collideRed:
                run = False
                Brect.y = -300
                score += 1
            elif collideGreen:
                run = False
                Brect.y = -300
                score += 1
            elif collideGrey:
                run = False
                Brect.y = -300
                score += 1
            elif collideGold:
                run = False
                Brect.y = -300
                score += 10
            
                      
            #What is responsible for putting the actual images and texts in the window
            screen.blit(livesNum, textRect)
            screen.blit(scoreNum, textRect1)
            screen.blit(firstNum, textRect2)
            screen.blit(secondNum, textRect3)
            screen.blit(thirdNum, textRect4)
            screen.blit(img, rect)
            screen.blit(banana_peel, Brect)
            screen.blit(redCar, Rrect)
            screen.blit(greyCar, GyRect)
            screen.blit(greenCar, GnRect)
            screen.blit(goldCar, GdRect)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                #if statements that put the banana peel in the lane when 1, 2, or 3 are clicked
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        Brect.y = banana1Y
                    elif event.key == pygame.K_2:
                        Brect.y = banana2Y
                    elif event.key == pygame.K_3:
                        Brect.y = banana3Y

            pygame.display.update()
        #increases the speed by .5 after each round
        speed += .5
 
    # Done! Time to quit.
    pygame.quit()

    #returns the score after the game is over so it can be put into the table 
    return score

