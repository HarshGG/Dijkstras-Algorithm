import pygame
pygame.init()

display = pygame.display.set_mode((1000,600))
pygame.display.set_caption("DIJKSTRA'S ALGORITHM")

run = True

while run:
    #handle events
    pygame.time.delay(10)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run = False

    #clear display
    display.fill(0)

     # draw scene
    pygame.draw.rect(display, ('#306678'), pygame.Rect(0,0,1000,600))
    pygame.draw.circle(display, ('#fcb614'), (50, 50), 20) #(r, g, b) is color, (x, y) is center, R is radius and w is the thickness of the circle border.

    # update display
    pygame.display.flip()


