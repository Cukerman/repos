import pygame
from pygame.locals import *
from virus import Virus
from bacterium import Bacterium
import random
from simulation import Simulation

class Window:

    def __init__(self, width=640, height=480, cell=2, speed=5) :
        self.width = width
        self.height = height
        self.cell = cell
        self.screen = width, height
        self.screen = pygame.display.set_mode(self.screen)
        self.cell_width = self.width // self.cell
        self.cell_height = self.height // self.cell
        self.cells = self.cell_width*self.cell_height
        self.speed = speed
        self.s =  Simulation()
    def draw_lines(self) :  
        self.screen.fill(pygame.Color('white'))
        for x in range(0, self.width, self.cell):
            pygame.draw.line(self.screen, pygame.Color('black'), 
                (x, 0), (x, self.height))
        for y in range(0, self.height, self.cell):
            pygame.draw.line(self.screen, pygame.Color('black'), 
                (0, y), (self.width, y))
    def print(self):                  
        for i in self.s.getItems():
            f=i.get()
            y=f[1]*self.cell
            if f[0]==0:
                x=self.width-self.cell
                y-=self.cell
            else:    
                x=f[0]*self.cell-self.cell    
            pygame.draw.rect(self.screen, pygame.Color(i.color()),
            (x+1,y+1,self.cell-1,self.cell-1))   

    def pause(self):
        clock = pygame.time.Clock()
        while True:
            self.draw_lines()
            self.print()
            for event in pygame.event.get():
                clock.tick(self.speed)
                if event.type == QUIT:
                    exit()
                elif event.type==pygame.MOUSEBUTTONDOWN:
                    x,y=pygame.mouse.get_pos()
                    if event.button==1:                      
                        self.s.add(Virus((x//self.cell)+1,y//self.cell,5))
                        self.draw_lines()
                        self.print()
                    elif event.button==3:
                        self.s.add(Bacterium((x//self.cell)+1,y//self.cell))
                        self.draw_lines()
                        self.print()
                    elif event.button==2:
                        s=[(x//self.cell)+1,y//self.cell]  
                        i=self.s.search(s,False) 
                        print (i)
                        if i!=None: 
                            self.s.remove(i)
                        self.draw_lines()
                        self.print()
                elif event.type==pygame.KEYDOWN:
                    if event.key==K_p:
                        return
                    elif event.key==K_SPACE:
                        self.s.step(self.cell_width,self.cell_height)
                        self.draw_lines()
                        self.print()
                        pygame.display.flip() 
            pygame.display.flip()       
               
           
    def run(self) :
        pygame.init()
        clock = pygame.time.Clock()
        pygame.display.set_caption('Game ')
        
        while True:
            clock.tick(self.speed)
            for event in pygame.event.get():
                
                if event.type == QUIT:
                    exit()
                elif event.type==pygame.MOUSEBUTTONDOWN:
                    x,y=pygame.mouse.get_pos()
                    if event.button==1:                      
                        self.s.add(Virus((x//self.cell)+1,y//self.cell,10))
                    elif event.button==3:
                        self.s.add(Bacterium((x//self.cell)+1,y//self.cell))
                    elif event.button==2:
                        s=[(x//self.cell)+1,y//self.cell]  
                        i=self.s.search(s,False) 
                        print (i)
                        if i!=None: 
                            self.s.remove(i)
                elif event.type==pygame.KEYDOWN:
                    if event.key==K_p:
                        self.pause()
                    
                        
            self.draw_lines()
            self.print()
            self.s.step(self.cell_width,self.cell_height)
            pygame.display.flip()
                

        pygame.quit()


