# wgranie pygame
import pygame
import random
import math

# initialize pygame
pygame.init()

# dodanie ekranu/wyswietlacza
screen = pygame.display.set_mode((800, 600))  # szerokosc , wysokosc  - 0, 0 to byloby "nic" w lewym gornym rogu

# Tło
background = pygame.image.load("kosmos.png")

# Tytul i Icona okna ekranu
pygame.display.set_caption("Space Invaders")  # nazwa okna ekranu
icon = pygame.image.load("space-invaders.png")
pygame.display.set_icon(icon)  # ikona okna ekranu

# player icon
playerImg = pygame.image.load('arcade-game.png')
playerX = 368  # to jest pozycja startowa  srodek to polowa z 800. rozmiar ikony to 64 (32 od polowy stad 368)
playerY = 480  # to tez
playerX_change = 0
playerY_change = 0

# ufo-
enemyImg = []                  # <-- to jest lista panie kolego
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
number_of_enemies = 6

for i in range(number_of_enemies):
    enemyImg.append(pygame.image.load('enemy.png'))
    enemyX.append(random.randint(0, 736))  # to jest pozycja startowa ufoludkow
    enemyY.append(random.randint(50, 100))  # to tez
    enemyX_change.append(0.3)
    enemyY_change.append(0.01)

# pew pew!
bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 0  # JAK TO ZROBIC zeby startowal z aktualnej pozycji statku? bo moj moze ruszac sie tez gora/dol
# bulletY tu bylo 480
bulletX_change = 0
bulletY_change = 4
bullet_state = "ready"  # w ready pocisk jest schowany pod statkiem

score=0

def player(x, y):
    screen.blit(playerImg, (x, y))  # blit draw-uje na ekranie (ikona, (osX, osY)


def enemy(x, y, i):
    screen.blit(enemyImg, (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))  # +16 i +10 zeby wylatywal ze srodka statku


def hits(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX - bulletX, 2)) + (math.pow(enemyY - bulletY, 2)))
    if distance < 27:        #27 to nazwijmy minimalna odleglosc od hitboxa
        return True
    else:
        return False


# loop gry (primo zeby sie nie zawieszalo, duo by okno sie nie zamykalo chyba ze po quitcie
running = True
while running:

    screen.fill((0, 0, 0))  # kolor wypelnienia ekranu w RGB
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # if keystroke is pressed check wheter its right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.3
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.3
            if event.key == pygame.K_UP:
                playerY_change = -0.3
            if event.key == pygame.K_DOWN:
                playerY_change = 0.3
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":  # "pobiera" aktualne kordynaty statku
                    bulletX = playerX
                    bulletY = playerY
                    fire_bullet(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                playerY_change = 0

    # boundaries statku gracza

    playerX += playerX_change
    playerY += playerY_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    if playerY <= 0:
        playerY = 0
    if playerY >= 536:
        playerY = 536

    # bullet movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"
    if bullet_state is "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change




    # boundaries ufojutkow

    enemyX += enemyX_change
    enemyY += enemyY_change


   #ruch ufojutkow

   # if enemyX <= 0:                dla jednego przeciwnika STARE
    #     enemyX_change = 0.3
    #     enemyY += enemyY_change
   # elif enemyX >= 736:
   #      enemyX_change = -0.3
    #     enemyY += enemyY_change
    for i in range(number_of_enemies):     #nie rozumiem tego [i] ale pewnie dlatego ze nie zrobilem list jeszcze
        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 0.3
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -0.3
            enemyY[i] += enemyY_change[i]

            #teraz trafienie musi byc wewnatrz tego loopa (wczensiej bylo oddzielnie)

        # trafienie
        hit = hits(enemyX[i], enemyY[i], bulletX, bulletY)
        if hit:
            bulletY = 480
            bullet_state = "ready"
            score += 1
            print(score)
            enemyX[i] = random.randint(0, 736)
            enemyY[i] = random.randint(50, 100)

        enemy(enemyX[i], enemyY[i], i)

    if enemyY <= 0:
        enemyY = 0
    if enemyY >= 536:
        enemyY = 536

    player(playerX,
           playerY)  # po screenfill bo najpierw musi byc narysowany ekran i jego wypelnieni i dopiero na nim player

    pygame.display.update()  # to pilnuje zeby updateowal to co dorzucimy do wyswietlania
