#############################################
#                                           #
#                    Mench                  #
#          created by Masoud Barati         #
#############################################
import pygame
import random
import math

pygame.init()                #importing imortant madules

class Piece:                         #pieces class
    def __init__(self,color1,pos1,pic1):
        self.color = color1
        self.pos = pos1
        self.pic = pic1
    def moving(self,n):                           #the most confusing function in this game!
        global dice                               #it get the dice number and make selected pieces to move
        former_pos = self.pos                     #pieces are separating by their color
        if self.color == red:                   #red color move
            if self.pos > 55 and self.pos < 60 and dice == 6:
                if myfield.field[0] != red:
                    self.pos = 0
                    dice = 0
                    myfield.field[0] = red
            elif self.pos + n < 44 and myfield.field[self.pos + n] != red:
                self.pos += n
                dice = 0
                myfield.field[self.pos] = red
        if self.color == yellow:                 #yellow color move
            if self.pos > 59 and self.pos < 64:
                if dice == 6 and myfield.field[10] != yellow:
                    self.pos = 10
                    dice = 0
                    myfield.field[10] = yellow              #these are algorithms for moving from end of field list to start point of it
            elif self.pos + n > 39:
                testdice = (dice - (39-self.pos)) - 1
                if myfield.field[testdice] != yellow:
                    self.pos = testdice
                    dice = 0
                    myfield.field[testdice] = yellow
            elif self.pos < 10 and self.pos + n > 9:
                testdice = (dice - (9-self.pos))
                if myfield.field[testdice + 43] != yellow and (testdice + 43) < 48:
                    self.pos = testdice + 43
                    dice = 0
                    myfield.field[testdice + 43] = yellow
            else:
                if myfield.field[self.pos + n] != yellow:
                    self.pos += n
                    dice = 0
                    myfield.field[self.pos] = yellow
        if self.color == green:                #green pieces move
            if self.pos > 63 and self.pos < 68:
                if dice == 6 and myfield.field[20] != green:
                    self.pos = 20
                    dice = 0
                    myfield.field[20] = green
            elif self.pos + n > 39:                     #these are algorithms for moving from end of field list to start point of it
                testdice = (dice - (39-self.pos)) - 1
                if myfield.field[testdice] != green:
                    self.pos = testdice
                    dice = 0
                    myfield.field[testdice] = green
            elif self.pos < 20 and self.pos + n > 19:
                testdice = (dice - (19-self.pos))
                if myfield.field[testdice + 47] != green and (testdice + 47) < 52:
                    self.pos = testdice + 47
                    dice = 0
                    myfield.field[testdice + 47] = green
            else:
                if myfield.field[self.pos + n] != green:
                    self.pos += n
                    dice = 0
                    myfield.field[self.pos] = green
        if self.color == blue:        #blue pieces move
            if self.pos > 67:
                if dice == 6 and myfield.field[30] != blue:
                    self.pos = 30
                    dice = 0
                    myfield.field[30] = blue
            elif self.pos + n > 39:                  #these are algorithms for moving from end of field list to start point of it
                testdice = (dice - (39-self.pos)) - 1
                if myfield.field[testdice] != blue:
                    self.pos = testdice
                    dice = 0
                    myfield.field[testdice] = blue
            elif self.pos < 30 and self.pos + n > 29:
                testdice = (dice - (29-self.pos))
                if myfield.field[testdice + 51] != blue and (testdice + 51) < 56:
                    self.pos = testdice + 51
                    dice = 0
                    myfield.field[testdice + 51] = blue
            else:
                if myfield.field[self.pos + n] != blue:
                    self.pos += n
                    dice = 0
                    myfield.field[self.pos] = blue
        if former_pos != self.pos:
            myfield.field[former_pos] = black                          
        for i in range(len(pieces)):                      #hitting other pieces are checking in this loop
            if self.pos == pieces[i].pos and self.color != pieces[i].color:
                hit(i)
