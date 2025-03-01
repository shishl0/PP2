import pygame
import sys

pygame.init()


SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Red Ball Movement")

# Circle params
BALL_RADIUS = 25
BALL_COLOR = (255, 0, 0) # red color
BALL_SPEED = 20

# starting point
ball_x = SCREEN_WIDTH // 2
ball_y = SCREEN_HEIGHT // 2


running = True
while running:
    screen.fill((255, 255, 255)) #bg color
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and ball_y - BALL_RADIUS - BALL_SPEED >= 0:
                ball_y -= BALL_SPEED
            elif event.key == pygame.K_DOWN and ball_y + BALL_RADIUS + BALL_SPEED <= SCREEN_HEIGHT:
                ball_y += BALL_SPEED
            elif event.key == pygame.K_LEFT and ball_x - BALL_RADIUS - BALL_SPEED >= 0:
                ball_x -= BALL_SPEED
            elif event.key == pygame.K_RIGHT and ball_x + BALL_RADIUS + BALL_SPEED <= SCREEN_WIDTH:
                ball_x += BALL_SPEED

    pygame.draw.circle(screen, BALL_COLOR, (ball_x, ball_y), BALL_RADIUS)

    pygame.display.flip()
    pygame.time.delay(30)

pygame.quit()
sys.exit()