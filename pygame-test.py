import pygame
import sys
import numpy as np 

pygame.init()
screen = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()

#track points
TPS = [
    [2,8],
    [4,6],
    [2,4],
    [5,2],
    [6,4],
    [8,4],
    [9,7]

]
# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moving Circle with Path")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Circle properties
velocity = [2, 1.5]       # Movement speed
radius = 5


# Starting position
p = np.array(TPS[0])


#vector property
delta = 5
step_size = 2

# Path history
path_points = []


#scale for 500 x 500 stage 

TPS = [ [x*50 for x in sublist] for sublist in TPS ]
TPS = [np.array(point) for point in TPS]

x = 250
y = 250

#current_trac_point_id
ctpi = 0 

# ntpi = ctpi + 1


ctp = TPS[ctpi]
ntp = TPS[ctpi+1]
nntp = TPS[ctpi+2]

p = ctp 

def sdist (av,bv):
    distv = av-bv
    return np.inner(distv,distv)

def near (p1, p2, delta =2):

    if sdist(p1,p2) <= delta*delta :
        return True
    else: 
        return False 
    
# def near (p1, p2, delta =2):
#     dist = np.linalg.norm(p1 - p2)
#     if dist <= delta :
#         return True
#     else: 
#         return False 
def dist (ap, bp):
    dv = bp-ap
    return np.linalg.norm(dv)

def get_direction_uv(ap,bp):
    dv = bp-ap
    return dv / np.linalg.norm(dv)

def get_unit_vector(dv):
    return dv / np.linalg.norm(dv)

    
def update_direction(p,d_v,ctp, ntp, nntp):
    nd_uv = get_direction_uv(p,ntp)
    nnd_uv = get_direction_uv(p,nntp)
    nsdist = dist(ctp,ntp)
    rsdist = dist(p,ntp)
    r = rsdist/nsdist
    return get_unit_vector(  nd_uv*(1-r) + nnd_uv* (r) ) 

d_v = get_direction_uv(ctp,ntp)
def half_way(p,a,b):
    if dist(p,b) < dist(a,b)/2 :
        return True
    else: 
        return False
    
while True:

    #Computation area
    # sdist = 
    # if half_way(p,ctp,ntp) and ctpi +2 < len (TPS):

    if ctpi == len(TPS) - 1 :
        ctpi = 0
        p = TPS[ctpi]
        ctp = TPS[ctpi]
        ntp = TPS[ctpi+1]
        #nntp = TPS[ctpi+2]
    if near(p,ntp) and ctpi +1 < len (TPS):
        ctpi +=1
        ctp = TPS[ctpi]
        if ctpi != len(TPS) -1:
            ntp = TPS[ctpi+1]
        #nntp = TPS[ctpi+2]

        
    #unit vector of movement direction
    d_v = (ntp - ctp) /  np.linalg.norm(ntp - ctp)
    # d_v = update_direction(p,d_v,ctp, ntp, nntp)

    #scaled step vector 
    dp = d_v * step_size 

    #drawing below 
    screen.fill((255, 255, 255))
    for [xx,yy] in TPS:
        pygame.draw.circle(screen, (0, 255, 0), (xx, yy), 5)
    #update point 
    p = p + dp
    pygame.draw.circle(screen, (255, 0, 0), p, 7)


    pygame.draw.lines(screen, BLACK, False, TPS, 2)
    #pygame.draw.polygon(screen, (0, 0, 0), ((0, 100), (0, 200), (200, 200), (200, 300), (300, 150), (200, 0), (200, 100)))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.flip()
    clock.tick(60)
