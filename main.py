import pygame, random

def main():
    # pygame setup
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    running = True

    min_square_size = 20
    max_square_size = 200
    square_size = random.randint(min_square_size, max_square_size)
    target = pygame.Rect(random.randint(0, screen.get_width() - square_size), random.randint(0, screen.get_height() - square_size), square_size, square_size)

    while running:
        clicked = False
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    clicked = True

        # fill the screen with a color to wipe away anything from last frame
        screen.fill("black")

        pygame.draw.rect(screen, "blue", target)

        # flip() the display to put your work on screen
        pygame.display.flip()

        if clicked:
            if target.collidepoint(pygame.mouse.get_pos()):
                # Successfully clicked the rectangle
                print("hit")
                square_size = random.randint(min_square_size, max_square_size)
                target = pygame.Rect(random.randint(0, screen.get_width() - square_size), random.randint(0, screen.get_height() - square_size), square_size, square_size)
            else:
                print("You suck")

    pygame.quit()

if __name__ == "__main__":
    main()