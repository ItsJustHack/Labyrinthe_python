from labyrinthe import creer_labirynthe, affiche_ecran, affiche_sortie
from player import Player
from random import randint
import pygame
import time
import os

def laby(taille):
    os.system("clear")
    #taille = int(input("Combien de largeur ?"))

    pygame.init()
    screen = pygame.display.set_mode((600,600))
    pygame.display.set_caption("Labirynthe")

    RUNNING = True
    #while RUNNING:
    labyrinthe = creer_labirynthe(taille, screen)
    a, damier, solution = labyrinthe[0], labyrinthe[1], labyrinthe[2]


        #time.sleep(3)
    player = Player(0.5, 0.5, damier, a)


    while RUNNING:

        screen.blit(player.image, ((player.x * 600 - 100) / taille, (player.y * 600 - 100) / taille))
        
        pygame.display.update()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                RUNNING = False

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_RIGHT:
                    player.turn_right()
                    time.sleep(0.1)
                    affiche_ecran(a, taille, screen)
                    """if (player.x,player.y)==fin:
                        RUNNING = False"""

                if event.key == pygame.K_LEFT:
                    player.turn_left()
                    time.sleep(0.1)
                    affiche_ecran(a, taille, screen)

                if event.key == pygame.K_UP:
                    player.turn_up()
                    time.sleep(0.1)
                    affiche_ecran(a, taille, screen)

                if event.key == pygame.K_DOWN:
                    player.turn_down()
                    time.sleep(0.1)
                    affiche_ecran(a, taille, screen)
                
                if event.key == pygame.K_F1:
                    affiche_sortie(solution, taille, screen)


from button import button as bt

def menu():
    pygame.init()  
    
    win = pygame.display.set_mode((500,500))
    win.fill((0,0,0))

    res = (600,600)  
    
    screen = pygame.display.set_mode(res)  
    
    width = screen.get_width()  
    height = screen.get_height()   

    base_font = pygame.font.Font(None,32)

    #============================
    #Button:
    quit_button = bt((255,255,255),width/2-125,height/2,250,100,'quit')
    start_button = bt((255,255,255),width/2-125,height/2-150,250,100,'game start')
    deco_button1 = bt((255,255,255),width/2-225,height/2-232-20, 200,50,'size set :')
    deco_button2 = bt((255,255,255),width/2-25,height/2-232-20, 200,50,'')
    #============================
    #Input:
    input_rect = pygame.Rect(width/2-15,height/2-245,140,32)
    user_text=''
    #============================



    def redrawWindow():
        win.fill((0,0,0))
        quit_button.draw(win, (155,0,0))
        start_button.draw(win, (0,155,0))
        deco_button1.draw(win, (0,0,0))
        deco_button2.draw(win, (0,0,0))

        pygame.draw.rect(win, (255,255,255),input_rect,2)
        text_surface = base_font.render(user_text, True, (0,0,0))
        win.blit(text_surface,(input_rect.x + 5, input_rect.y + 5))
        pygame.display.update()

    while True:  
        redrawWindow()
        for event in pygame.event.get():  
            
            if event.type == pygame.QUIT:  
                pygame.quit()   

            if event.type == pygame.MOUSEBUTTONDOWN:
                if quit_button.isOver(mouse):
                    pygame.quit()
                if start_button.isOver(mouse):
                    laby(int(user_text))
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    user_text=user_text[:-1]
                else:
                    user_text += event.unicode

    
        
        mouse = pygame.mouse.get_pos()

menu()