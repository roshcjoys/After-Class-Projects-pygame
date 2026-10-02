import pygame

# Initialize pygame
pygame.init()
pygame.mixer.init()

# Create game window
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("My Game")

# Load background image
background = pygame.image.load("background.jpg")

# Resize background to fit the window
background = pygame.transform.scale(background, (800, 600))

# Load background music
pygame.mixer.music.load("background.mp3")

# Play music continuously
pygame.mixer.music.play(-1)

# Main game loop
running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Display background image
    screen.blit(background, (0, 0))

    # Update display
    pygame.display.update()

# Stop music
pygame.mixer.music.stop()

# Quit pygame
pygame.quit()