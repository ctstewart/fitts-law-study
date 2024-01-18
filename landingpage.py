import pygame
import sys


# Function to be executed when the "Continue" button is clicked
def continue_button():
    print("Continue button clicked!")


def start_landing_page():

    # Set up colors
    white = (255, 255, 255)
    black = (0, 0, 0)


    # pygame setup
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    running = True


    # Set up fonts
    font_title = pygame.font.Font(None, 60)  # Use None for the default font
    font_button = pygame.font.Font(None, 40)

    while running:
        clicked = False
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                            # Check if the mouse click is within the "Continue" button area
                            if continue_button_rect.collidepoint(event.pos):
                                continue_button()

        # Clear the screen
        screen.fill(white)

        # Draw the title
        title_text = font_title.render("FITTS TEST PROCEDURE", True, black)
        title_rect = title_text.get_rect(center=(1280 // 2, 150))
        screen.blit(title_text, title_rect)

        # Draw the "Continue" button
        continue_button_text = font_button.render("Continue", True, white)
        continue_button_rect = pygame.Rect(
            (1280 // 2 - 100, 300, 200, 50)
        )  # Button dimensions
        pygame.draw.rect(screen, black, continue_button_rect)
        screen.blit(continue_button_text, continue_button_rect.move(25, 10))

        # Update the display
        pygame.display.flip()


    pygame.quit()

if __name__ == "__main__":
    start_landing_page()