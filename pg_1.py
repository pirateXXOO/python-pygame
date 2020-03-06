import pygame
import sys
# init pygame
pygame.init()

size = width, height = 900, 900
speed = [-2, 1]
bg = (255, 255, 255)

# create a window Surface
screen = pygame.display.set_mode(size)

# config window title
pygame.display.set_caption("Nice to meet you!")

# load picture
turtle = pygame.image.load("tortoise.jfif")

# get picture square
position = turtle.get_rect()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    # move picture
    position = position.move(speed)

    if position.left < 0 or position.right > width:
        # flip picture
        turtle = pygame.transform.flip(turtle, True, False)
        # move opposite direction
        speed[0] = -speed[0]

    if position.top < 0 or position.bottom > height:
        speed[1] = -speed[1]

    # fill background
    screen.fill(bg)
    # update picture
    screen.blit(turtle, position)
    # update interface
    pygame.display.flip()
    # delay 10 ms
    pygame.time.delay(10)

