import pygame
import sys
import os
from window import Window 
from virus import Virus
from bacterium import Bacterium
          

if __name__ == '__main__':
    
    width=640
    height=480
    cell_size=20
    cell1 = width//cell_size
    cell2 = height//cell_size
   

    game = Window(width, height, cell_size)
    game.run()
