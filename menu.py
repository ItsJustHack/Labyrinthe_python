from button import button as bt
import pygame


class Menu:


    def __init__(self, laby, screen):
        pygame.init()
      
        self.screen = screen    
        self.laby = laby

        self.base_font = pygame.font.Font(None,32)
        width, height = 600,600
        #============================
        #Button:
        self.quit_button = bt((255,255,255),width/2-125,height/2,250,100,'quit')
        self.start_button = bt((255,255,255),width/2-125,height/2-150,250,100,'game start')
        self.deco_button1 = bt((255,255,255),width/2-225,height/2-232-20, 200,50,'size set :')
        self.deco_button2 = bt((255,255,255),width/2-25,height/2-232-20, 200,50,'')
        #============================
        #Input:
        self.input_rect = pygame.Rect(width/2-15,height/2-245,140,32)
        self.user_text=''
        #============================

        running = True
        while running:  
            
            self.redrawWindow()
            for event in pygame.event.get():  

                mouse = pygame.mouse.get_pos()

                
                if event.type == pygame.QUIT:  
                    pygame.quit()   

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.quit_button.isOver(mouse):
                        running = False
                        pygame.quit()

                    if self.start_button.isOver(mouse):
                        self.laby(int(self.user_text))
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        self.user_text=self.user_text[:-1]
                    else:
                        self.user_text += event.unicode

    def redrawWindow(self):
        self.screen.fill(("black"))
        self.quit_button.draw(self.screen, (155,0,0))
        self.start_button.draw(self.screen, (0,155,0))
        self.deco_button1.draw(self.screen, (0,0,0))
        self.deco_button2.draw(self.screen, (0,0,0))

        pygame.draw.rect(self.screen, (255,255,255),self.input_rect,2)
        text_surface = self.base_font.render(self.user_text, True, (0,0,0))
        self.screen.blit(text_surface,(self.input_rect.x + 5, self.input_rect.y + 5))
        pygame.display.update()

    
        
