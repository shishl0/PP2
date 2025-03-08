import pygame, sys, random, time

pygame.init()

# Create Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED   = (255, 0, 0)
BLUE  = (0, 0, 255)


# Game Window Dimensions and Settings
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
# Each block (snake segment and food) is a square of BLOCK_SIZE x BLOCK_SIZE pixels.
BLOCK_SIZE = 20

# Create game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake Game")

# Clock to control game speed
clock = pygame.time.Clock()

# Fonts for displaying score, level, and messages
font = pygame.font.SysFont(None, 35)

def draw_text(text, color, x, y):
    """Utility function to render and draw text on the screen."""
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

def generate_food(snake_body):
    """
    Generate a random food position ensuring:
    1. The food is not placed on the outer wall.
    2. The food does not appear on any part of the snake's body.
    """
    valid_position = False
    while not valid_position:
        # Ensure food does not fall on the wall by choosing coordinates with a margin.
        food_x = random.randint(1, (SCREEN_WIDTH - BLOCK_SIZE*2) // BLOCK_SIZE) * BLOCK_SIZE
        food_y = random.randint(1, (SCREEN_HEIGHT - BLOCK_SIZE*2) // BLOCK_SIZE) * BLOCK_SIZE
        # Shift the food so it is not flush with the wall.
        food_x += BLOCK_SIZE
        food_y += BLOCK_SIZE
        # Check that the generated position is not on the snake's body.
        if [food_x, food_y] not in snake_body:
            valid_position = True
    return food_x, food_y


# Initialize Snake Variables (Aligned to Grid)
# ------------------------------
# Starting position for the snake's head is now aligned (multiples of BLOCK_SIZE).
snake_head = [100, 40]  # 100 and 40 are both multiples of 20
# Initial snake body consisting of 3 segments.
snake_body = [
    [100, 40],
    [80, 40],
    [60, 40]
]

# Initial movement direction. Valid directions: 'RIGHT', 'LEFT', 'UP', 'DOWN'
direction = "RIGHT"
change_to = direction


# Initialize Food, Score, Level, and Speed
food_x, food_y = generate_food(snake_body)
score = 0
level = 1
# Base speed (frames per second). This will increase as the level increases.
base_speed = 3

# Main Game Loop
game_over = False
while not game_over:
    # Process Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # Check for keystrokes to change the snake's direction.
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and direction != "RIGHT":
                change_to = "LEFT"
            elif event.key == pygame.K_RIGHT and direction != "LEFT":
                change_to = "RIGHT"
            elif event.key == pygame.K_UP and direction != "DOWN":
                change_to = "UP"
            elif event.key == pygame.K_DOWN and direction != "UP":
                change_to = "DOWN"

    # Update the direction of movement.
    direction = change_to

    # Update Snake's Head Position Based on the Direction
    if direction == "RIGHT":
        snake_head[0] += BLOCK_SIZE
    elif direction == "LEFT":
        snake_head[0] -= BLOCK_SIZE
    elif direction == "UP":
        snake_head[1] -= BLOCK_SIZE
    elif direction == "DOWN":
        snake_head[1] += BLOCK_SIZE

    # Insert the new head position into the snake body list.
    snake_body.insert(0, list(snake_head))

    # Check if Snake has Eaten the Food
    if snake_head[0] == food_x and snake_head[1] == food_y:
        score += 1  # Increase score by 1
        # Increase level for every 3 foods eaten.
        if score % 3 == 0:
            level += 1
        # Generate a new food position ensuring it does not conflict with the snake or walls.
        food_x, food_y = generate_food(snake_body)
    else:
        # Remove the tail segment if food not eaten (this moves the snake forward).
        snake_body.pop()

    # Border Collision: Check if the snake hits the wall.
    if (snake_head[0] < 0 or snake_head[0] >= SCREEN_WIDTH or
        snake_head[1] < 0 or snake_head[1] >= SCREEN_HEIGHT):
        game_over = True

    # Self Collision: Check if the snake collides with its own body.
    for segment in snake_body[1:]:
        if snake_head[0] == segment[0] and snake_head[1] == segment[1]:
            game_over = True

    # Drawing Everything on the Screen
    screen.fill(BLACK)  # Clear the screen with a black background.

    # Draw the food as a red block.
    pygame.draw.rect(screen, RED, pygame.Rect(food_x, food_y, BLOCK_SIZE, BLOCK_SIZE))
    
    # Draw each segment of the snake as a green block.
    for segment in snake_body:
        pygame.draw.rect(screen, GREEN, pygame.Rect(segment[0], segment[1], BLOCK_SIZE, BLOCK_SIZE))

    # Draw the score (top left) and level (top right) counters.
    draw_text("Score: " + str(score), WHITE, 10, 10)
    draw_text("Level: " + str(level), WHITE, SCREEN_WIDTH - 150, 10)

    # Update the display
    pygame.display.update()

    # Control Game Speed: Increase speed as level increases.
    clock.tick(base_speed + (level - 1) * 2)

# Game Over: Display a Game Over Message
screen.fill(BLUE)
draw_text("Game Over! Score: " + str(score), WHITE, SCREEN_WIDTH / 6, SCREEN_HEIGHT / 3)
pygame.display.update()
time.sleep(2)
pygame.quit()
sys.exit()