#!/usr/bin/env python
import pygame
import sys

pygame.init()
size = (512,512)
dim = 32 # amount of pixes height and width of ledmatrix
screen = pygame.display.set_mode(size)

while True:
    while sys.stdin.read(1) != '\x01':
        pass
    for row in range(dim):
        for col in range(dim):
            r,g,b = sys.stdin.read(3)
            color = (ord(r),ord(g),ord(b))
            
            pygame.draw.rect(screen, color, [16*col, 16*row, 16, 16])
    pygame.display.flip()
