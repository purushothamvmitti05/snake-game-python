import pygame
import time
import random

# Initialize Pygame
pygame.init()

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (220, 20, 60)
green = (0, 255, 0)
blue = (50, 153, 213)
purple = (128, 0, 128)

# Display
width, height = 800, 600
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("🐍 Sneaky Snake Game")

# Clock and font
clock = pygame.time.Clock()
snake_block = 20
snake_speed = 15
font_style = pygame.font.SysFont("comicsansms", 30)
score_font = pygame.font.SysFont("comicsansms", 35)

# Sound (Optional)
# Uncomment if you want sound effects
# eat_sound = pygame.mixer.Sound("eat.wav")
# gameover_sound = pygame.mixer.Sound("gameover.wav")

def your_score(score):
    value = score_font.render(f"Score: {score}", True, white)
    win.blit(value, [10, 10])

def draw_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(win, purple, [x[0], x[1], snake_block, snake_block], border_radius=5)

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    win.blit(mesg, [width / 6, height / 3])

def game_loop():
    game_over = False
    game_close = False

    x = width / 2
    y = height / 2
    x_change = 0
    y_change = 0

    snake_list = []
    length_of_snake = 1

    food_x = round(random.randrange(0, width - snake_block) / 20.0) * 20.0
    food_y = round(random.randrange(0, height - snake_block) / 20.0) * 20.0

    while not game_over:
        while game_close:
            win.fill(black)
            message("Game Over! Press C to Play Again or Q to Quit", red)
            your_score(length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -snake_block
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = snake_block
                    y_change = 0
                elif event.key == pygame.K_UP:
                    y_change = -snake_block
                    x_change = 0
                elif event.key == pygame.K_DOWN:
                    y_change = snake_block
                    x_change = 0

        if x >= width or x < 0 or y >= height or y < 0:
            # pygame.mixer.Sound.play(gameover_sound)
            game_close = True

        x += x_change
        y += y_change
        win.fill(blue)
        pygame.draw.rect(win, green, [food_x, food_y, snake_block, snake_block], border_radius=3)
        snake_head = [x, y]
        snake_list.append(snake_head)

        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for block in snake_list[:-1]:
            if block == snake_head:
                # pygame.mixer.Sound.play(gameover_sound)
                game_close = True

        draw_snake(snake_block, snake_list)
        your_score(length_of_snake - 1)
        pygame.display.update()

        if x == food_x and y == food_y:
            # pygame.mixer.Sound.play(eat_sound)
            food_x = round(random.randrange(0, width - snake_block) / 20.0) * 20.0
            food_y = round(random.randrange(0, height - snake_block) / 20.0) * 20.0
            length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

game_loop()
