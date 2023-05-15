import pygame

# Initialize Pygame
pygame.init()

# Set up the game window
width = 800
height = 600
game_window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Weight Loss Game")

# Load character sprite
character_sprite = pygame.image.load("character.png")
character_sprite = pygame.transform.scale(character_sprite, (80, 120))

# Character properties
character_x = 50
character_y = height // 2 - 60
character_speed = 5
character_is_jumping = False
character_jump_height = 150
character_weight = 100
character_has_eczema = True

# Load level sprite
level_sprite = pygame.image.load("level.png")
level_sprite = pygame.transform.scale(level_sprite, (50, 50))

# Level properties
levels = [
    {"x": 200, "y": height - 100},
    {"x": 400, "y": height - 150},
    {"x": 600, "y": height - 200},
]

# Start screen
start_font = pygame.font.Font(None, 60)
start_text = start_font.render("Weight Loss Game", True, (0, 0, 0))
start_text_rect = start_text.get_rect(center=(width // 2, height // 2))

# Game state
game_active = False

# Game loop
running = True
clock = pygame.time.Clock()
while running:
    clock.tick(60)  # Limit the frame rate to 60 FPS

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if game_active:
                    if not character_is_jumping:
                        character_is_jumping = True
                else:
                    game_active = True

    if game_active:
        # Update character position
        if character_is_jumping:
            character_y -= character_speed
            if character_y <= character_jump_height:
                character_is_jumping = False
        else:
            character_y += character_speed
            if character_y >= height - 120:
                character_y = height - 120

    # Draw the game window
    game_window.fill((255, 255, 255))  # Fill the window with white color

    if game_active:
        # Draw character on the window
        game_window.blit(character_sprite, (character_x, character_y))

        # Draw eczema
        if character_has_eczema:
            pygame.draw.rect(game_window, (255, 0, 0), (character_x + 20, character_y - 10, 10, 10))
            pygame.draw.rect(game_window, (255, 0, 0), (character_x + 50, character_y - 10, 10, 10))

        # Draw levels on the window
        for level in levels:
            game_window.blit(level_sprite, (level["x"], level["y"]))
    else:
        # Draw start screen
        game_window.blit(start_text, start_text_rect)

    pygame.display.update()

# Quit the game
pygame.quit()
