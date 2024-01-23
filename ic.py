import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QCheckBox, QMessageBox
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtGui import QFont
import markdown
import pygame
import random

def load_consent_text(file_path):
    with open(file_path, 'r') as file:
        md_text = file.read()
        html = markdown.markdown(md_text)
        return html

class ConsentForm(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout(self)

        # Web Engine View to display Markdown as HTML
        self.web_view = QWebEngineView()
        consent_html = load_consent_text("consent_form.md")
        self.web_view.setHtml(consent_html)
        layout.addWidget(self.web_view)

        # Checkbox
        self.checkbox = QCheckBox('I agree to the terms and conditions', self)
        checkbox_font = QFont("Arial", 14)  # Set font and size
        self.checkbox.setFont(checkbox_font)
        self.checkbox.setStyleSheet("QCheckBox { spacing: 10px; }")  # Increase spacing
        layout.addWidget(self.checkbox)
        self.checkbox.stateChanged.connect(self.onCheckboxChange)

        # Agree Button
        self.agree_button = QPushButton('Agree', self)
        agree_button_font = QFont("Arial", 16)  # Set font and size
        self.agree_button.setFont(agree_button_font)
        self.agree_button.setFixedHeight(40)  # Set fixed height
        self.agree_button.clicked.connect(self.onAgree)
        layout.addWidget(self.agree_button)

        # Decline Button
        decline_button = QPushButton('Decline', self)
        decline_button.setFont(agree_button_font)
        decline_button.setFixedHeight(40)  # Set fixed height
        decline_button.clicked.connect(self.onDecline)
        layout.addWidget(decline_button)

        self.setLayout(layout)
        self.setWindowTitle('Consent Form')
        self.showMaximized()
        # self.setGeometry(300, 300, 350, 250)

    def onCheckboxChange(self, state):
        if state == 2:  # Checkbox is checked
            self.agree_button.setStyleSheet("QPushButton { color: green; }")
        else:
            self.agree_button.setStyleSheet("")

    def onAgree(self):
        if self.checkbox.isChecked():
            self.close()
            game()
        else:
            QMessageBox.warning(self, 'Error', 'You must agree to the terms and conditions.', QMessageBox.StandardButton.Ok)

    def onDecline(self):
        sys.exit('User declined the consent form.')

def game():
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

    pygame.quit()

# PyQt6 Application
app = QApplication(sys.argv)
consent_form = ConsentForm()
consent_form.show()
sys.exit(app.exec())


