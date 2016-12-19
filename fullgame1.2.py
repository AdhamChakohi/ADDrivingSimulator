import pygame
import random
import time


## The car class. This is the generic car which will be most of what it spawns, and the other kinds of cars are child classes from this
class Car:
    def __init__(self, xCoord, yCoord):
        self.carWidth = 42
        self.carLength = 100
        self.xCoord = xCoord
        self.yCoord = yCoord
        self.rectangle = pygame.Rect(self.xCoord,self.yCoord,self.carWidth,self.carLength)
        self.vel = random.randint(5,9)
        self.color = (255,255,255)
        self.isSheikh = False
        self.isLocalMobile = False
        self.isBMW = False

        self.img = pygame.image.load("car_t.png").convert()


    def display(self,surface):
        #pygame.draw.rect(surface,self.color,self.rectangle)
        surface.blit(self.img, self.rectangle.topleft)


    def moveDown(self):
        self.rectangle.move_ip(0,self.vel)

class BMW(Car):
    def __init__(self, xCoord, yCoord):
        Car.__init__(self,xCoord,yCoord)
        self.vel = random.randint(13,17)
        self.color = (255,0,0)
        self.isSheikh = False
        self.isLocalMobile = False
        self.isBMW = True
        self.img = pygame.image.load("bmw_t.png").convert()

## Range Rover
class RR(Car):
    def __init__(self, xCoord, yCoord):
        Car.__init__(self,xCoord,yCoord)
        self.vel = random.randint(5,15)
        self.color = (0,255,0)
        self.isSheikh = False
        self.isLocalMobile = True
        self.isBMW = False
        self.img = pygame.image.load("rr_t.png").convert()

## Nissan Patrol
class NP(Car):
    def __init__(self, xCoord, yCoord):
        Car.__init__(self,xCoord,yCoord)
        self.vel = random.randint(5,15)
        self.color = (0,0,255)
        self.isSheikh = False
        self.isLocalMobile = True
        self.isBMW = False
        self.img = pygame.image.load("nissan_patrol_t.png").convert()

## Shiekh's car. Game ends if player hits this.
class Sheikh(Car):
    def __init__(self, xCoord, yCoord):
        Car.__init__(self,xCoord,yCoord)
        self.vel = random.randint(8,12)
        self.color = (0,51,102)
        self.isSheikh = True
        self.isLocalMobile = False
        self.isBMW = False
        self.img = pygame.image.load("sheikh_car_t.png").convert()

## the class of the player. the car stays at the bottom of the screen and goes left and right.
class Player:
    def __init__(self, xCoord, yCoord):
        self.xCoord = xCoord
        self.yCoord = yCoord
        self.carWidth = 41
        self.carLength = 100
        self.rectangle = pygame.Rect(self.xCoord,self.yCoord,self.carWidth,self.carLength)
        self.licensePoints = 0
        self.distance = 0
        self.img = pygame.image.load("player_car_t.png").convert()

    def display(self,surface):
        #pygame.draw.rect(surface,(255,255,255),self.rectangle)
        surface.blit(self.img, self.rectangle.topleft)
    def left(self):
        self.rectangle.move_ip(-7,0)
    def right(self):
        self.rectangle.move_ip(7,0)

pygame.init()
surface = pygame.display.set_mode((800, 720))

font1 = pygame.font.Font(None, 36)
font2 = pygame.font.Font(None, 25)

width = surface.get_width()

textlist = ['Welcome To', 'AD Traffic Sim', 'New Game', 'LeaderBoard', 'Quit', 'Press Space to Select']

xpos1 = (width/2 - 75)
ypos1 = 25

xpos2 = (width/2 - 90)
ypos2 = ypos1 + 45

xpos3 = (width/2 - 60)
ypos3 = ypos2 + 50

ypos4 = ypos3 + 50

ypos5 = ypos4 + 50

xposlist = [xpos1, xpos2, xpos3, xpos3, xpos3]
yposlist = [ypos1, ypos2, ypos3, ypos4, ypos5]

