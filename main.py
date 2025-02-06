import pygame

# Initialize pygame
pygame.init()

# Set up the game window
window = pygame.display.set_mode((640, 480))

FPS = 60
GRID_SIZE = 20
BORDER = pygame.Rect(0, 0, 640, 480)

# Create a board object
board = GameBoard(GRID_SIZE)

# Main loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update the game board
    board.update()

    # Draw the game board
    window.fill((255, 255, 255))
    board.draw(window)

    # Update the display
    pygame.display.flip()

# fill the functions
def start_game():

	pass

def stop_game():
	pass