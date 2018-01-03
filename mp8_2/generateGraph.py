import pygame
from pygame.locals import *
import mp8_2

yMax = 25
xMax = 25

liste = mp8_2.generate_labyrinthe(xMax,yMax)
mazebase = liste

pygame.init()
clock = pygame.time.Clock()
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 30)

# window est du type Surface(), on peut donc utiliser blit(), fill() sur window
# et donc "dessiner sur l'écran" (attention cela se fait en réalité en mémoire, il
# faut appeler flip() pour que cela devienne visible)
window = pygame.display.set_mode( (xMax*20 + 10, yMax*20 + 10) )

# vous pouvez chargez n'importe quel fichier image, les png sont recommandés comme
# format (car ils gèrent bien la transparence)
# on import les images des différents mur

wall = pygame.image.load("mur.png")
empty = pygame.image.load("empty.png")
player = pygame.image.load("start.png")
end = pygame.image.load("end.png")

playerloc = None
mouvement = 0
finish = False
play = False

running = True


def draw_csv():
    fe


buttonPlay = pygame.Rect(100, 100, 250, 50)
buttonReplay = pygame.Rect(100, 200, 250, 50)

while running:
   clock.tick(60)
   window.fill( (255,255,255) )

   if finish == True:
    window.fill(0)

   if finish != True and play == True:
       for y in range(len(liste)):
        for x in range(len(liste[y])):
            if liste[y][x] == 2:
                playerloc = (x, y)
                e = player
            elif liste[y][x] == 3:
                e = end
            elif liste[y][x] == 0:
                e = wall
            elif liste[y][x] == 1:
                e = empty
            window.blit( e, (x*10,y*10) )

   if play != True:
        pygame.draw.rect(window, [255, 0, 0], buttonPlay)
        pygame.draw.rect(window, [255, 0, 0], buttonReplay)

   pygame.display.flip()

   for event in pygame.event.get():
        if playerloc is not None:
            (x, y) = playerloc

        if event.type == QUIT or(event.type == KEYUP and event.key == K_ESCAPE):
           running = False
        if event.type == KEYDOWN and playerloc is not None:
            if event.key == K_UP:
                if y-1 >= 0:
                    if liste[y-1][x] == 1:
                        liste[y][x] = 1
                        liste[y-1][x] = 2
                        mouvement += 1
                    elif liste[y-1][x] == 3:
                        finish = True

            if event.key == K_DOWN:
                if y+1 < (2*yMax+1):
                    if liste[y+1][x] == 1:
                        liste[y][x] = 1
                        liste[y+1][x] = 2
                        mouvement += 1
                    elif liste[y+1][x] == 3:
                        finish = True

            if event.key == K_RIGHT:
                if x+1 < (2*xMax+1):
                    if liste[y][x+1] == 1:
                        liste[y][x] = 1
                        liste[y][x+1] = 2
                        mouvement += 1
                    elif liste[y][x+1] == 3:
                        finish = True

            if event.key == K_LEFT:
                if x-1 >= 0:
                    if liste[y][x-1] == 1:
                        liste[y][x] = 1
                        liste[y][x-1] = 2
                        mouvement += 1
                    elif liste[y][x-1] == 3:
                        finish = True

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if buttonPlay.collidepoint(mouse_pos):
                print('play')
                play = True
            if buttonReplay.collidepoint(mouse_pos):
                print('replay')


pygame.quit()