xcursorpos = xpos3 - 15
cursor = pygame.Rect(xcursorpos, 125, 10, 10)

play = True
while play:

    #ref: http://stackoverflow.com/questions/25494726/how-to-use-pygame-keydown
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
            break
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                if cursor.top == 125:
                    cursor = pygame.Rect(xcursorpos, 175, 10, 10)
                elif cursor.top == 175:
                    cursor = pygame.Rect(xcursorpos, 225, 10, 10)
                elif cursor.top == 225:
                    cursor = pygame.Rect(xcursorpos, 125, 10, 10)
            if event.key == pygame.K_UP:
                if cursor.top == 125:
                    cursor = pygame.Rect(xcursorpos, 225, 10, 10)
                elif cursor.top == 175:
                    cursor = pygame.Rect(xcursorpos, 125, 10, 10)
                elif cursor.top == 225:
                    cursor = pygame.Rect(xcursorpos, 175, 10, 10)
            if event.key == pygame.K_SPACE:
                if cursor.top == 125:


                    ## constants and initializations
                    #
                    # def laneSpawn(xCoord,container):
                    #     rectangle = pygame.Rect(xCoord,0,5,100)
                    #     container.append(rectangle)


                    laneSeperation = 55

                    listOfSpawnModifiers = []

                    speedConst = 25

                    carSep = 100

                    sheikhEnding = False

                    localMobileEnding = False

                    surface = pygame.display.set_mode((800,720))

                    completelyUselessCar = Car(0,0)

                    pygame.mixer.music.load("music.wav")

                    listOfCars = [[],[],[]]
                    listOfLaneLines = [[],[]]

                    player = Player(surface.get_width()//2,surface.get_height()-completelyUselessCar.carLength-10)

                    lanes = [surface.get_width()//2 - laneSeperation, surface.get_width()//2, surface.get_width()//2 + laneSeperation]

                    laneLines = [surface.get_width()//2 - completelyUselessCar.carWidth+20, surface.get_width()//2 + completelyUselessCar.carWidth-20]


                    clock = pygame.time.Clock()

                    font3 = pygame.font.Font(None, 30)

                    width = surface.get_width()
                    height = surface.get_height()

                    rect1 = pygame.Rect(0, 0, width/2 - 110, height)
                    rect2 = pygame.Rect(width/2 - 110, 0, 20, height)
                    rect3 = pygame.Rect(width/2 - 90, 0, 220, height)
                    rect4 = pygame.Rect(width/2 + 130, 0, 20, height)
                    rect5 = pygame.Rect(width/2 + 150, 0, width - (width/2 + 110), height)

                    font5 = pygame.font.Font(None, 35)

                    instructions = ["each accident adds points to your license", 'Nissan Patrols and Range rovers are VIPs, 2 points are added.', 'Rolls Royces contain Sheikhs. hitting them ends the game instantly.','5 points gets your license revoked.']
                    ylist = [surface.get_height()/2 - 100, surface.get_height()/2-50, surface.get_height()/2,surface.get_height()/2+50]

                    eg = True
                    while eg:
                        for i in pygame.event.get():
                            if i.type == pygame.KEYDOWN:
                                eg = False
                                break

                        surface.fill((0,0,0))

                        for i in range(len(instructions)):
                            disp = font5.render(instructions[i], True, (255,255,255))
                            surface.blit(disp, (surface.get_width()/2 - 400, ylist[i]))

                        disp = font2.render('Press any Key to go back', True, (255,255,255))
                        surface.blit(disp, (xpos1, surface.get_height() - 25))

                        pygame.display.update()

                    pygame.mixer.music.play()

                    ## each time a player makes a collision, points are added to his license. If the points exceed a certain number, the player's license gets revoked.
                    while player.licensePoints < 5:

                        collision = False

                        for i in pygame.event.get():
                            if i.type == pygame.QUIT:
                                player.licensePoints += 500
                                break

                        clock.tick(60)

                        keys = pygame.key.get_pressed()
                        if keys[pygame.K_LEFT]:
                            if player.rectangle.left - 1 > surface.get_width()//2-90:
                                player.left()
                        if keys[pygame.K_RIGHT]:
                            if player.rectangle.right + 1 < surface.get_width()//2+130:
                                player.right()

                        #surface.fill((0,0,0))

                        pygame.draw.rect(surface,(235,175,96),rect1)
                        pygame.draw.rect(surface,(255,255,0),rect2)
                        pygame.draw.rect(surface,(128,128,128),rect3)
                        pygame.draw.rect(surface,(255,255,0),rect4)
                        pygame.draw.rect(surface,(235,175,96),rect5)

                        player.display(surface)

                        for i in listOfCars:
                            ##Car spawning algorithm
                            for j in range(3):
                                if not len(listOfCars[j]) and not random.randrange(30):
                                    if not random.randrange(10):
                                        bm = BMW(lanes[j],0)
                                        modulus = (surface.get_height()-120)/(speedConst*bm.vel)
                                        counter = 0

                                        for k in listOfSpawnModifiers:
                                            if k[0] > modulus-carSep and k[0] < modulus + carSep:
                                                counter += 1

                                        if counter == 0:
                                            listOfSpawnModifiers.append([modulus,time.time()])
                                            listOfCars[j].append(bm)

                                        break
                                    elif not random.randrange(10):
                                        rr = RR(lanes[j],0)
                                        modulus = (surface.get_height()-120)/(speedConst*rr.vel)
                                        counter = 0

                                        for k in listOfSpawnModifiers:
                                            if k[0] > modulus-carSep and k[0] < modulus + carSep:
                                                counter += 1

                                        if counter == 0:
                                            listOfSpawnModifiers.append([modulus,time.time()])
                                            listOfCars[j].append(rr)

                                        break
                                    elif not random.randrange(10):
                                        np = NP(lanes[j],0)
                                        modulus = (surface.get_height()-120)/(speedConst*np.vel)
                                        counter = 0

                                        for k in listOfSpawnModifiers:
                                            if k[0] > modulus-carSep and k[0] < modulus + carSep:
                                                counter += 1

                                        if counter == 0:
                                            listOfSpawnModifiers.append([modulus,time.time()])
                                            listOfCars[j].append(np)

                                        break
                                    elif not random.randrange(30):
                                        sh = Sheikh(lanes[j],0)
                                        modulus = (surface.get_height()-120)/(speedConst*sh.vel)
                                        counter = 0

                                        for k in listOfSpawnModifiers:
                                            if k[0] > modulus-carSep and k[0] < modulus + carSep:
                                                counter += 1

                                        if counter == 0:
                                            listOfSpawnModifiers.append([modulus,time.time()])
                                            listOfCars[j].append(sh)

                                        break
                                    else:
                                        car = Car(lanes[j],0)
                                        modulus = (surface.get_height()-100)/(speedConst*car.vel)
                                        counter = 0

                                        for k in listOfSpawnModifiers:
                                            if k[0] > modulus-carSep and k[0] < modulus+carSep:
                                                counter += 1

                                        if counter == 0:
                                            listOfSpawnModifiers.append([modulus,time.time()])
                                            listOfCars[j].append(car)

                                        break

                            ## moving the cars and detecting for collisions.
                            for j in i:
                                j.moveDown()
                                j.display(surface)
                                if j.rectangle.top >= surface.get_height():
                                    i.remove(j)
                                if player.rectangle.colliderect(j.rectangle):

                                    i.remove(j)
                                    if j.isSheikh:
                                        sheikhEnding = True
                                        player.licensePoints += 500

                                    if j.isLocalMobile:
                                        player.licensePoints += 2

                                    collision = True
                        # for i in range(len(listOfLaneLines)):
                        #     if not listOfLaneLines[i]:
                        #         laneSpawn(laneLines[i],listOfLaneLines[i])
                        # for i in listOfLaneLines:
                        #     for j in i:
                        #         j.move_ip(0,3)
                        #         pygame.draw.rect(surface,((255,255,255)),j)
                        #         if j.top >= surface.get_height():
                        #             i.remove(j)




                        if collision:
                            player.licensePoints += 1

                        text1 = 'License Points: ' + str(player.licensePoints)
                        text2 = 'Distance: ' + str(player.distance/100)

                        disp = font3.render(text1,True,(0,0,0))
                        surface.blit(disp, (10, 40))

                        disp = font3.render(text2,True,(0,0,0))
                        surface.blit(disp, (surface.get_width() - 150, 40))

                        pygame.display.update()
                        player.distance += 1

                        for i in listOfSpawnModifiers:
                            end = time.time()
                            timePassed = end-i[1]
                            i[0]-=timePassed
                            if i[0]<0:
                                listOfSpawnModifiers.remove(i)

                    ## different endings
                    if sheikhEnding:
                        font4 = pygame.font.Font(None, 35)

                        messagelist = ["You hit the Sheikh's car", 'You have been deported', 'Score: ' + str(player.distance/100) + 'km']
                        ylist = [surface.get_height()/2 - 50, surface.get_height()/2, surface.get_height()/2 + 50]

                        eg = True
                        while eg:
                            for i in pygame.event.get():
                                if i.type == pygame.KEYDOWN:
                                    eg = False
                                    break

                            surface.fill((0,0,0))

                            for i in range(len(messagelist)):
                                disp = font4.render(messagelist[i], True, (255,255,255))
                                surface.blit(disp, (surface.get_width()/2 - 150, ylist[i]))

                            disp = font2.render('Press any Key to go back', True, (255,255,255))
                            surface.blit(disp, (xpos1, surface.get_height() - 25))

                            pygame.display.update()
                        pygame.display.quit()
                    else:
                        font5 = pygame.font.Font(None, 35)

                        messagelist = ["Too many License Points", 'Your license has been revoked', 'Score: ' + str(player.distance/100) + 'km']
                        ylist = [surface.get_height()/2 - 50, surface.get_height()/2, surface.get_height()/2 + 50]

                        eg = True
                        while eg:
                            for i in pygame.event.get():
                                if i.type == pygame.KEYDOWN:
                                    eg = False
                                    break

                            surface.fill((0,0,0))

                            for i in range(len(messagelist)):
                                disp = font5.render(messagelist[i], True, (255,255,255))
                                surface.blit(disp, (surface.get_width()/2 - 150, ylist[i]))

                            disp = font2.render('Press any Key to go back', True, (255,255,255))
                            surface.blit(disp, (xpos1, surface.get_height() - 25))

                            pygame.display.update()
                        pygame.display.quit()

                    font6 = pygame.font.Font(None, 30)
                    font7 = pygame.font.Font(None, 20)

                    inputprompt = 'Please enter your initials: '
                    namestring = ''
                    text = 'Press Space to Continue'
                    surface = pygame.display.set_mode((800, 720))
                    width = surface.get_width()

                    se = True
                    while se:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                se = False
                                break
                            if event.type == pygame.KEYDOWN:
                                if len(namestring) < 3:
                                    if event.key == pygame.K_a:
                                        namestring += 'A'
                                    elif event.key == pygame.K_b:
                                        namestring += 'B'
                                    elif event.key == pygame.K_c:
                                        namestring += 'C'
                                    elif event.key == pygame.K_d:
                                        namestring += 'D'
                                    elif event.key == pygame.K_e:
                                        namestring += 'E'
                                    elif event.key == pygame.K_f:
                                        namestring += 'F'
                                    elif event.key == pygame.K_g:
                                        namestring += 'G'
                                    elif event.key == pygame.K_h:
                                        namestring += 'H'
                                    elif event.key == pygame.K_i:
                                        namestring += 'I'
                                    elif event.key == pygame.K_j:
                                        namestring += 'J'
                                    elif event.key == pygame.K_k:
                                        namestring += 'K'
                                    elif event.key == pygame.K_l:
                                        namestring += 'L'
                                    elif event.key == pygame.K_m:
                                        namestring += 'M'
                                    elif event.key == pygame.K_n:
                                        namestring += 'N'
                                    elif event.key == pygame.K_o:
                                        namestring += 'O'
                                    elif event.key == pygame.K_p:
                                        namestring += 'P'
                                    elif event.key == pygame.K_q:
                                        namestring += 'Q'
                                    elif event.key == pygame.K_r:
                                        namestring += 'R'
                                    elif event.key == pygame.K_s:
                                        namestring += 'S'
                                    elif event.key == pygame.K_t:
                                        namestring += 'T'
                                    elif event.key == pygame.K_u:
                                        namestring += 'U'
                                    elif event.key == pygame.K_v:
                                        namestring += 'V'
                                    elif event.key == pygame.K_w:
                                        namestring += 'W'
                                    elif event.key == pygame.K_x:
                                        namestring += 'X'
                                    elif event.key == pygame.K_y:
                                        namestring += 'Y'
                                    elif event.key == pygame.K_z:
                                        namestring += 'Z'
                                if event.key == pygame.K_BACKSPACE:
                                    namestring = namestring[:-1]
                                if event.key == pygame.K_SPACE:
                                    se = False
                                    break

                        surface.fill((0,0,0,))

                        disp = font6.render(inputprompt, True, (255,255,255))
                        surface.blit(disp, (surface.get_width()/2 - 250, surface.get_height()/2 ))

                        disp = font6.render(namestring, True, (255,255,255))
                        surface.blit(disp, (surface.get_width()/2 + 30, surface.get_height()/2 ))

                        disp = font7.render(text, True, (255,255,255))
                        surface.blit(disp, (width/2 - 75, surface.get_height() - 25))

                        pygame.display.update()
                    pygame.display.quit()

                    with open("leaderboard.csv","a") as fp:
                        print(namestring + "," + str(player.distance/100),file=fp)


                if cursor.top == 175:

                    dictlist = []

                    with open('leaderboard.csv') as fp:
                        fp.readline()
                        for i in fp:
                            l = i.strip().split(',')
                            d = {'name':l[0], 'score':float(l[1])}
                            dictlist.append(d)


                    leader = sorted(dictlist, key=lambda k: k['score'], reverse = True)

                    font8 = pygame.font.Font(None, 30)
                    font9 = pygame.font.Font(None, 25)

                    width = surface.get_width()

                    headerlist = ['NAME','SCORE']
                    hdrx = width/2 - 100
                    hdrx2 = hdrx+150

                    yposlistlb = [125, 150, 175, 200, 225]


                    lboard = True
                    while lboard:
                        for event in pygame.event.get():
                            if event.type == pygame.KEYDOWN:
                                lboard = False
                                break

                        if not lboard:
                            break

                        surface.fill((0,0,0,))

                        disp = font8.render(headerlist[0], True, (255,255,255))
                        surface.blit(disp, (hdrx, 75 ))

                        disp = font8.render(headerlist[1], True, (255,255,255))
                        surface.blit(disp, (hdrx2, 75 ))

                        for i in range(5):
                            disp = font9.render(leader[i]['name'], True, (255,255,255))
                            surface.blit(disp, (hdrx, yposlistlb[i]))

                            disp = font9.render(str(leader[i]['score']), True, (255,255,255))
                            surface.blit(disp, (hdrx2, yposlistlb[i]))

                        disp = font8.render('Press any Key to go back', True, (255,255,255))
                        surface.blit(disp, (xpos1, surface.get_height() - 25))

                        pygame.display.update()

                if cursor.top == 225:
                    play = False
                    break

    surface = pygame.display.set_mode((800,720))

    surface.fill((0, 0, 0))

    pygame.draw.rect(surface, (255, 255, 255), cursor)

    for i in range(len(textlist[:-1])):
        disp = font1.render(str(textlist[i]), True, (255,255,255))
        surface.blit(disp, (xposlist[i], yposlist[i]))

    disp = font2.render(str(textlist[-1]), True, (255,255,255))
    surface.blit(disp, (xpos1, surface.get_height() - 25))

    pygame.display.update()
pygame.display.quit()
