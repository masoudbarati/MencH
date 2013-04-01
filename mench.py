import pygame
import random
import math
import socket

pygame.init()

class Mohre:
    def __init__(self,color1,pos1,num1):
        self.color = color1
        self.pos = pos1
        self.num = num1
        self.pic = pic1
    def moving(self,n):
        #/////
    def display(self):
        #/////
#//////////////////////////////////////
white = [255,255,255]
black = [0,0,0]
red = [225,0,0]
green = [0,147,0]
yellow = [255,255,0]
blue = [0,0,255]
#//////////////////////////////////////
class Field:
    def __init__(self):
        self.field = []
        for i in range(40):
            self.field.append(black)
        self.red_dest = [black,black,black,black]
        self.blue_dest = [black,black,black,black]
        self.green_dest = [black,black,black,black]
        self.yellow_dest = [black,black,black,black]
        self.red_rip = [red,red,red,red]
        self.blue_rip = [blue,blue,blue,blue]
        self.green_rip = [green,green,green,green]
        self.yellow_rip = [yellow,yellow,yellow,yellow]
    def display(self):
        pygame.draw.circle(screen,self.field[0],[235,535],25,4)
        pygame.draw.circle(screen,self.field[1],[235,485],25,4)
        pygame.draw.circle(screen,self.field[2],[235,435],25,4)
        pygame.draw.circle(screen,self.field[3],[235,385],25,4)
        pygame.draw.circle(screen,self.field[4],[235,335],25,4)
        pygame.draw.circle(screen,self.field[5],[185,335],25,4)
        pygame.draw.circle(screen,self.field[6],[135,335],25,4)
        pygame.draw.circle(screen,self.field[7],[85,335],25,4)
        pygame.draw.circle(screen,self.field[8],[35,335],25,4)
        pygame.draw.circle(screen,self.field[9],[35,285],25,4)
        pygame.draw.circle(screen,self.field[10],[35,235],25,4)
        pygame.draw.circle(screen,self.field[11],[85,235],25,4)
        pygame.draw.circle(screen,self.field[12],[135,235],25,4)
        pygame.draw.circle(screen,self.field[13],[185,235],25,4)
        pygame.draw.circle(screen,self.field[14],[235,235],25,4)
        pygame.draw.circle(screen,self.field[15],[235,185],25,4)
        pygame.draw.circle(screen,self.field[16],[235,135],25,4)
        pygame.draw.circle(screen,self.field[17],[235,85],25,4)
        pygame.draw.circle(screen,self.field[18],[235,35],25,4)
        pygame.draw.circle(screen,self.field[19],[285,35],25,4)
        pygame.draw.circle(screen,self.field[20],[335,35],25,4)
        pygame.draw.circle(screen,self.field[21],[335,85],25,4)
        pygame.draw.circle(screen,self.field[22],[335,135],25,4)
        pygame.draw.circle(screen,self.field[23],[335,185],25,4)
        pygame.draw.circle(screen,self.field[24],[335,235],25,4)
        pygame.draw.circle(screen,self.field[25],[385,235],25,4)
        pygame.draw.circle(screen,self.field[26],[435,235],25,4)
        pygame.draw.circle(screen,self.field[27],[485,235],25,4)
        pygame.draw.circle(screen,self.field[28],[535,235],25,4)
        pygame.draw.circle(screen,self.field[29],[535,285],25,4)
        pygame.draw.circle(screen,self.field[30],[535,335],25,4)
        pygame.draw.circle(screen,self.field[31],[485,335],25,4)
        pygame.draw.circle(screen,self.field[32],[435,335],25,4)
        pygame.draw.circle(screen,self.field[33],[385,335],25,4)
        pygame.draw.circle(screen,self.field[34],[335,335],25,4)
        pygame.draw.circle(screen,self.field[35],[335,385],25,4)
        pygame.draw.circle(screen,self.field[36],[335,435],25,4)
        pygame.draw.circle(screen,self.field[37],[335,485],25,4)
        pygame.draw.circle(screen,self.field[38],[335,535],25,4)
        pygame.draw.circle(screen,self.field[39],[285,535],25,4)
        ####
        pygame.draw.circle(screen,self.red_dest[0],[285,485],15,2)
        pygame.draw.circle(screen,self.red_dest[1],[285,435],15,2)
        pygame.draw.circle(screen,self.red_dest[2],[285,385],15,2)
        pygame.draw.circle(screen,self.red_dest[3],[285,335],15,2)
        pygame.draw.circle(screen,self.yellow_dest[0],[85,285],15,2)
        pygame.draw.circle(screen,self.yellow_dest[1],[135,285],15,2)
        pygame.draw.circle(screen,self.yellow_dest[2],[185,285],15,2)
        pygame.draw.circle(screen,self.yellow_dest[3],[235,285],15,2)
        pygame.draw.circle(screen,self.green_dest[0],[285,85],15,2)
        pygame.draw.circle(screen,self.green_dest[1],[285,135],15,2)
        pygame.draw.circle(screen,self.green_dest[2],[285,185],15,2)
        pygame.draw.circle(screen,self.green_dest[3],[285,235],15,2)
        pygame.draw.circle(screen,self.blue_dest[0],[485,285],15,2)
        pygame.draw.circle(screen,self.blue_dest[1],[435,285],15,2)
        pygame.draw.circle(screen,self.blue_dest[2],[385,285],15,2)
        pygame.draw.circle(screen,self.blue_dest[3],[335,285],15,2)
        ####
        pygame.draw.circle(screen,self.red_rip[0],[90,530],25,4)
        pygame.draw.circle(screen,self.red_rip[1],[40,480],25,4)
        pygame.draw.circle(screen,self.red_rip[2],[140,480],25,4)
        pygame.draw.circle(screen,self.red_rip[3],[90,430],25,4)
        pygame.draw.circle(screen,self.yellow_rip[0],[90,40],25,4)
        pygame.draw.circle(screen,self.yellow_rip[1],[40,90],25,4)
        pygame.draw.circle(screen,self.yellow_rip[2],[140,90],25,4)
        pygame.draw.circle(screen,self.yellow_rip[3],[90,140],25,4)
        pygame.draw.circle(screen,self.green_rip[0],[480,40],25,4)
        pygame.draw.circle(screen,self.green_rip[1],[430,90],25,4)
        pygame.draw.circle(screen,self.green_rip[2],[530,90],25,4)
        pygame.draw.circle(screen,self.green_rip[3],[480,140],25,4)
        pygame.draw.circle(screen,self.blue_rip[0],[480,530],25,4)
        pygame.draw.circle(screen,self.blue_rip[1],[430,480],25,4)
        pygame.draw.circle(screen,self.blue_rip[2],[530,480],25,4)
        pygame.draw.circle(screen,self.blue_rip[3],[480,430],25,4)
#//////////////////////////////////////
size = width, height = 1000, 570
screen = pygame.display.set_mode(size)
