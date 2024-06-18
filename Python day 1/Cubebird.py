import pygame
import random

# Initialize the pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Cube bird V1")
WIDTH, HEIGHT = 640, 480
FONT_SIZE = 24
font = pygame.font.Font(None, FONT_SIZE)
text = "Hello, World!"
# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
BIRD_COLOR = (255, 255, 0)
PIPE_COLOR = (0, 255, 0)
FLOOR_COLOR = (139, 69, 19)
BACKGROUND_COLOR = (135, 206, 235)
BUTTON_COLOR = (0, 255, 255)
BUTTON_HOVER_COLOR = (0, 200, 200)

# Game variables
clock = pygame.time.Clock()
FPS = 60

# Bird variables
BIRD_WIDTH = 34
BIRD_HEIGHT = 24
bird_x = SCREEN_WIDTH // 4
bird_y = SCREEN_HEIGHT // 2
bird_velocity = 0
gravity = 0.5
jump = -10

# Pipe variables
PIPE_WIDTH = 52
PIPE_HEIGHT = 320
PIPE_GAP = 150
pipe_velocity = -4
pipe_frequency = 1500  # milliseconds
last_pipe = pygame.time.get_ticks() - pipe_frequency
pipes = []

# Floor variables
FLOOR_HEIGHT = 50
floor_y = SCREEN_HEIGHT - FLOOR_HEIGHT

# Game states
RUNNING = 0
GAME_OVER = 1
game_state = RUNNING

# Button dimensions
BUTTON_WIDTH = 100
BUTTON_HEIGHT = 50

def draw_bird(x, y):
    pygame.draw.rect(screen, BIRD_COLOR, (x, y, BIRD_WIDTH, BIRD_HEIGHT))

def create_pipe():
    pipe_height = random.randint(100, 400)
    top_pipe = pygame.Rect(SCREEN_WIDTH, pipe_height - PIPE_HEIGHT, PIPE_WIDTH, PIPE_HEIGHT)
    bottom_pipe = pygame.Rect(SCREEN_WIDTH, pipe_height + PIPE_GAP, PIPE_WIDTH, PIPE_HEIGHT)
    return top_pipe, bottom_pipe

def move_pipes(pipes):
    for pipe in pipes:
        pipe.x += pipe_velocity
    return [pipe for pipe in pipes if pipe.x > -PIPE_WIDTH]

def draw_pipes(pipes):
    for pipe in pipes:
        pygame.draw.rect(screen, PIPE_COLOR, pipe)

def draw_floor():
    pygame.draw.rect(screen, FLOOR_COLOR, (0, floor_y, SCREEN_WIDTH, FLOOR_HEIGHT))

def check_collision(pipes, bird_rect):
    for pipe in pipes:
        if bird_rect.colliderect(pipe):
            return True
    if bird_rect.top <= 0:
        return True
    return False

def draw_button(text, x, y, w, h, color, hover_color):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(screen, hover_color, (x, y, w, h))
        if click[0] == 1:
            return True
    else:
        pygame.draw.rect(screen, color, (x, y, w, h))
    small_text = pygame.font.Font("freesansbold.ttf", 20)
    text_surf = small_text.render(text, True, BLACK)
    text_rect = text_surf.get_rect(center=(x + w // 2, y + h // 2))
    screen.blit(text_surf, text_rect)
    return False

def game_over_screen():
    screen.fill(BACKGROUND_COLOR)
    large_text = pygame.font.Font('freesansbold.ttf', 50)
    large_text2 = pygame.font.Font('freesansbold.ttf', 14)
    text_surf = large_text.render('Game over', True, RED)
    text_rect = text_surf.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 4))
    screen.blit(text_surf, text_rect)
   
    text_surf2 = large_text2.render('https://github.com/Aapoxz/MyRoadToLearnPython', True, BLACK)
    text_rect2 = text_surf.get_rect(center=(SCREEN_WIDTH // 2.5, SCREEN_HEIGHT // 2.5))
    screen.blit(text_surf2, text_rect2)
    pygame.display.update()


def reset_game():
    global bird_x, bird_y, bird_velocity, pipes, last_pipe, game_state
    bird_x = SCREEN_WIDTH // 4
    bird_y = SCREEN_HEIGHT // 2
    bird_velocity = 0
    pipes = []
    last_pipe = pygame.time.get_ticks() - pipe_frequency
    game_state = RUNNING

# Game loop
running = True
while running:
    if game_state == RUNNING:
        screen.fill(BACKGROUND_COLOR)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE) or \
               (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
                bird_velocity = jump

        bird_velocity += gravity
        bird_y += bird_velocity

        # Prevent bird from falling below the floor
        if bird_y >= floor_y - BIRD_HEIGHT:
            bird_y = floor_y - BIRD_HEIGHT
            bird_velocity = 0

        # Create new pipes
        time_now = pygame.time.get_ticks()
        if time_now - last_pipe > pipe_frequency:
            pipes.extend(create_pipe())
            last_pipe = time_now

        # Move pipes
        pipes = move_pipes(pipes)

        # Draw bird
        draw_bird(bird_x, bird_y)

        # Draw pipes
        draw_pipes(pipes)

        # Draw floor
        draw_floor()

        # Check for collisions
        bird_rect = pygame.Rect(bird_x, bird_y, BIRD_WIDTH, BIRD_HEIGHT)
        if check_collision(pipes, bird_rect):
            game_state = GAME_OVER

        pygame.display.update()
        clock.tick(FPS)
    
    elif game_state == GAME_OVER:
         game_over_screen()
   

pygame.quit()
