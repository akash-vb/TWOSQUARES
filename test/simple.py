import pygame
import time
import random

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
green = (177, 204, 120)

display_width = 400
display_height = 400

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('TWOSQUARES')
clock = pygame.time.Clock()


def snake(snakex, snakey, snakew, snakeh, colour):
    pygame.draw.rect(gameDisplay, colour, (snakex, snakey, snakew, snakeh))

def food(randomx, randomy, foodwidth, foodheight, colour):
    pygame.draw.rect(gameDisplay, colour, (randomx, randomy, foodwidth, foodheight))

def crash_message(text):
    font1 = pygame.font.Font('freesansbold.ttf', 25)
    gameDisplay.blit(font1.render(text, True, (177, 204, 120)), (display_width/3, display_height/2))
    pygame.display.update()
    time.sleep(1)

    gameloop()

def score(text):
    font1 = pygame.font.Font('freesansbold.ttf', 16)
    gameDisplay.blit(font1.render('score ' + str(text), True, (177, 204, 120)), (10, 10))
    pygame.display.update()


def gameloop():
    x = display_width / 2
    y = display_height / 2
    w = 10
    h = 10
    foodwidth = 10
    foodheight = 10
    x_change = x
    y_change = y
    keyspeed = 5
    randomx = random.randrange(0, 380)
    randomy = random.randrange(0, 380)
    crashed = False
    count = 0

    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change += -keyspeed

            if event.key == pygame.K_RIGHT:
                x_change += keyspeed

            if event.key == pygame.K_UP:
                y_change += -keyspeed

            if event.key == pygame.K_DOWN:
                y_change += keyspeed


        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                x_change = x - 2

            if event.key == pygame.K_RIGHT:
                x_change = x + 2

            if event.key == pygame.K_UP:
                y_change = y - 2

            if event.key == pygame.K_DOWN:
                y_change = y + 2

        x = x_change
        y = y_change

        if x < 0:
            x = display_width
        elif x > display_width:
            x = 0

        if y < 0:
            y = display_height
        elif y > display_height:
            y = 0

        gameDisplay.fill(black)
        food(randomx, randomy, foodwidth, foodheight, white)
        snake(x, y, w, h, green)

        if (x >= randomx and x <= randomx + foodwidth) and (y >= randomy and y <= randomy + foodheight):
            randomx = random.randrange(0, display_width-10)
            randomy = random.randrange(0, display_height-10)
            count += 1


        elif (x + w >= randomx and x + w <= randomx + foodwidth) and (y >= randomy and y <= randomy + foodheight):
            randomx = random.randrange(0, display_width-10)
            randomy = random.randrange(0, display_height-10)
            count += 1

        elif (x + h + w >= randomx and x + h + w <= randomx + foodwidth) and (y >= randomy and y <= randomy + foodheight):
            randomx = random.randrange(0, display_width -10)
            randomy = random.randrange(0, display_height -10)
            count += 1

        elif (y + h + x >= randomy and y + h + x  <= randomy + foodheight) and (y + h + x >= randomx and y + h + x <= randomx + foodwidth):
            randomx = random.randrange(0, display_width -10)
            randomy = random.randrange(0, display_height - 10)
            count += 1

        elif (y + h >= randomy and y + h <= randomy + h) and (y + h >= randomx and y + h <= randomx + w ):
            randomx = random.randrange(0, display_width - 10)
            randomy = random.randrange(0, display_height - 10)
            count += 1

        score(count)
        if x + 10 >= display_width or y + 10 > display_height:
            crashed = True
            crash_message("You crashed!")


        pygame.display.update()
        clock.tick(60)

gameloop()
pygame.quit()
quit()
