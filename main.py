import pygame
import random

def main():
    # Example file showing a circle moving on screen

    # pygame setup
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()
    running = True
    dt = 0

    # player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
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

        # pygame.draw.circle(screen, "red", player_pos, 40)
        pygame.draw.rect(screen, "blue", target)

        # flip() the display to put your work on screen
        pygame.display.flip()

        if clicked:
            if target.collidepoint(pygame.mouse.get_pos()):
                # Successfully clicked the rectangle
                print("hit")
                square_size = random.randint(min_square_size, max_square_size)
                target = pygame.Rect(random.randint(0, screen.get_width() - square_size), random.randint(0, screen.get_height() - square_size), square_size, square_size)

        # limits FPS to 60
        # dt is delta time in seconds since last frame, used for framerate-
        # independent physics.
        # dt = clock.tick(60) / 1000

    pygame.quit()

if __name__ == "__main__":
    main()