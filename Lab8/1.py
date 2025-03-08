import pygame, sys, random, time
from pygame.locals import *

pygame.init()

# Setting up FPS
FPS = 60
FramePerSec = pygame.time.Clock()

# Creating colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Other Variables for use in the program
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SPEED = 5           # Base speed for enemy and coin movement
SCORE = 0           # Score for dodged enemies
coin_count = 0      # Counter for collected coins

# Define constant sizes for the entities
PLAYER_SIZE = (50, 100)   # Constant size for the Player sprite
ENEMY_SIZE = (50, 100)    # Constant size for the Enemy sprite
COIN_SIZE = (30, 30)     # Constant size for the Coin sprite

# Setting up Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

# Load the background image
background = pygame.image.load("AnimatedStreet.png")

# Create the game display window
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Car Game")

# ------------------------------
# Define the Enemy sprite class
# ------------------------------
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Enemy.png")
        # Scale the enemy image to a constant size
        self.image = pygame.transform.scale(self.image, ENEMY_SIZE)
        self.rect = self.image.get_rect()
        # Start enemy at a random horizontal position at the top,
        self.rect.center = (
            random.randint(ENEMY_SIZE[0] // 2, SCREEN_WIDTH - ENEMY_SIZE[0] // 2),
            0
        )

    def move(self):
        global SCORE
        # Move enemy downward by SPEED pixels
        self.rect.move_ip(0, SPEED)
        # When the enemy moves off the bottom of the screen,
        # increment the score and reposition it at the top
        if self.rect.top > SCREEN_HEIGHT:
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (
                random.randint(ENEMY_SIZE[0] // 2, SCREEN_WIDTH - ENEMY_SIZE[0] // 2),
                0
            )

# ------------------------------
# Define the Player sprite class
# ------------------------------
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Player.png")
        # Scale the player image to a constant size
        self.image = pygame.transform.scale(self.image, PLAYER_SIZE)
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
        
    def move(self):
        # Movement on K_LEFT and K_RIGHT
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:        
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)

# ------------------------------
# Define the Coin sprite class
# ------------------------------
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Coin.png")
        # Scale the coin image to a constant size
        self.image = pygame.transform.scale(self.image, COIN_SIZE)
        self.rect = self.image.get_rect()
        # Set the coin's starting position at a random horizontal position along the top
        self.rect.center = (
            random.randint(COIN_SIZE[0] // 2, SCREEN_WIDTH - COIN_SIZE[0] // 2),
            0
        )
        
    def move(self):
        # Move coin downward by SPEED pixels
        self.rect.move_ip(0, SPEED)
        # Remove the coin if it moves off the bottom of the screen
        if self.rect.top > SCREEN_HEIGHT:
            self.kill()

# ------------------------------
# Instantiate game sprites
# ------------------------------
P1 = Player()
E1 = Enemy()

# Creating Sprite Groups
enemies = pygame.sprite.Group()
enemies.add(E1)

coins = pygame.sprite.Group()  # Group to hold coin sprites

all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)

# ------------------------------
# Set up a timer event to increment speed
# ------------------------------
INC_SPEED = pygame.USEREVENT + 0.5
pygame.time.set_timer(INC_SPEED, 1000)

# ------------------------------
# Main Game Loop
# ------------------------------
while True:
    # Process events
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 0.5  # Gradually increase game speed
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    # Randomly spawn coins with an approximate 2% chance per frame
    if random.randint(1, 100) < 2:
        new_coin = Coin()
        coins.add(new_coin)
        all_sprites.add(new_coin)
    
    # Draw the background first so that sprites appear on top
    DISPLAYSURF.blit(background, (0, 0))
    
    # Render and display the score (number of enemies dodged) at the top left
    score_text = font_small.render("Score: " + str(SCORE), True, BLACK)
    DISPLAYSURF.blit(score_text, (10, 10))
    
    # Render and display the coin count at the top right
    coin_text = font_small.render("Coins: " + str(coin_count), True, BLACK)
    coin_text_rect = coin_text.get_rect(topright=(SCREEN_WIDTH - 10, 10))
    DISPLAYSURF.blit(coin_text, coin_text_rect)
    
    # Update and draw all sprites
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()
    
    # Check for collisions between the player and coins
    coins_collected = pygame.sprite.spritecollide(P1, coins, True)
    if coins_collected:
        coin_count += len(coins_collected)
    
    # Check for collision between the player and any enemy
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound('crash.wav').play()
        time.sleep(0.5)
        
        # Display the game over screen
        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over, (30, 250))
        pygame.display.update()
        
        # Remove all sprites from the screen
        for entity in all_sprites:
            entity.kill() 
        time.sleep(2)
        pygame.quit()
        sys.exit()        
    
    # Update the display and tick the FPS clock
    pygame.display.update()
    FramePerSec.tick(FPS)