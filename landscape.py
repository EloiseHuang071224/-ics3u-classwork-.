import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Simple Landscape')

# Define colors
sky_blue = (135, 206, 250)
grass_green = (34, 139, 34)
sun_yellow = (255, 255, 0)
tree_brown = (139, 69, 19)
tree_green = (0, 100, 0)
cloud_white = (255, 255, 255)
mountain_gray = (128, 128, 128)
river_blue = (0, 191, 255)

# Sun properties
sun_radius = 50
sun_x = 0
sun_speed = 1  # Speed of the sun's movement

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the sun
    sun_x += sun_speed
    if sun_x > width + sun_radius:
        sun_x = -sun_radius  # Reset to start position when it goes off-screen

    # Fill the screen with sky color
    screen.fill(sky_blue)

    # Draw the grass
    pygame.draw.rect(screen, grass_green, (0, height // 2, width, height // 2))

    # Draw the sun
    pygame.draw.circle(screen, sun_yellow, (sun_x, height // 4), sun_radius)

    # Draw the tree trunk
    pygame.draw.rect(screen, tree_brown, (width // 2 - 10, height // 2 + 50, 20, 100))

    # Draw the tree leaves
    pygame.draw.polygon(screen, tree_green, [(width // 2 - 60, height // 2 + 50), 
                                             (width // 2 + 60, height // 2 + 50), 
                                             (width // 2, height // 2 - 10)])

    # Draw clouds
    pygame.draw.circle(screen, cloud_white, (150, 100), 30)
    pygame.draw.circle(screen, cloud_white, (200, 100), 30)
    pygame.draw.circle(screen, cloud_white, (175, 80), 20)

    # Draw mountains
    pygame.draw.polygon(screen, mountain_gray, [(100, height // 2 - 50), (300, height // 2 - 150), (500, height // 2 - 50)])
    pygame.draw.polygon(screen, mountain_gray, [(600, height // 2 - 50), (700, height // 2 - 100), (800, height // 2 - 50)])

    # Draw a river
    pygame.draw.polygon(screen, river_blue, [(100, height // 2 + 100), (700, height // 2 + 100), (750, height // 2 + 150), (50, height // 2 + 150)])

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(60)  # 60 frames per second

# Quit Pygame
pygame.quit()
sys.exit()
