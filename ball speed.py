import pygame,sys

pygame.init()
size = width, height = 600, 400
speed = [1, 1]
BLACK = 0, 0, 0
s = pygame.display.set_mode(size)
pygame.display.set_caption("ball speed")
ball = pygame.image.load(r'D:\Users\熊政\PycharmProjects\pythonProject\PYG02-ball.gif')
ballrect = ball.get_rect()
fps = 200
fclock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    ballrect = ballrect.move(speed[0], speed[1])
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = - speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = - speed[1]

    s.fill(BLACK)
    s.blit(ball, ballrect)
    pygame.display.update()
    fclock.tick(fps)

