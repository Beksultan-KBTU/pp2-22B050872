import pygame, math, datetime

pygame.init()

mickey = pygame.transform.scale(pygame.image.load('mickey.png'), (780, 740))
left_hand = pygame.transform.scale(pygame.image.load('left_hand.png'), (375, 115))
right_hand = pygame.transform.scale(pygame.image.load('right_hand.png'), (297, 161))

center = (400, 400)
screen = pygame.display.set_mode((800, 800))
fps = 120
clock = pygame.time.Clock()

def polar_to_cartesian(r, theta):
    x = r * sin(pi * theta / 180)
    y = r * cos(pi * theta / 180)
    return x + 400, - (y - 400)

def blitRotateCenter(surf, image, topleft, angle):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center = image.get_rect(topleft = topleft).center)
    surf.blit(rotated_image, new_rect)

def blitRotate(surf, image, pos, originPos, angle):
    image_rect = image.get_rect(topleft = (pos[0] - originPos[0], pos[1] - originPos[1]))
    offset_center_to_pivot = pygame.math.Vector2(pos) - image_rect.center
    rotated_offset = offset_center_to_pivot.rotate(angle)
    rotated_image_center = (pos[0] - rotated_offset.x, pos[1] - rotated_offset.y)
    rotated_image = pygame.transform.rotate(image, -angle)
    rotated_image_rect = rotated_image.get_rect(center = rotated_image_center)
    surf.blit(rotated_image, rotated_image_rect)

def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((255, 255, 255))
        screen.blit(mickey, (10, 30))
        current_date_time = datetime.datetime.now()
        minute = current_date_time.minute
        second = current_date_time.second

        theta = (minute + second / 60) * (360 / 60)
        blitRotate(screen, right_hand, center, (right_hand.get_width() / 2 + 110, left_hand.get_height() / 2 + 75), theta + 75)

        theta = second * (360 / 60)
        blitRotate(screen, left_hand, center, (left_hand.get_width() / 2 - 145, left_hand.get_height() / 2), theta - 87)
        pygame.display.update()

    clock.tick(FPS)
    pygame.quit()

main()