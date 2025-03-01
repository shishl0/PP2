import pygame
import sys
import datetime
import math

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 1024, 1024
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Mickey Clock")

# load of images
body_img = pygame.image.load('/Users/zhan/Documents/PP2/Lab7/mickeyclock-body.jpg').convert_alpha()
minute_arm_img = pygame.image.load('/Users/zhan/Documents/PP2/Lab7/mickeyclock-smallArm.png').convert_alpha()
second_arm_img = pygame.image.load('/Users/zhan/Documents/PP2/Lab7/mickeyclock_longArm.png').convert_alpha()

# pivot points of each arm
minute_pivot = (67, 210)
second_pivot = (41, 272)


body_rect = body_img.get_rect()
clock_center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
body_rect.center = clock_center

def blitRotate(surf, image, pos, originPos, angle):
    image_rect = image.get_rect(topleft=(pos[0] - originPos[0], pos[1] - originPos[1]))
    
    offset_center_to_pivot = pygame.math.Vector2(pos) - image_rect.center
    
    rotated_offset = offset_center_to_pivot.rotate(-angle)
    
    rotated_image_center = (pos[0] - rotated_offset.x, pos[1] - rotated_offset.y)
    
    rotated_image = pygame.transform.rotate(image, angle)
    rotated_image_rect = rotated_image.get_rect(center=rotated_image_center)
    
    surf.blit(rotated_image, rotated_image_rect)

fps_clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((255, 255, 255))
    
    screen.blit(body_img, body_rect)
    
    # now time
    now = datetime.datetime.now()
    seconds = now.second + now.microsecond / 1e6
    minutes = now.minute + seconds / 60.0  # for smooth tick

    minute_angle = -(minutes * 6)
    second_angle = -(seconds * 6)
    

    blitRotate(screen, minute_arm_img, clock_center, minute_pivot, minute_angle)
    blitRotate(screen, second_arm_img, clock_center, second_pivot, second_angle)
    
    pygame.display.update()
    fps_clock.tick(60)