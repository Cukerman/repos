import pygame
from pygame.locals import *
from virus import Virus

class Window:

    def __init__(self, width=640, height=480, cell=10, speed=10) :
        self.width = width
        self.height = height
        self.cell = cell
        self.screen = width, height
        self.screen = pygame.display.set_mode(self.screen)
        self.cell_width = self.width // self.cell
        self.cell_height = self.height // self.cell
        self.cells = self.cell_width*self.cell_height
        self.speed = speed

    def draw_lines(self) :  
        for x in range(0, self.width, self.cell):
            pygame.draw.line(self.screen, pygame.Color('black'), 
                (x, 0), (x, self.height))
        for y in range(0, self.height, self.cell):
            pygame.draw.line(self.screen, pygame.Color('black'), 
                (0, y), (self.width, y))
    def print(self):    
        v=Virus()
        for i in range(self.cells):
            cell=v.get(i)    
            y=cell[2]*self.cell
            if cell[1]==0:
                x=self.width-self.cell
                y-=self.cell
            else:    
                x=cell[1]*self.cell-self.cell
    
            if cell[0]==1:
                pygame.draw.rect(self.screen, pygame.Color('green'),
                (x,y,self.cell_width,self.cell_height))
            elif cell[0]==0:
                pygame.draw.rect(self.screen, pygame.Color('white'),
                (x,y,self.cell_width,self.cell_height))
            elif cell[0]==2:
                pygame.draw.rect(self.screen, pygame.Color('red'),
                (x,y,self.cell_width,self.cell_height))
            self.draw_lines()
    def qwe(self,x,y):
        y//=self.cell
        x//=self.cell
        
        if y==0:
            return x            
        return (y*self.cell_width)+x
    def run(self) :
        pygame.init()
        clock = pygame.time.Clock()
        pygame.display.set_caption('Game ')
        self.screen.fill(pygame.Color('white'))
        running = True
        v=Virus()
        while running:
            for event in pygame.event.get():
                clock.tick(self.speed)
                if event.type == QUIT:
                    running = False
                elif event.type==pygame.MOUSEBUTTONDOWN:
                    x,y=pygame.mouse.get_pos()
                    print (x,y)
                    print((x//self.cell),(y//self.cell))
                    if event.button==1:
                        v.edit(self.qwe(x,y)+1,1)
                    elif event.button==3:
                        v.edit(self.qwe(x,y)+1,2)  
                    elif event.button==2:
                        v.edit(self.qwe(x,y)+1,0)     
                self.draw_lines()
                self.print()
                pygame.display.flip()
                

        pygame.quit()


