import pygame

def game():

    pygame.init()

    # Set up the drawing window
    screen_width = 800
    screen_height = int(screen_width * 0.8)

    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Monkey")

    x = 400
    y = 590
    scale = 0.2
    img = pygame.image.load("images/monke.png")
    img = pygame.transform.scale(img, (img.get_width() * scale, img.get_height() * scale))
    rect = img.get_rect()
    rect.center = (x, y)

    # Run until the user asks to quit
    run = True
    while run:

        screen.blit(img, rect)

        # Did the user click the window close button?
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()

    # Done! Time to quit.
    pygame.quit()


game()