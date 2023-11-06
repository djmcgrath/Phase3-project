import pygame
from random import randint
def game():

    pygame.init()

    # Set up the drawing window
    screen_width = 800
    screen_height = int(screen_width * 0.8)

    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Monkey")

    # def send_car ()


    #"grass" patch
    color = (0,250,0)
    pygame.draw.rect(screen, color, pygame.Rect(1, 540, 800, 800))
    pygame.display.flip()

    #road image setup
    road = pygame.image.load("images/road.png")
    scale1 = 2.8
    road = pygame.transform.scale(road, (road.get_width() * scale1, road.get_height() * scale1))
  

    #monkey image
    x = 650
    y = 590
    scale = 0.2
    img = pygame.image.load("images/monke.png")
    img = pygame.transform.scale(img, (img.get_width() * scale, img.get_height() * scale))
    rect = img.get_rect()
    rect.center = (x, y)

    #banana image
    banana_peel = pygame.image.load("images/bpeel.webp")
    scale2 = .15
    banana_peel = pygame.transform.scale(banana_peel, (banana_peel.get_width() * scale, banana_peel.get_height() * scale))

    #car images 
    redCar = pygame.image.load("images/redCar.png")
    redCar = pygame.transform.scale(redCar, (redCar.get_width() * scale2, redCar.get_height() * scale2))

    goldCar = pygame.image.load("images/goldCar.png")
    goldCar = pygame.transform.scale(goldCar, (goldCar.get_width() * scale2, goldCar.get_height() * scale2))

    greenCar = pygame.image.load("images/greenCar.png")
    greenCar = pygame.transform.scale(greenCar, (greenCar.get_width() * scale2, greenCar.get_height() * scale2))

    greyCar = pygame.image.load("images/greyCar.png")
    greyCar = pygame.transform.scale(greyCar, (greyCar.get_width() * scale2, greyCar.get_height() * scale2))

    #Round # text
    White = (250, 250, 250)
    Black = (0, 0, 0)
    font = pygame.font.Font('freesansbold.ttf', 50)
    roundNum = font.render("Round 1", True, White, Black)
    textRect = roundNum.get_rect()
    textRect.center = (400, 590)

    #X and Y variables for the different color cars and banana positions in the 3 lanes and speed for how fast the car goes
    greenCarX = -300
    greenCarY = 380

    redCarX = -300
    redCarY = 30

    greyCarX = -300
    greyCarY = 200

    bananaX = 620
    banana1Y = 50
    banana2Y = 230
    banana3Y = 410

    speed = 4

    randomCar = randint(1,3)

    # Run until the user asks to quit
    run = True
    while run:

        screen.blit(road, (0, -50))

        if randomCar == 1:
            greenCarX += speed
        elif randomCar == 2:
            redCarX += speed
        else:
            greyCarX += speed
        
        
        screen.blit(roundNum, textRect)
        screen.blit(img, rect)
        screen.blit(redCar, (redCarX, redCarY))
        screen.blit(greyCar, (greyCarX, greyCarY))
        screen.blit(greenCar, (greenCarX, greenCarY))
        
        
        
        

        # Did the user click the window close button?
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    screen.blit(banana_peel, (bananaX, banana1Y))
                elif event.key == pygame.K_2:
                    screen.blit(banana_peel, (bananaX, banana2Y))
                elif event.key == pygame.K_3:
                    screen.blit(banana_peel, (bananaX, banana3Y))


        pygame.display.update()

    # Done! Time to quit.
    pygame.quit()


game()