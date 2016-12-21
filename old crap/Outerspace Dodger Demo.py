import pygame, time, random
global livesRemain   # to do, change black boxes to diff asteroid sprites, have like 5 diff sizes and just change their orientation randomly and speed. Make a changing background image not colours and also Highscore system
   #### make all the hitboxes of enemies half the size (removing top half)     
pygame.init()
display_width = 800
display_height = 600
gameDisplay = pygame.display.set_mode((display_width,display_height))#,pygame.FULLSCREEN)

black = (0,0,0)    # colours use RGB filing, i dont use any of these except random but i kept them in code for future use
white = (255,255,255)
green = (0,255,0)

def Explodeath():
    exd1()
    exd2()
    exd3()
    exd4()
    exd5()
    exd6()
    exd7()
    exd8()
    exd9()
    exd10()
def exd1():
    global x
    global y
    shipImg=pygame.image.load('data/Explosions/explo1.png')
    gameDisplay.blit(shipImg, ((x-32),(y-40)))
    time.sleep(0.1)
def exd2():
    global x
    global y
    shipImg=pygame.image.load('data/Explosions/explo2.png')
    gameDisplay.blit(shipImg, ((x-32),(y-40)))
    time.sleep(0.1)
def exd3():
    global x
    global y
    shipImg=pygame.image.load('data/Explosions/explo3.png')
    gameDisplay.blit(shipImg, ((x-32),(y-40)))
    time.sleep(0.1)
def exd4():
    global x
    global y
    shipImg=pygame.image.load('data/Explosions/explo4.png')
    gameDisplay.blit(shipImg, ((x-32),(y-40)))
    time.sleep(0.1)
def exd5():
    global x
    global y
    shipImg=pygame.image.load('data/Explosions/explo5.png')
    gameDisplay.blit(shipImg, ((x-32),(y-40)))
    time.sleep(0.1)
def exd6():
    global x
    global y
    shipImg=pygame.image.load('data/Explosions/explo6.png')
    gameDisplay.blit(shipImg, ((x-32),(y-40)))
    time.sleep(0.1)
def exd7():
    global x
    global y
    shipImg=pygame.image.load('data/Explosions/explo7.png')
    gameDisplay.blit(shipImg, ((x-32),(y-40)))
    time.sleep(0.1)
def exd8():
    global x
    global y
    shipImg=pygame.image.load('data/Explosions/explo8.png')
    gameDisplay.blit(shipImg, ((x-32),(y-40)))
    time.sleep(0.1)
def exd9():
    global x
    global y
    shipImg=pygame.image.load('data/Explosions/explo9.png')
    gameDisplay.blit(shipImg, ((x-32),(y-40)))
    time.sleep(0.1)
def exd10():
    global x
    global y
    shipImg=pygame.image.load('data/Explosions/explo10.png')
    gameDisplay.blit(shipImg, ((x-32),(y-40)))
    time.sleep(0.1)

    
clock = pygame.time.Clock()
ship_width=73
livesRemain=99999999999#5

crashexplosion=pygame.mixer.Sound('explosion1_0.wav')
def lives():
    global colourchange
    font = pygame.font.SysFont(None, 35)
    text = font.render("Lives: "+str(livesRemain), True, colourchange)
    gameDisplay.blit(text, (0,100))
def things_dodged(count):
    global colourchange
    font = pygame.font.SysFont(None, 35)
    text = font.render("Dodged: "+str(count), True, colourchange)
    gameDisplay.blit(text,(0,0))
def DemoMode():
    global colourchange
    font=pygame.font.SysFont(None,50)
    font2=pygame.font.SysFont(None,35)
    text= font.render("| DEMO MODE |",True, colourchange)
    gameDisplay.blit(text,(273,200))
    text2=font2.render("<- Left | Right -> | Shooting WIP", True, colourchange)
    gameDisplay.blit(text2, (200,50))

#ast1=pygame.image.load('data/asteroids and enemy ships/asteroid1.png')
ast2=pygame.image.load('data/asteroids and enemy ships/asteroid2.png')
ast3=pygame.image.load('data/asteroids and enemy ships/asteroid3.png')
ast4=pygame.image.load('data/asteroids and enemy ships/asteroid4.png')
en1=pygame.image.load('data/asteroids and enemy ships/enemyRed.png')
en2=pygame.image.load('data/asteroids and enemy ships/topdownfighter.png')

