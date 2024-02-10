import pygame
import random
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QCheckBox, QMessageBox
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtGui import QFont
import markdown
import pandas as pd

# --- pygame related functionalities ---

class PygameApp:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1280, 720))

    def start_landing_page(self):
        white = (255, 255, 255)
        black = (0, 0, 0)
        font_title = pygame.font.Font(None, 60)
        font_button = pygame.font.Font(None, 40)
        running = True

        while running:
            self.screen.fill(white)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if continue_button_rect.collidepoint(event.pos):
                        running = False  # Close the landing page
                        self.show_consent_form()

            title_text = font_title.render("FITTS TEST PROCEDURE", True, black)
            title_rect = title_text.get_rect(center=(1280 // 2, 150))
            self.screen.blit(title_text, title_rect)

            continue_button_text = font_button.render("Continue", True, white)
            continue_button_rect = pygame.Rect(1280 // 2 - 100, 300, 200, 50)
            pygame.draw.rect(self.screen, black, continue_button_rect)
            self.screen.blit(continue_button_text, continue_button_rect.move(25, 10))

            pygame.display.flip()

    def show_consent_form(self):
        pygame.quit()  # Close Pygame before starting PyQt application
        app = QApplication(sys.argv)
        consent_form = ConsentForm(self)
        consent_form.show()
        sys.exit(app.exec())

# --- PyQt6 related functionalities ---

def load_consent_text(file_path):
    with open(file_path, 'r') as file:
        md_text = file.read()
    return markdown.markdown(md_text)

class ConsentForm(QWidget):
    def __init__(self, pygame_app):
        super().__init__()
        self.pygame_app = pygame_app
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout(self)
        self.web_view = QWebEngineView()
        consent_html = load_consent_text("consent_form.md")
        self.web_view.setHtml(consent_html)
        layout.addWidget(self.web_view)

        self.setup_checkbox(layout)
        self.setup_buttons(layout)
        self.setLayout(layout)
        self.setWindowTitle('Consent Form')
        self.showMaximized()

    def setup_checkbox(self, layout):
        self.checkbox = QCheckBox('I agree to the terms and conditions', self)
        self.checkbox.setFont(QFont("Arial", 14))
        self.checkbox.setStyleSheet("QCheckBox { spacing: 10px; }")
        layout.addWidget(self.checkbox)
        self.checkbox.stateChanged.connect(self.onCheckboxChange)

    def setup_buttons(self, layout):
        self.agree_button = QPushButton('Agree', self)
        self.agree_button.setFont(QFont("Arial", 16))
        self.agree_button.setFixedHeight(40)
        self.agree_button.clicked.connect(self.onAgree)
        layout.addWidget(self.agree_button)

        decline_button = QPushButton('Decline', self)
        decline_button.setFont(QFont("Arial", 16))
        decline_button.setFixedHeight(40)
        decline_button.clicked.connect(self.onDecline)
        layout.addWidget(decline_button)

    def onCheckboxChange(self, state):
        if state == 2:
            self.agree_button.setStyleSheet("QPushButton { color: green; }")
        else:
            self.agree_button.setStyleSheet("")

    def onAgree(self):
        if self.checkbox.isChecked():
            self.close()
            game = Game()
            game.run_game()  # Start the game after consent
        else:
            QMessageBox.warning(self, 'Error', 'You must agree to the terms and conditions.', QMessageBox.StandardButton.Ok)

    def onDecline(self):
        sys.exit('User declined the consent form.')

class Game:
    def __init__(self):
        # pygame setup
        pygame.init()
        self.screen = pygame.display.set_mode((1280, 720))
        self.running = True

    def run_game(self):
        pygame.mouse.set_pos(self.screen.get_width() / 2, self.screen.get_height() / 2)
        square_size_options = [80, 120, 160, 200]
        distance_options = [100, 200, 300, 400, 700, 800, 900, 1000]
        square_size = random.choice(square_size_options)
        target = pygame.Rect(random.choice(distance_options), self.screen.get_height() / 2 - square_size / 2, square_size, square_size)
        data = []
        trial = 1
        errors = 0
        start_time = pygame.time.get_ticks()

        while self.running and trial <= 320:
            clicked = False
            # poll for events
            # pygame.QUIT event means the user clicked X to close your window
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        clicked = True

            # fill the screen with a color to wipe away anything from last frame
            self.screen.fill("black")

            pygame.draw.rect(self.screen, "blue", target)

            # flip() the display to put your work on screen
            pygame.display.flip()

            if clicked:
                if target.collidepoint(pygame.mouse.get_pos()):
                    # Successfully clicked the rectangle
                    # print("hit")
                    data.append([trial, square_size, target.x, abs(pygame.mouse.get_pos()[0]-(self.screen.get_width() / 2)), pygame.time.get_ticks()-start_time, errors])
                    pygame.mouse.set_pos(self.screen.get_width() / 2, self.screen.get_height() / 2)
                    square_size = random.choice(square_size_options)
                    target = pygame.Rect(random.choice(distance_options), self.screen.get_height() / 2 - square_size / 2, square_size, square_size)
                    trial += 1
                    errors = 0
                    start_time = pygame.time.get_ticks()
                else:
                    errors += 1

        data = pd.DataFrame(data, columns=["Trial", "Target Size (px)", "Target Starting x Position (px)", "Distance Mouse Traveled (px)", "Time (ms)", "Misses"])
        data.to_csv("fitts_data.csv", index=False)
        pygame.quit()

# --- Main Entry Point ---

def main():
    pygame_app = PygameApp()  # Initialize the Pygame App
    pygame_app.start_landing_page()  # Start with the landing page

if __name__ == "__main__":
    main()