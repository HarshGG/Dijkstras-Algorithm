import pygame
import sys
from pygame.locals import *
import math
pygame.init()

display = pygame.display.set_mode((1000,600))
pygame.display.set_caption("DIJKSTRA'S ALGORITHM")

font = pygame.font.SysFont('Arial', 12)
fontMedium = pygame.font.SysFont('Arial', 17)
fontLarge = pygame.font.SysFont('Arial', 18)

run = True
nodes = []
numNodes = 1

tempConn = [0,0]
tempDij = [0,0]

connPressed = False
dijPressed = False
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
    else:
        pass
    distance = getDistance(node1, node2)
    for node in node1conns:
        pass
        #print(node.num)
        #print('The distance between node ' + str(node1.num) + ' and node ' + str(node2.num) + ' is ' + str(distance))
    

def getDistance(node1, node2):
    distance = math.sqrt(math.pow((node1.x-node2.x),2) + math.pow((node1.y-node2.y),2))
    return distance

def dijkstra(start, end):
    visited = []
    unvisited = []
    for i in range(len(nodes)):
        unvisited.append(i+1)
    table = {}
    inf = 99999999
    for i in range(len(nodes)):
        if not i+1==start.num:
            table[str(i+1)]=[inf,0] #i+1 is key, number of node. array's first element is distance from start, second is via which node
        else:
            table[str(i+1)]=[0,start.num] 
    print(table)
    curr = start
    while unvisited:
        currConns = curr.connections
        for node in currConns:
            if node.num in unvisited:
                nextCurr = node
                pass
        for node in currConns:
            if not node in visited:
                if not curr == start:
                    dist = table[str(curr.num)][0] + getDistance(curr, node)
                else:
                    dist = getDistance(curr, node)
                if(dist<table[str(node.num)][0]):
                    table[str(node.num)][0] = dist
                    table[str(node.num)][1] = curr.num
                if(dist < table[str(curr.num)][0] + getDistance(nextCurr,curr)):
                    nextCurr = node
        visited.append(curr)
        print('curr ' + str(curr.num))
        print(unvisited)
        print(table)
        print('')
        unvisited.remove(curr.num)
        curr = nextCurr

def dijkstraNew(start, end):
    unvisited = nodes
    table = {}
    inf = 99999999
    for i in range(len(nodes)):
        if not i+1==start.num:
            table[str(i+1)]=[inf,0] #i+1 is key, number of node. array's first element is distance from start, second is via which node
        else:
            table[str(i+1)]=[0,start.num] 
    print(table)
    while unvisited:
        curr = None
        for node in unvisited:
            if curr is None:
                curr = node
            elif table[str(node.num)][0] < table[str(curr.num)][0]:
                curr = node
        currConns = curr.connections

        for node in currConns:
            dist = getDistance(curr,node) + table[str(curr.num)][0]
            if dist<table[str(node.num)][0]:
                table[str(node.num)][0] = dist
                table[str(node.num)][1] = curr
        unvisited.remove(curr)

        trackNode = end
        path = []
        while trackNode!=start:
            if table[str(trackNode.num)][1]!=0:
                path.insert(0,trackNode)
                goalNode = table[str(goalNode.num)][1]
        
        path.insesrt(0,start)
        print(path)



while run:
    #handle events
    pygame.time.delay(10)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run = False
        elif event.type==pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if(pos[0]>=850 and pos[0]<=950 and pos[1]>=30 and pos[1]<=80):#connection button
                connPressed = not connPressed
            elif(pos[0]>=850 and pos[0]<=900 and pos[1]>=80 and pos[1]<=130):#shortest path button
                dijPressed = True
            elif(not connPressed and not dijPressed):
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
            if(dijPressed):
                connPressed = False
                for node in nodes:
                    if(pos[0]>(node.x-20) and pos[0]<(node.x+20) and pos[1]>(node.y-20) and pos[1]<(node.y+20)):
                        if(tempDij[0]==0):
                            tempDij[0] = node.num
                        else:
                            tempDij[1] = node.num
                            dijkstra(nodes[tempDij[0]-1],nodes[tempDij[1]-1])
                            dijPressed = False
                            tempDij = [0,0]
                            



    #clear display
    display.fill(0)

     # draw scene
    
    pygame.draw.rect(display, ('#306678'), pygame.Rect(0,0,1000,600))
    #nodes
    for node in nodes:
        pygame.draw.circle(display, ('#fcb614'), (node.x, node.y), 20) #(r, g, b) is color, (x, y) is center, R is radius and w is the thickness of the circle border.
        display.blit(fontLarge.render(str(node.num), True, (0,0,0)), (node.x-5, node.y-12))

    #connection button
    if(not connPressed):
        color = '#71e381'
    else:
        color = '#35ad2f'
    pygame.draw.rect(display, (color), pygame.Rect(850,30,100,50))
    display.blit(fontLarge.render('Connection', True, (0,0,0)), (865, 45))

    #test button
    pygame.draw.rect(display, ('#ff2659'), pygame.Rect(850,100,50,50))

    #connection lines
    for node in nodes:
        startX = node.x 
        startY = node.y 
        for conn in node.connections:
            endX = conn.x 
            endY = conn.y 
            pygame.draw.line(display, (0,0,0), (startX, startY), (endX, endY),3)
            display.blit(font.render(str(round(getDistance(node,conn),3)), True, (99, 0, 98)), ((startX+endX)/2, (startY+endY)/2))

    # update display
    pygame.display.flip()