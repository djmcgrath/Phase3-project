import pygame

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

    #road image setup
    road = pygame.image.load("images/road.png")
    scale1 = 2.8
    road = pygame.transform.scale(road, (road.get_width() * scale1, road.get_height() * scale1))
  

    #monkey image
    x = 400
    y = 590
    scale = 0.2
    img = pygame.image.load("images/monke.png")
    img = pygame.transform.scale(img, (img.get_width() * scale, img.get_height() * scale))
    rect = img.get_rect()
    rect.center = (x, y)

    # #banana image
    # banana_peel = pygame.image.load("images/bpeel.webp")

    # #car images 
    # redCar = pygame.image.load("images/redCar.png")
    # goldCar = pygame.image.load("images/goldCar.png")
    # greenCar = pygame.image.load("images/greenCar.png")
    # greyCar = pygame.image.load("images/greyCar.png")

    # Run until the user asks to quit
    run = True
    while run:

        screen.blit(img, rect)
        screen.blit(road, (1, - 50))

        # Did the user click the window close button?
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()

    # Done! Time to quit.
    pygame.quit()


game()