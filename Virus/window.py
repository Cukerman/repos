import pygame
from pygame.locals import *
from virus import Virus
from bacterium import Bacterium
import random

class Window:

    def __init__(self, width=640, height=480, cell=2, speed=10,virus=Virus(), bacterium=Bacterium()) :
        self.width = width
        self.height = height
        self.cell = cell
        self.screen = width, height
        self.screen = pygame.display.set_mode(self.screen)
        self.cell_width = self.width // self.cell
        self.cell_height = self.height // self.cell
        self.cells = self.cell_width*self.cell_height
        self.speed = speed
        self.v = virus
        self.b = bacterium
    def draw_lines(self) :  
        self.screen.fill(pygame.Color('white'))
        for x in range(0, self.width, self.cell):
            pygame.draw.line(self.screen, pygame.Color('black'), 
                (x, 0), (x, self.height))
        for y in range(0, self.height, self.cell):
            pygame.draw.line(self.screen, pygame.Color('black'), 
                (0, y), (self.width, y))
    def print(self):                  
        for i in self.v.get():
            y=i[1]*self.cell
            if i[0]==0:
                x=self.width-self.cell
                y-=self.cell
            else:    
                x=i[0]*self.cell-self.cell    
            pygame.draw.rect(self.screen, pygame.Color('green'),
            (x+1,y+1,self.cell-1,self.cell-1))
        for i in self.b.get():
            y=i[1]*self.cell
            if i[0]==0:
                x=self.width-self.cell
                y-=self.cell
            else:    
                x=i[0]*self.cell-self.cell    
            pygame.draw.rect(self.screen, pygame.Color('red'),
            (x+1,y+1,self.cell-1,self.cell-1))   

    def step(self):
        if self.v.len()==0:
            return
        for i in self.v.get():
            c=[]
            c.append(i[0])
            c.append(i[1])
            self.v.step(i,self.cell_width,self.cell_height)
            
            # if self.v.search(c) and self.b.search(c):
            #     self.v.edit(c)
            
            if random.randint(0,101)<=10:
                self.v.edit(c)

            
           
    def run(self) :
        pygame.init()
        clock = pygame.time.Clock()
        pygame.display.set_caption('Game ')
        

        running = True
        
        b=Bacterium()
        while running:
            clock.tick(self.speed)
            for event in pygame.event.get():
                
                if event.type == QUIT:
                    running = False
                elif event.type==pygame.MOUSEBUTTONDOWN:
                    x,y=pygame.mouse.get_pos()
                    print (x,y,'координаты')
                    print((x//self.cell),(y//self.cell),'квадратик')
                    if event.button==1:
                        s=[(x//self.cell)+1,y//self.cell]
                        if self.b.search(s):    
                            self.v.edit(s)
                            print('зел')
                    elif event.button==3:
                        s=[(x//self.cell)+1,y//self.cell]
                        if self.v.search(s):
                            self.b.edit(s)
                            print('крас')
                    elif event.button==2:
                        s=[(x//self.cell)+1,y//self.cell]    
                        if not self.v.search(s):
                            self.v.dell(s)
                        elif not self.b.search(s):
                            self.b.dell(s)
                # elif event.type==pygame.KEYDOWN:
                #     if event.key==K_p:
                        
            self.draw_lines()
            self.print()
            self.step()
            pygame.display.flip()
                

        pygame.quit()