#//////////////////////////////////////
def hit(hitted_num):                        #this function will hit a piece         
    if pieces[hitted_num].color == red:     #it means that the mentioned piece will sent to the its color repository
        for i in range(56,60):
            if myfield.field[i] == black:
                pieces[hitted_num].pos = i
                myfield.field[i] = red
                break
    if pieces[hitted_num].color == yellow:
        for i in range(60,64):
            if myfield.field[i] == black:
                pieces[hitted_num].pos = i
                myfield.field[i] = yellow
                break
    if pieces[hitted_num].color == green:
        for i in range(64,68):
            if myfield.field[i] == black:
                pieces[hitted_num].pos = i
                myfield.field[i] = green
                break
    if pieces[hitted_num].color == blue:
        for i in range(68,72):
            if myfield.field[i] == black:
                pieces[hitted_num].pos = i
                myfield.field[i] = blue
                break
#//////////////////////////////////////
white = [255,255,255]
black = [0,0,0]
red = [225,0,0]
green = [0,147,0]                  #defining colors !!
yellow = [255,255,0]
blue = [0,0,255]
#//////////////////////////////////////
def get_pos(num):                 #this function locate the pieces and field steps
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
class Field:                                #field class
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
            pygame.draw.circle(screen,self.field[i],get_pos(i),25,4)
        for i in range(40,56):
            pygame.draw.circle(screen,self.field[i],get_pos(i),15,2)
        for i in range(56,72):
            pygame.draw.circle(screen,self.field[i],get_pos(i),25,4)
    def cleaner(self):          #it will clean the empty steps of the field
        for i in range(len(self.field)):
            if self.field[i] != black:
                m = 0
                for j in pieces:
                    if j.pos == i:
                        m = 1
                        break
                if m == 0:
                    self.field[i] = black
#//////////////////////////////////////
size = width, height = 1000, 570                 #defining base variables
screen = pygame.display.set_mode(size)
loop = True
font = pygame.font.Font("calibri.ttf",60)
num_of_players = 0
dice = 0
is_six = False
pieces = []
while loop:                                    #a loop for Understanding the number of players!
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False
            pygame.quit()
    screen.fill([255,0,255])
    txt1 = font.render("Number of players:",True,[0,0,0])
    txt2 = font.render("2",True,[0,0,0])
    txt3 = font.render("3",True,[0,0,0])
    txt4 = font.render("4",True,[0,0,0])
    screen.blit(txt1,[280,150])
    screen.blit(txt2,[300,250])
    screen.blit(txt3,[500,250])
    screen.blit(txt4,[700,250])
    if pygame.mouse.get_pressed() == (1,0,0):
        x,y = pygame.mouse.get_pos()
        if (y < 300 and y > 230 and x > 260 and x < 340):
            num_of_players = 2
            loop = False
        if (y < 300 and y > 230 and x > 460 and x < 540):
            num_of_players = 3
            loop = False
        if (y < 300 and y > 230 and x > 660 and x < 740):
            num_of_players = 4
            loop = False
    pygame.display.flip()
#//////////////////////////////////////
for i in range(4):                        #declaring pieces
    img = pygame.image.load("red.png")
    img = pygame.transform.scale(img,(50,50))
    pieces.append(Piece(red,56+i,img))
for i in range(4):
    img = pygame.image.load("green.png")
    img = pygame.transform.scale(img,(50,50))
    pieces.append(Piece(green,64+i,img))
tern = [red,green]
if num_of_players > 2:
    for i in range(4):
        img = pygame.image.load("blue.png")
        img = pygame.transform.scale(img,(50,50))
        pieces.append(Piece(blue,68+i,img))
    tern.append(blue)
if num_of_players > 3:
    for i in range(4):
        img = pygame.image.load("yellow.png")
        img = pygame.transform.scale(img,(50,50))
        pieces.append(Piece(yellow,60+i,img))
    tern.append(yellow)
