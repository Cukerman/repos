import pygame
from pygame.locals import *
from virus import Virus
from bacterium import Bacterium
import random
from simulation import Simulation

class Window:

    def __init__(self, width=640, height=480, cell=2, speed=10) :
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
        # for i in self.b.get():
        #     y=f[1]*self.cell
        #     if i[0]==0:
        #         x=self.width-self.cell
        #         y-=self.cell
        #     else:    
        #         x=f[0]*self.cell-self.cell    
        #     pygame.draw.rect(self.screen, pygame.Color('red'),
        #     (x+1,y+1,self.cell-1,self.cell-1))   

    # def step(self):
    #     if self.v.len()==0:
    #         return
    #     for i in self.v.get():
    #         c=[]
    #         c.append(i[0])
    #         c.append(i[1])
    #         self.v.step(i,self.cell_width,self.cell_height)
            
            # if self.v.search(c) and self.b.search(c):
            #     self.v.edit(c)
            
    #         if random.randint(0,101)<=10:
    #             self.v.edit(c)

            
           
    def run(self) :
        pygame.init()
        clock = pygame.time.Clock()
        pygame.display.set_caption('Game ')
        

        running = True
        
        
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
                        self.s.add(Virus((x//self.cell)+1,y//self.cell))
                        print('зел')
                    elif event.button==3:
                        self.s.add(Bacterium((x//self.cell)+1,y//self.cell))
                        print('крас')
                    elif event.button==2:
                        s=[(x//self.cell)+1,y//self.cell]    
                        
                # elif event.type==pygame.KEYDOWN:
                #     if event.key==K_p:
                        
            self.draw_lines()
            self.print()
            # self.step()
            pygame.display.flip()
                

        pygame.quit()


