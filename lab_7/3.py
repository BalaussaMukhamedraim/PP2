import pygame

# Initialize Pygame
pygame.init()

# Set up screen
WIDTH, HEIGHT = 500, 500  # Window size
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moving Ball")

# Ball settings
BALL_RADIUS = 25
ball_x, ball_y = WIDTH // 2, HEIGHT // 2  # Start in the center
BALL_COLOR = (255, 0, 0)  # Red
BG_COLOR = (255, 255, 255)  # White
MOVE_DISTANCE = 20  # Pixels per key press

running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and ball_y - BALL_RADIUS - MOVE_DISTANCE >= 0:
                ball_y -= MOVE_DISTANCE
            elif event.key == pygame.K_DOWN and ball_y + BALL_RADIUS + MOVE_DISTANCE <= HEIGHT:
                ball_y += MOVE_DISTANCE
            elif event.key == pygame.K_LEFT and ball_x - BALL_RADIUS - MOVE_DISTANCE >= 0:
                ball_x -= MOVE_DISTANCE
            elif event.key == pygame.K_RIGHT and ball_x + BALL_RADIUS + MOVE_DISTANCE <= WIDTH:
                ball_x += MOVE_DISTANCE

    # Draw everything
    screen.fill(BG_COLOR)  # Clear screen
    pygame.draw.circle(screen, BALL_COLOR, (ball_x, ball_y), BALL_RADIUS)  # Draw ball

    pygame.display.update()  # Refresh screen

pygame.quit()