#def ast1thing(thingx,thingy,thingw,thingh):
    #gameDisplay.blit(ast1,[thingx,thingy,thingw,thingh])
def ast2thing(thingx2,thingy2,thingw2,thingh2):
    gameDisplay.blit(ast2,[thingx2,thingy2,thingw2,thingh2])
def ast3thing(thingx3,thingy3,thingw3,thingh3):
    gameDisplay.blit(ast3,[thingx3,thingy3,thingw3,thingh3])
def ast4thing(thingx4,thingy4,thingw4,thingh4):
    gameDisplay.blit(ast4,[thingx4,thingy4,thingw4,thingh4])
def en1thing(thingx5,thingy5,thingw5,thingh5):
    gameDisplay.blit(en1,[thingx5,thingy5,thingw5,thingh5])
def en2thing(thingx6,thingy6,thingw6,thingh6):
    gameDisplay.blit(en2,[thingx6,thingy6,thingw6,thingh6])
    
shipImg = pygame.image.load('Spaceship_tut3.png')
def ship(x,y):
    gameDisplay.blit(shipImg, ((x-35),(y-20)))
def text_objects(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()
def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',75)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)    
    pygame.display.update()
    time.sleep(2)
    game_loop()
def crash():
    Explodeath()
    #crashexplosion.play()
    #time.sleep(2.5)
    message_display("Bye-Bye!")

def background():
    bg1=pygame.image.load('data/weltraumrA.png')
    bgsized=pygame.transform.scale(bg1,(800,600),)
    gameDisplay.blit(bgsized,(0,0))


def game_loop():
    global x
    global y
    global colourchange
    backgtrue=1
    global livesRemain
    if livesRemain <= 0:
        pygame.quit()
        quit()
    pygame.mixer.music.load('Junkyard Tribe.mp3')   # It's inside game loop so it restarts when you 'crash'
    pygame.mixer.music.set_endevent(pygame.constants.USEREVENT)  # but these 3 lines
    pygame.mixer.music.play()                                   # load a specific sound file then play it. if you want to you can set a command so when this track ends it loads another one

    x =  (display_width * 0.45)
    y = (display_height * 0.8)
    x_change = 0

    #thing_startx = random.randrange(0,display_width)
    thing_startx2 = random.randrange(0,display_width)
    thing_startx3 = random.randrange(0,display_width)
    thing_startx4 = random.randrange(0,display_width)
    thing_startx5 = random.randrange(0,display_width)
    thing_startx6 = random.randrange(0,display_width)
    
    #thing_starty= random.randrange(-2800,-600,100)
    thing_starty2= random.randrange(-2600,-600,100)
    thing_starty3= random.randrange(-2200,-600,100)
    thing_starty4= random.randrange(-2800,-600,100)
    thing_starty5= random.randrange(-3400,-600,100)
    thing_starty6= random.randrange(-3400,-600,100)
    
    thing_speed = 5
    #thing_width = 100
    #thing_height = 100
    thingCount=1
    dodged=0

    
    #thingw=110
    #thingh=110
    thingw2=90
    thingh2=88
    thingw3=90
    thingh3=88
    thingw4=90
    thingh4=88
    thingw5=60
    thingh5=78
    thingw6=85
    thingh6=148
    
    s1=10
    s2=25
    s3=80
    changeS=1
    
    gameExit= False
    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True

            
            ############################
            if event.type == pygame.KEYDOWN:      # KEYUP/DOWN are key modes, down is pressed, up is not pressed
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
            ######################
        x += x_change
        ##

        colourchange=(s1,s2,s3)
          
        if changeS==1:
            if s1<=40:
                s1=s1+1
                s3=s3-1
            if s3<=50:
                changeS=2
        if changeS==2:
            if s3>=50:
                s1=s1-1
                s3=s3+1
            if s1<=10:
                changeS=1

        background()


        #######
       # spawnValue= random.randrange(1,6,1)
        #if spawnValue<=4:


        #ast1thing(thing_startx,thing_starty,thingw,thingh)

        ast2thing(thing_startx2,thing_starty2,thingw2,thingh2)

        ast3thing(thing_startx3,thing_starty3,thingw3,thingh3)

        ast4thing(thing_startx4,thing_starty4,thingw4,thingh4)

        en1thing(thing_startx5,thing_starty5,thingw5,thingh5)

        en2thing(thing_startx6,thing_starty6,thingw6,thingh6)
        #newthings(thing_startx,thing_starty,thingw,thingh)

        #thing_starty += thing_speed  ## keep
        thing_starty2 +=thing_speed
        thing_starty3 +=thing_speed
        thing_starty4 +=thing_speed
        thing_starty5 +=thing_speed
        thing_starty6 +=thing_speed

        ship(x,y)
        lives()
        things_dodged(dodged)

        DemoMode()

        
        if x+15 > display_width - ship_width or x+15 < 0:
            livesRemain= livesRemain-1
            crash()
        #if thing_starty > display_height:
         #   #thing_starty = 0 - thingh
          #  thing_startx = random.randrange(0,display_width)
           # thing_starty= random.randrange(-2800,-600,200)
            #dodged += 1

        if thing_starty2 > display_height:
            #thing_starty2 = 0 - thingh2
            thing_startx2 = random.randrange(0,display_width)
            thing_starty2= random.randrange(-2600,-600,200)
            dodged += 1

        if thing_starty3 > display_height:
            #thing_starty3 = 0 - thingh3
            thing_startx3 = random.randrange(0,display_width)
            thing_starty3= random.randrange(-2200,-600,200)
            dodged += 1

        if thing_starty4 > display_height:
            #thing_starty4 = 0 - thingh4
            thing_startx4 = random.randrange(0,display_width)
            thing_starty4= random.randrange(-2800,-600,200)
            dodged+=1
        if thing_starty5 > display_height:
            #thing_starty5 = 0 - thingh5
            thing_startx5 = random.randrange(0,display_width)
            thing_starty5= random.randrange(-3400,-600,200)
            dodged+=1
        if thing_starty6 > display_height:
            #thing_starty6 = 0 - thingh6
            thing_startx6 = random.randrange(0,display_width)
            thing_starty6= random.randrange(-3400,-600,200)
            dodged+=1

            

            thing_speed += 0.75
            #thing_width += (dodged * 1.2)

        ####
        #if y+20 < thing_starty+thingh:
         #   if x-10 > thing_startx and x-10 < thing_startx + thingw or x+ship_width > thing_startx and x + ship_width < thing_startx+thingw:
          #      livesRemain= livesRemain-1
           #     crash()
        if y-15 < thing_starty2+thingh2:
            if x-7 > thing_startx2 and x-6 < thing_startx2 + thingw2 or x+ship_width-10 > thing_startx2 and x + ship_width+7 < thing_startx2+thingw2:
                livesRemain= livesRemain-1
                crash()
        if y-15 < thing_starty3+thingh3:
            if x-7 > thing_startx3 and x-6 < thing_startx3 + thingw3 or x+ship_width-10 > thing_startx3 and x + ship_width+7 < thing_startx3+thingw3:
                livesRemain= livesRemain-1
                crash()
        if y-15 < thing_starty4+thingh4:
            if x-7 > thing_startx4 and x-6 < thing_startx4 + thingw4 or x+ship_width-10 > thing_startx4 and x + ship_width+7 < thing_startx4+thingw4:
                livesRemain= livesRemain-1
                crash()
        if y-15 < thing_starty5+thingh5:
            if x-7 > thing_startx5 and x-6 < thing_startx5 + thingw5 or x+ship_width-10 > thing_startx5 and x + ship_width+7 < thing_startx5+thingw5:
                livesRemain= livesRemain-1
                crash()
        if y-15 < thing_starty6+thingh6:
            if x-7 > thing_startx6 and x-6 < thing_startx6 + thingw6 or x+ship_width-10 > thing_startx6 and x + ship_width+7 < thing_startx6+thingw6:
                livesRemain= livesRemain-1
                crash()
        ####
            
        pygame.display.update()
        clock.tick(60)
    while gameExit== True:
        pygame.quit()
        quit()
pygame.mouse.set_visible(False)   # makes cursor invisible
game_loop()
pygame.quit()
quit()
