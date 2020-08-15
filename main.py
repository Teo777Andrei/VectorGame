import random
import time

import pygame as game

#pygame module initialisation
game.init()

#start time --starts when game is initialised
t1=time.time()

#map width and length (pixels)
WIDTH = 800
HEIGHT = 500

#display initialisation
DISPLAY=game.display.set_mode(size=(WIDTH,HEIGHT))

#fill map with backround colour (white)
DISPLAY.fill((255,255,255))
game.display.update()

#title and display icon
game.display.set_caption('Vector')
game.display.set_icon(game.image.load('vector.png'))

#horizontal and vertical limits of playable map
MAX_LIMIT_HEIGHT = 460
Max_LIMIT_WIDTH = 760


#gameplay icons -- arrows and square
down_arrow = game.image.load('down_arrow.png')
left_arrow = game.image.load('left_arrow.png')
right_arrow = game.image.load('right_arrow.png')
up_arrow = game.image.load('up_arrow.png')
square = game.image.load('game_square.png')



#time - limit
limit = 100

# initialise  variables for tracking position (width-pixel and height-pixel) of arrows
width = 400
height = 0

#condition statement-- this statement  determines whether the gui closes or the game continues
k = 0


#the game starts with down_arrow at position : (width, height)
DISPLAY.blit(down_arrow,(width,height))
#after each modification to the map, the display must be refreshed to see progress
game.display.update()

# X and Y are coordinates of the first square spawned randomly on map
X = random.randint(10, WIDTH-50)
Y = random.randint(10, HEIGHT-50)

#initialising the game loop
while game.display.get_active():
    #spawn square
    DISPLAY.blit(square, (X, Y))
    game.display.update()

    for i in game.event.get():
        #if quit button is pressed condition value  becomes 2
        if i.type == game.QUIT:
            k = 2
        if i.type == game.KEYDOWN:
            #if escape button is pressed , condition value becomes 1
            if i.key == game.K_ESCAPE :
                k = 1


            else:
                limit += 5
                #if down key is pressed then down_arrow.png is shown on the screen
                if i.key == game.K_DOWN:
                    #firstly the map backround is filled with white
                    DISPLAY.fill((255,255,255))
                    #therefore down_arrow.png is display at (width, height) position
                    DISPLAY.blit(down_arrow,(width,height))
                    #after each modification on gui the map refreshes through .display() method
                    game.display.update()
                    height += 40


                #same process as above goes for up, left and right keys
                #right_key
                if i.key == game.K_RIGHT:
                    DISPLAY.fill((255, 255, 255))
                    DISPLAY.blit(right_arrow, (width, height))
                    game.display.update()
                    width += 40

                #left_key
                if i.key == game.K_LEFT:
                    DISPLAY.fill((255, 255, 255))
                    DISPLAY.blit(left_arrow, (width, height))
                    game.display.update()
                    width -= 40

                #up_key
                if i.key == game.K_UP:
                    DISPLAY.fill((255, 255, 255))
                    DISPLAY.blit(up_arrow, (width, height))
                    game.display.update()
                    height -= 40

    #if arrow position is within the following range it means:
    #-arrow has "touched" the square
    #-new X,Y coordinates for square are generated , randomly
    if width > X-25 and width < X+25 and height < Y+25 and height > Y-25:
        X=random.randint(10, Max_LIMIT_WIDTH)
        Y=random.randint(10, MAX_LIMIT_HEIGHT)

    #updates time
    t2 = time.time()

    #if innactive more than limit (seconds) , gui ends
    if t2-t1 > limit:
        break
    #if condition value is 1 or arrow position values exceeds the playable map limits , gui ends
    elif k == 1  or height > MAX_LIMIT_HEIGHT or width > Max_LIMIT_WIDTH or width < 0 or height < 0:
        break
    #if condition value is 2, then the game  ends
    elif k == 2:
        break




