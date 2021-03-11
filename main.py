from labyrinthe import creer_labirynthe
import pygame


taille = int(input("Combien de largeur ?"))

pygame.init()
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption("Echecs")

RUNNING = True
a = creer_labirynthe(taille, screen)

while RUNNING:
    # mettre à jour l'écran
    for arc in a.arcs:
        x = (arc.s_origine.pos[0] * 2 /taille, arc.s_origine.pos[1] * 2 /taille)
        y = (arc.s_extremite.pos[0] * 2 /taille, arc.s_extremite.pos[1] * 2 /taille)
        pygame.draw.line(screen, "white", x, y, 1)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False
