import pygame

pygame.init()
screen = pygame.display.set_mode((510, 510))
done = False
color = (255, 0, 0)
x = 25
y = 25

clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP] and y > 25: y -= 20
    if pressed[pygame.K_DOWN] and y < 485: y += 20
    if pressed[pygame.K_LEFT] and x > 25: x -= 20
    if pressed[pygame.K_RIGHT] and x < 485: x += 20
    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, color, (x, y), 25)
    pygame.display.flip()
    clock.tick(60)