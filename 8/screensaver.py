import sys
from pygame import display, draw, time, event, quit
from random import randrange

rr = randrange

MAX_ITEMS = 100
MIN_RADIUS = 20
MAX_RADIUS = 30
MAX_ACCEPTABLE_RADIUS = 80
MIN_WIDTH = 1
MAX_WIDTH = 15

assert(MIN_RADIUS > MAX_WIDTH)
clock = time.Clock()
width = 1150
height = 800
screen = display.set_mode([width, height])

def newcircle():
    return {'colour': [rr(0,255),rr(0,255),rr(0,255)],
            'center': [rr(0, width),rr(0, height)],
            'radius': rr(MIN_RADIUS,MAX_RADIUS),
            'width': rr(MIN_WIDTH,MAX_WIDTH)}


pool = []

while True:
    screen.fill([0,0,0])
    ev = event.poll()
    if ev.type > 1:
        display.quit()
        quit()
        sys.exit(0)

    if len(pool) < MAX_ITEMS:
        pool.append(newcircle())

    for item in pool:
        if item['radius'] < MAX_ACCEPTABLE_RADIUS:
            item['radius'] += 1
        else:
            pool.remove(item)
        draw.circle(screen, item['colour'], item['center'], item['radius'], item['width'])

    display.flip()
    clock.tick(60)
