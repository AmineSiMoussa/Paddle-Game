#----importing stuff------+
import pygame,sys,random
from pygame.locals import*
from pygame import mixer

#----basic screen stuff---------------------------------+

def main():
    pygame.init()

    (width, height) = (890, 590)
    pygame.display.set_caption("Paddle Game")
    DISPLAY = pygame.display.set_mode((width, height))

    BG = (50,50,50)
    orange = (242, 144, 24)
    white = (250, 250, 250)

#----paddle positions and height--+
    padypos = height - 100
    (padwidth,padheith) = (100,20)

#----ball information--------------+
    (ballwidth,ballheight) = 20,20
    ballx = width/2
    bally = 100
    velocityX = 0
    velocityY = 0
    accelaration = 0.002
    padland = False
    bounceDir = False
    bouncable = True

    rand = 7

    score_value = 0
    fontsize = 420
    font = pygame.font.Font('freesansbold.ttf',fontsize)
    textcolor = 60
    textoffset = 4



#----sound--------------------------+
    bounce_sound = mixer.Sound('paddle_game/sfx/bounce.wav')
    lose_sound = mixer.Sound('paddle_game/sfx/lose.wav')
    flip_sound = mixer.Sound('paddle_game/sfx/flip2.wav')

#----functions--------------+
    def show_score(x,y):
        score = font.render(str(score_value),True,(textcolor,textcolor,textcolor))
        DISPLAY.blit(score,(x,y))

#----game running----------------------------------------------------------------------------+
    while True:
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()

        textX = width/2 - fontsize/textoffset
        textY = height/2 - fontsize/2

        mx, my = pygame.mouse.get_pos()
        DISPLAY.fill(BG)

        show_score(textX,textY)

        pygame.draw.rect(DISPLAY,orange,(mx - 50,padypos - 20/2,padwidth,padheith))
        pygame.draw.rect(DISPLAY,white,(ballx - 10,bally - 10,ballwidth,ballheight))

        velocityY += accelaration
        bally += velocityY

        ballx += velocityX

        if ballx  >= (mx - 50) and ballx <= (mx + 50):
            padland = True
        else:
            padland = False

        if bally >= (padypos - padheith) and bally <= (padypos + padheith) and padland == True and bouncable == True:
            velocityY = -1
            bounce_sound.play()
            bounceDir = True
            bouncable = False

        if bounceDir == True:
            velocityX += (random.randrange(rand * -1, rand)*0.1)
            score_value += 1
            bounceDir = False

        if bally <= 400:
            bouncable = True

        if ballx >= (width - 10):
            velocityX *= -1
            flip_sound.play()
        if ballx <= 10:
            velocityX *= -1
            flip_sound.play()

        if score_value > 9:
            textoffset = 2
        if score_value > 99:
            textoffset = 1.21

        if bally >= height:
            lose_sound.play()
            return main()

        pygame.display.update()
main()