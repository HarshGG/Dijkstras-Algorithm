import pygame
pygame.init()

display = pygame.display.set_mode((1000,600))
pygame.display.set_caption("DIJKSTRA'S ALGORITHM")

run = True
nodes = []

class Node:
    def __init__(self,nx,ny):
        self.x = nx
        self.y = ny

    pass

while run:
    #handle events
    pygame.time.delay(10)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run = False
        elif event.type==pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            nodes.append(Node(pos[0],pos[1])) 


    #clear display
    display.fill(0)

     # draw scene
    pygame.draw.rect(display, ('#306678'), pygame.Rect(0,0,1000,600))
    for node in nodes:
        pygame.draw.circle(display, ('#fcb614'), (node.x, node.y), 20) #(r, g, b) is color, (x, y) is center, R is radius and w is the thickness of the circle border.

    # update display
    pygame.display.flip()


