from button import button as bt
import pygame


class Menu:
    def __init__(self, laby, screen):
        pygame.init()
        pygame.display.set_caption("Labirynthe")  # changement du titre de la fenêtre

        self.screen = screen
        self.laby = laby

        self.base_font = pygame.font.Font(None, 32)
        width, height = 600, 600

        self.background_set("assets/background.png")
        # ============================
        # Button:
        self.quit_button = bt(
            (255, 255, 255), width / 2 - 125, height / 2, 250, 100, "Quitter"
        )
        self.start_button = bt(
            (255, 255, 255), width / 2 - 125, height / 2 - 150, 250, 100, "Démarer"
        )
        self.deco_button1 = bt(
            (255, 255, 255), width / 2 - 225, height / 2 - 232 - 20, 200, 50, "Taille :"
        )
        self.deco_button2 = bt(
            (255, 255, 255), width / 2 - 25, height / 2 - 232 - 20, 200, 50, ""
        )
        # ============================
        # Input:
        self.input_rect = pygame.Rect(width / 2 - 15, height / 2 - 245, 140, 32)
        self.user_text = "10"
        # ============================
        # liste des entrées possibles:
        self.entree = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

        running = True
        while running:

            self.redrawWindow()
            self.backgroundX -= 1.4
            self.backgroundX2 -= 1.4
            # ===================================================================
            # cette partie contient l'implémentation d'easter egg, des petits secrets qui ne servent à rien
            if self.user_text == "thebeaf":
                self.background_set("assets/background.jpg")
                self.user_text = ""

            if self.user_text == "reverse":
                self.background_set("assets/background.png")
                self.user_text = ""

            if self.user_text == "alexcendrenoel":
                self.background_set("assets/meme.png")
                self.user_text = ""

            if self.user_text == "???????????????????????????????????????????????":
                self.background = pygame.image.load("assets/meme2.png")
                self.background_set("assets/meme2.png")
                self.user_text = ""

            self.secret_button = bt((0, 0, 0), 0, 0, 3, 3, "")
            # =====================================================================

            if self.backgroundX < self.background.get_width() * -1:
                self.backgroundX = self.background.get_width()

            if self.backgroundX2 < self.background.get_width() * -1:
                self.backgroundX2 = self.background.get_width()

            for event in pygame.event.get():

                mouse = pygame.mouse.get_pos()

                if self.quit_button.isOver(mouse):
                    self.quit_button.color = (155, 0, 0)
                else:
                    self.quit_button.color = (255, 255, 255)

                if self.start_button.isOver(mouse):
                    self.start_button.color = (0, 155, 0)
                else:
                    self.start_button.color = (255, 255, 255)

                if event.type == pygame.QUIT:
                    pygame.quit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.quit_button.isOver(mouse):
                        running = False
                        pygame.quit()
                    if self.secret_button.isOver(mouse):
                        self.background_set("assets/secret.png")

                    if self.start_button.isOver(mouse):
                        self.test_entree()
                        self.laby(int(self.user_text))

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        self.test_entree()
                        self.laby(int(self.user_text))

                    if event.key == pygame.K_BACKSPACE:
                        self.user_text = self.user_text[:-1]
                    else:
                        self.user_text += event.unicode

    def redrawWindow(self):
        self.screen.fill(("black"))
        self.screen.blit(self.background, (self.backgroundX, 0))
        self.screen.blit(self.background, (self.backgroundX2, 0))
        self.quit_button.draw(self.screen, (155, 0, 0))
        self.start_button.draw(self.screen, (0, 155, 0))
        self.deco_button1.draw(self.screen, (0, 0, 0))
        self.deco_button2.draw(self.screen, (0, 0, 0))

        pygame.draw.rect(self.screen, (255, 255, 255), self.input_rect, 2)
        text_surface = self.base_font.render(self.user_text, True, (0, 0, 0))
        self.screen.blit(text_surface, (self.input_rect.x + 5, self.input_rect.y + 5))
        pygame.display.update()

    def test_entree(self):
        if self.user_text == "":
            self.user_text = "10"
        else:
            for i in self.user_text:
                if i not in self.entree:
                    self.user_text = "10"

    def background_set(self, chemin):
        self.background = pygame.image.load(chemin)
        self.backgroundX = 0
        self.backgroundX2 = self.background.get_width()
