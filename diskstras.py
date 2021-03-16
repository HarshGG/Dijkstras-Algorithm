import pygame
import sys
from pygame.locals import *
pygame.init()

display = pygame.display.set_mode((1000,600))
pygame.display.set_caption("DIJKSTRA'S ALGORITHM")

font = pygame.font.SysFont('Arial', 12)
fontLarge = pygame.font.SysFont('Arial', 18)

run = True
nodes = []
numNodes = 1

tempConn = [0,0]


connPressed = False
color =  ''

class Node:
    def __init__(self,nx,ny,num):
        self.x = nx
        self.y = ny
        self.num = num
        self.connections = []

def addConnection(node1, node2):
    node1conns = node1.connections
    node2conns = node2.connections
    if node2 not in node1conns:
        node1.connections.append(node2)
    else:
        pass
    if node1 not in node2conns:
        node2.connections.append(node1)
    print("for first node")
    for node in node1conns:
        print(str(node.num) + " ")
    print("for second node")
    for node in node2conns:
        print(str(node.num) + " ")

while run:
    #handle events
    pygame.time.delay(10)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run = False
        elif event.type==pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if(pos[0]>=850 and pos[0]<=950 and pos[1]>=30 and pos[1]<=80):
                connPressed = not connPressed
            elif(not connPressed):
                nodes.append(Node(pos[0],pos[1],numNodes))
                numNodes+=1 
            elif(connPressed):
                for node in nodes:
                    if(pos[0]>(node.x-20) and pos[0]<(node.x+20) and pos[1]>(node.y-20) and pos[1]<(node.y+20)):
                        if(tempConn[0]==0):
                            tempConn[0] = node.num
                        else:
                            tempConn[1] = node.num
                            addConnection(nodes[tempConn[0]-1],nodes[tempConn[1]-1])
                            tempConn = [0,0]
                            



    #clear display
    display.fill(0)

     # draw scene
    
    pygame.draw.rect(display, ('#306678'), pygame.Rect(0,0,1000,600))
    #nodes
    for node in nodes:
        pygame.draw.circle(display, ('#fcb614'), (node.x, node.y), 20) #(r, g, b) is color, (x, y) is center, R is radius and w is the thickness of the circle border.
        display.blit(font.render(str(node.num), True, (0,0,0)), (node.x-3, node.y-7))

    #connection button
    if(not connPressed):
        color = '#71e381'
    else:
        color = '#35ad2f'
    pygame.draw.rect(display, (color), pygame.Rect(850,30,100,50))
    display.blit(fontLarge.render('Connection', True, (0,0,0)), (865, 45))
    # update display
    pygame.display.flip()