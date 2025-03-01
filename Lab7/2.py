import pygame
import sys
import os

# init of Pygame and mixer(for music).
pygame.init()
pygame.mixer.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 1000, 400
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Music Player")

# auto search of mp3 files in current dir
playlist = [file for file in os.listdir() if file.endswith(".mp3")]

if not playlist:
    print("No music files found in the directory!")
    sys.exit()

current_track = 0

# load of first track
pygame.mixer.music.load(playlist[current_track])

# Text to show 
font = pygame.font.Font(None, 36)
instructions = [
    "Press P to Play",
    "Press S to Stop",
    "Press N for Next Track",
    "Press B for Previous Track",
    "Press ESC to Quit"
]
instruction_surfaces = [font.render(text, True, (255, 255, 255)) for text in instructions]

def draw_instructions():
    """Draw of text"""
    screen.fill((0, 0, 0))
    y = 20
    for surface in instruction_surfaces:
        screen.blit(surface, (20, y))
        y += 40
    
    # "Now playin" renderer
    track_name = font.render(f"Now Playing: {playlist[current_track]}", True, (255, 255, 0))
    screen.blit(track_name, (20, y + 20))
    
    pygame.display.flip()


running = True
while running:
    draw_instructions()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

            elif event.key == pygame.K_p:
                pygame.mixer.music.play()

            elif event.key == pygame.K_s:
                pygame.mixer.music.stop()

            elif event.key == pygame.K_n:
                current_track = (current_track + 1) % len(playlist)
                pygame.mixer.music.load(playlist[current_track])
                pygame.mixer.music.play()

            elif event.key == pygame.K_b:
                current_track = (current_track - 1) % len(playlist)
                pygame.mixer.music.load(playlist[current_track])
                pygame.mixer.music.play()

pygame.quit()
sys.exit()