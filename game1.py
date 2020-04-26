import pygame
pygame.init()
screen = pygame.display.set_mode((640, 480))
background=pygame.Surface(screen.get_size())
background.fill((255,255,255))
background=background.convert()
screen.blit(background, (0,0))

mainloop=True
ballx=320
bally=240
dx=20
dy=20
clock = pygame.time.Clock()
mainloop = True
FPS = 30 # desired framerate in frames per second. try out other values !
playtime = 0.0
pygame.key.set_repeat(True)
while mainloop:
    milliseconds = clock.tick(FPS) # do not go faster than this frame rate
    playtime += milliseconds / 1000.0
    for event in pygame.event.get():
    	velocity_x = 0
    	velocity_y = 0
    if event.type==pygame.QUIT:
            mainloop=False
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            velocity_x = -20
        elif event.key == pygame.K_ESCAPE:
            mainloop = False
        elif event.key == pygame.K_RIGHT:
            velocity_x = 20
        elif event.key == pygame.K_UP:
        	velocity_y = -20
        elif event.key == pygame.K_DOWN:
        	velocity_y = 20
    elif event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT:
            velocity_x = 0
        elif event.key == pygame.K_RIGHT:
            velocity_x = 0
        elif event.key == pygame.K_UP:
        	velocity_y = 0
        elif event.key == pygame.K_DOWN:
        	velocity_y = 0

    ballx += velocity_x
    bally += velocity_y
    if ballx>=640:
        ballx = ballx-dx
    if ballx<=0:
        ballx=ballx+dx
    if bally<=0:
        bally=bally+dy
    if bally>=480:
        bally=bally-dy
    screen.blit(background, (0, 0))
    pygame.draw.circle(screen, (255, 0, 0), (ballx, bally), 25)
    pygame.display.set_caption("Frame rate: {:0.2f} frames per second." 
                               " Playtime: {:.2} seconds".format(
                               clock.get_fps(),playtime))
    pygame.display.flip()
 
print("this 'game' was played for %.2f seconds" % playtime)
pygame.quit()