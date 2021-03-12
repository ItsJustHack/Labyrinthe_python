from graphe import*
import pygame

class Player:
    def __init__(self,x_initial,y_initial, damier, graphe):
        self.x = x_initial
        self.y = y_initial
        self.damier = damier
        self.graphe = graphe
        self.image = pygame.image.load("assets/player.png")

    def turn_right(self):
        #self.damier[(3,1)]
        try:
            if not self.graphe.presence_arc(self.damier[( self.x+0.5 , self.y+0.5 )], self.damier[( self.x+0.5 , self.y-0.5 )]):
                self.x+=1
        except KeyError:
            print("Bien joué tu as résolu le labirynthe")

    def turn_left(self):
        if not self.graphe.presence_arc(self.damier[( self.x-0.5 , self.y+0.5 )], self.damier[( self.x-0.5 , self.y-0.5 )]):
            self.x-=1


    def turn_up(self):
        if not self.graphe.presence_arc(self.damier[( self.x-0.5 , self.y-0.5 )], self.damier[( self.x+0.5 , self.y-0.5 )]):
            self.y-=1

    def turn_down(self):
        if not self.graphe.presence_arc(self.damier[( self.x-0.5 , self.y+0.5 )], self.damier[( self.x+0.5 , self.y+0.5 )]):
            self.y+=1
