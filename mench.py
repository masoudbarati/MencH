import pygame
import random
import math

pygame.init()

class Piece:
    def __init__(self,color1,pos1,pic1):
        self.color = color1
        self.pos = pos1
        self.pic = pic1
    def moving(self,n):
        pass
#//////////////////////////////////////
white = [255,255,255]
black = [0,0,0]
red = [225,0,0]
green = [0,147,0]
yellow = [255,255,0]
blue = [0,0,255]
#//////////////////////////////////////
def get_pos(num):
    if num == 0:
        return [235,535]
    elif num == 1:
        return [235,485]
    elif num == 2:
        return [235,435]
    elif num == 3:
        return [235,385]
    elif num == 4:
        return [235,335]
    elif num == 5:
        return [185,335]
    elif num == 6:
        return [135,335]
    elif num == 7:
        return [85,335]
    elif num == 8:
        return [35,335]
    elif num == 9:
        return [35,285]
    elif num == 10:
        return [35,235]
    elif num == 11:
        return [85,235]
    elif num == 12:
        return [135,235]
    elif num == 13:
        return [185,235]
    elif num == 14:
        return [235,235]
    elif num == 15:
        return [235,185]
    elif num == 16:
        return [235,135]
    elif num == 17:
        return [235,85]
    elif num == 18:
        return [235,35]
    elif num == 19:
        return [285,35]
    elif num == 20:
        return [335,35]
    elif num == 21:
        return [335,85]
    elif num == 22:
        return [335,135]
    elif num == 23:
        return [335,185]
    elif num == 24:
        return [335,235]
    elif num == 25:
        return [385,235]
    elif num == 26:
        return [435,235]
    elif num == 27:
        return [485,235]
    elif num == 28:
        return [535,235]
    elif num == 29:
        return [535,285]
    elif num == 30:
        return [535,335]
    elif num == 31:
        return [485,335]
    elif num == 32:
        return [435,335]
    elif num == 33:
        return [385,335]
    elif num == 34:
        return [335,335]
    elif num == 35:
        return [335,385]
    elif num == 36:
        return [335,435]
    elif num == 37:
        return [335,485]
    elif num == 38:
        return [335,535]
    elif num == 39:
        return [285,535]
    elif num == 40:
        return [285,485]
    elif num == 41:
        return [285,435]
    elif num == 42:
        return [285,385]
    elif num == 43:
        return [285,335]
    elif num == 44:
        return [85,285]
    elif num == 45:
        return [135,285]
    elif num == 46:
        return [185,285]
    elif num == 47:
        return [235,285]
    elif num == 48:
        return [285,85]
    elif num == 49:
        return [285,135]
    elif num == 50:
        return [285,185]
    elif num == 51:
        return [285,235]
    elif num == 52:
        return [485,285]
    elif num == 53:
        return [435,285]
    elif num == 54:
        return [385,285]
    elif num == 55:
        return [335,285]
    elif num == 56:
        return [90,530]
    elif num == 57:
        return [40,480]
    elif num == 58:
        return [140,480]
    elif num == 59:
        return [90,430]
    elif num == 60:
        return [90,40]
    elif num == 61:
        return [40,90]
    elif num == 62:
        return [140,90]
    elif num == 63:
        return [90,140]
    elif num == 64:
        return [480,40]
    elif num == 65:
        return [430,90]
    elif num == 66:
        return [530,90]
    elif num == 67:
        return [480,140]
    elif num == 68:
        return [480,530]
    elif num == 69:
        return [430,480]
    elif num == 70:
        return [530,480]
    elif num == 71:
        return [480,430]
#//////////////////////////////////////
class Field:
    def __init__(self):
        self.field = []                   #  0-39 -->main field 
        for i in range(56):               #  40-55 -->players goal
            self.field.append(black)      #  56-71 -->players repository
        for i in range(4):
            self.field.append(red)
        for i in range(4):
            self.field.append(yellow)
        for i in range(4):
            self.field.append(green)
        for i in range(4):
            self.field.append(blue)
    def display(self):
        for i in range(40):
            pygame.draw.circle(screen,self.field[i],get_gos(i),25,4)
        for i in range(40,56):
            pygame.draw.circle(screen,self.field[i],get_pos(i),15,2)
        for i in range(56,72):
            pygame.draw.circle(screen,self.field[i],get_pos(i),25,4)