myfield = Field()
dice_button = pygame.image.load("diceButton.png")
dice_button = pygame.transform.scale(dice_button,(200,(200/6)))
no_move = pygame.image.load("nomove.png")
no_move = pygame.transform.scale(no_move,(100,130))
#bgnumber = random.randint(1,3);                           # set back ground image
bgimage = pygame.image.load("bg2.jpg")
bgimage = pygame.transform.scale(bgimage,(1000,570))
#//////////////////////////////////////
def gameover():                       #determine the game is over or no
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
def screen_display():
    screen.fill(white)                                          # khoshgel kari ha !
    screen.blit(bgimage,[0,0])
    pygame.draw.circle(screen,[215,0,0],get_pos(0),25,25)
    pygame.draw.circle(screen,[255,192,0],get_pos(10),25,25)
    pygame.draw.circle(screen,green,get_pos(20),25,25)
    pygame.draw.circle(screen,blue,get_pos(30),25,25)
    pygame.draw.circle(screen,[255,20,20],get_pos(39),25,25)
    pygame.draw.circle(screen,yellow,get_pos(9),25,25)
    pygame.draw.circle(screen,[0,255,0],get_pos(19),25,25)
    pygame.draw.circle(screen,[0,102,255],get_pos(29),25,25)
    red_arrow = pygame.image.load("redarrow.png")
    red_arrow = pygame.transform.scale(red_arrow,(50,70))
    green_arrow = pygame.image.load("greenarrow.png")
    green_arrow = pygame.transform.scale(green_arrow,(70,75))
    blue_arrow = pygame.image.load("bluearrow.png")
    blue_arrow = pygame.transform.scale(blue_arrow,(70,40))
    yellow_arrow = pygame.image.load("yellowarrow.png")
    yellow_arrow = pygame.transform.scale(yellow_arrow,(70,40))
    screen.blit(red_arrow,[150,500])
    screen.blit(green_arrow,[350,20])
    screen.blit(blue_arrow,[490,370])
    screen.blit(yellow_arrow,[10,170])
    #
    myfield.display()                            # field and pieces displaying
    for i in pieces:
        pos = get_pos(i.pos)
        pos[0] -= 25
        pos[1] -= 25
        screen.blit(i.pic,pos)
    txt = pygame.font.Font("calibri.ttf",35)
    turntxt = txt.render("Turn:",True,black)     
    screen.blit(turntxt,[700,50])
    pygame.draw.rect(screen,tern[0],[800,50,70,40])
    screen.blit(dice_button,[700,150])
    screen.blit(no_move,[750,450])
    if dice != 0:
        name = str(dice) + ".png"              #It's the best way ! :D
        dice_pic = pygame.image.load(name)
        dice_pic = pygame.transform.scale(dice_pic,(70,70))
        screen.blit(dice_pic,[765,350])
    pygame.display.flip()
#//////////////////////////////////////
game_quit = False                   
while (not gameover()) and (not game_quit):                 # main loop
    screen_display()                                        # it check the position of the mouse and deciding which work should do
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_quit = True
    if pygame.mouse.get_pressed() == (1,0,0):
        x,y = pygame.mouse.get_pos()
        if x > 700 and x < 900 and y > 150 and y < 235 and dice == 0:
            dice = random.randint(1,6)
            if dice == 6:
                is_six = True
            else:
                is_six = False
        for i in pieces:
            piece_pos = get_pos(i.pos)
            if x > (piece_pos[0] - 25) and x < (piece_pos[0] + 25) and y > (piece_pos[1] - 25) and y < (piece_pos[1] + 25) and tern[0] == i.color and dice != 0:
                i.moving(dice)
                if is_six == False and dice == 0:
                    temp = tern[0]
                    tern.pop(0)
                    tern.append(temp)
        if x > 750 and x < 850 and y > 450 and y < 580 and dice != 0:
            dice = 0
            temp = tern[0]
            tern.pop(0)
            tern.append(temp)
#//////////////////////////////////////
pygame.quit()   # quit the game
                                                   #created by Masoud Barati
                                                            #the END
