import pygame
import random
import sys


pygame.init()

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

BIRD_SIZE = 30
BIRD_X = 100
BIRD_Y = SCREEN_HEIGHT // 2
GRAVITY = 1
FLAP_STRENGTH = -10


PIPE_WIDTH = 50
PIPE_GAP = 200
PIPE_SPEED = 3

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Flappy Bird Clone")

clock = pygame.time.Clock()


def draw_bird(x, y):
    pygame.draw.rect(screen, BLACK, (x, y, BIRD_SIZE, BIRD_SIZE))


def draw_pipes(pipe_x, pipe_height):
    pygame.draw.rect(screen, GREEN, (pipe_x, 0, PIPE_WIDTH, pipe_height))
    pygame.draw.rect(screen, GREEN, (pipe_x, pipe_height + PIPE_GAP, PIPE_WIDTH, SCREEN_HEIGHT - pipe_height - PIPE_GAP))

def check_collision(bird_y, pipe_x, pipe_height):
    if bird_y < 0 or bird_y + BIRD_SIZE > SCREEN_HEIGHT:
        return True
    if BIRD_X + BIRD_SIZE > pipe_x and BIRD_X < pipe_x + PIPE_WIDTH:
        if bird_y < pipe_height or bird_y + BIRD_SIZE > pipe_height + PIPE_GAP:
            return True
    return False


def game_loop():
    bird_y = BIRD_Y
    bird_velocity = 0
    pipe_x = SCREEN_WIDTH
    pipe_height = random.randint(100, 400)
    score = 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bird_velocity = FLAP_STRENGTH

        bird_velocity += GRAVITY
        bird_y += bird_velocity

        pipe_x -= PIPE_SPEED
        if pipe_x + PIPE_WIDTH < 0:
            pipe_x = SCREEN_WIDTH
            pipe_height = random.randint(100, 400)
            score += 1


        if check_collision(bird_y, pipe_x, pipe_height):
            running = False


        screen.fill(WHITE)
        draw_bird(BIRD_X, bird_y)
        draw_pipes(pipe_x, pipe_height)

        font = pygame.font.SysFont(None, 35)
        score_text = font.render(f"Score: {score}", True, BLACK)
        screen.blit(score_text, (10, 10))
    
        pygame.display.update()
        clock.tick(30)

    pygame.quit()
    sys.exit()


game_loop()  