#//////////////////////////////////////
size = width, height = 1000, 570
screen = pygame.display.set_mode(size)
loop = True
font = pygame.font.Font("calibri.ttf",60)
num_of_players = 0
dice = 0
pieces = []
while loop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False
            pygame.quit()
    screen.fill([255,0,255])
    font = pygame.font.Font("calibri.ttf",60)
    txt1 = font.render("Number of players:",True,[0,0,0])
    txt2 = font.render("2",True,[0,0,0])
    txt3 = font.render("3",True,[0,0,0])
    txt4 = font.render("4",True,[0,0,0])
    screen.blit(txt1,[300,150])
    screen.blit(txt2,[300,250])
    screen.blit(txt3,[500,250])
    screen.blit(txt4,[700,250])
    if pygame.mouse.get_pressed() == (1,0,0):
        x,y = pygame.mouse.get_pos()
        if (y < 270 and y > 230 and x > 260 and x < 340):
            num_of_players = 2
            loop = False
        if (y < 270 and y > 230 and x > 460 and x < 540):
            num_of_players = 3
            loop = False
        if (y < 290 and y > 210 and x > 660 and x < 740):
            num_of_players = 4
            loop = False
    pygame.display.flip()
#//////////////////////////////////////
for i in range(4):
    img = pygame.image.load("red.png")
    img = pygame.transform.scale(img,(25,25))
    pieces.append(Piece(red,56+i,img))
for i in range(4):
    img = pygame.image.load("green.png")
    img = pygame.transform.scale(img,(25,25))
    pieces.append(Piece(green,64+i,img))
if num_of_players > 2:
    for i in range(4):
        img = pygame.image.load("blue.png")
        img = pygame.transform.scale(img,(25,25))
        pieces.append(Piece(green,68+i,img))
if num_of_players > 3:
    for i in range(4):
        img = pygame.image.load("yellow.png")
        img = pygame.transform.scale(img,(25,25))
        pieces.append(Piece(green,60+i,img))
myfield = Field()
#//////////////////////////////////////
def gameover():
    if myfield.field[40] == red and myfield.field[41] == red and myfield.field[42] == red and myfield.field[43] == red:
        screen.fill(white)
        wfont = pygame.font.Font("calibri.ttf",70)
        wtxt = wfont.render("Red wins!!",True,red)
        screen.blit(wtxt,[400,250])
        pygame.display.flip()
        pygame.time.delay(6000)
        return True
    if myfield.field[44] == yellow and myfield.field[45] == yellow and myfield.field[46] == yellow and myfield.field[47] == yellow:
        screen.fill(white)
        wfont = pygame.font.Font("calibri.ttf",70)
        wtxt = wfont.render("Yellow wins!!",True,yellow)
        screen.blit(wtxt,[400,250])
        pygame.display.flip()
        pygame.time.delay(6000)
        return True
    if myfield.field[48] == green and myfield.field[49] == green and myfield.field[50] == green and myfield.field[51] == green:
        screen.fill(white)
        wfont = pygame.font.Font("calibri.ttf",70)
        wtxt = wfont.render("Green wins!!",True,green)
        screen.blit(wtxt,[400,250])
        pygame.display.flip()
        pygame.time.delay(6000)
        return True
    if myfield.field[52] == blue and myfield.field[53] == blue and myfield.field[54] == blue and myfield.field[55] == blue:
        screen.fill(white)
        wfont = pygame.font.Font("calibri.ttf",70)
        wtxt = wfont.render("Blue wins!!",True,blue)
        screen.blit(wtxt,[400,250])
        pygame.display.flip()
        pygame.time.delay(6000)
        return True
    return False
#//////////////////////////////////////

#//////////////////////////////////////
pygame.quit()
