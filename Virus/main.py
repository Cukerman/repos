import pygame
import sys
import os
from window import Window 
from virus import Virus

def fill_in(cell1,cell2):
    v=Virus()
    for i in range(cell2+1):
        for j in range (cell1):
            cells=0,j,i
            v.add(cells)           

if __name__ == '__main__':
    v=Virus()
    width=640
    height=480
    cell_size=20
    cell1 = width//cell_size
    cell2 = height//cell_size
    fill_in(cell1,cell2)
    
    v.edit(32,1)

    game = Window(width, height, cell_size)
    game.run()
