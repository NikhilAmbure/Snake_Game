import pygame
import  random
import os

pygame.mixer.init()

pygame.init() # compulsory to run

# Colors  RGB values = 0 - 255
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
aqua = (0, 255, 255)
darkselmon = (233, 150, 122)

screen_width = 900
screen_height = 600

# Creating Window
Game_Window = pygame.display.set_mode((screen_width, screen_height))

# Background image
bgimage = pygame.image.load('snake.webp')
bgimage = pygame.transform.scale(bgimage, (screen_width, screen_height)).convert_alpha()

# Game Title
pygame.display.set_caption("SnakesWithGodThor")
pygame.display.update()
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 55)

def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    Game_Window.blit(screen_text, [x, y])

def plot_snake(Game_Window, color, snk_list, snake_size):  # food plotting
    for x, y in snk_list:
        pygame.draw.rect(Game_Window, color, [x, y, snake_size, snake_size])

# Welcome Screen
def welcome():
    exit_game = False

    # Game Loop
    while not exit_game:

        Game_Window.fill(darkselmon)
        text_screen("Snake World", aqua, 290, 250)
        text_screen("Press Space Bar to Play", aqua, 240, 300)

        # Exit Event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.mixer.music.load('back.mp3')
                    pygame.mixer.music.play()
                    gameloop()

        pygame.display.update()
        clock.tick(60)


# Game Loop
def gameloop():
    # reads highscore
    # Check if highscore file exist - bug
    if (not os.path.exists("Highscore.txt")):
        with open("Highscore.txt", "w") as f:
            f.write("0")

    with open("Highscore.txt", "r") as f:
        highscore = f.read()

    # Game specific variables
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    velocity_x = 0
    velocity_y = 0
    food_x = random.randint(10, screen_width / 2)  # food position
    food_y = random.randint(10, screen_height / 2)

    snake_size = 20  # snake size at start
    fps = 60  # game smoothness
    score = 0
    init_velocity = 5  # velocity of snake

    snk_list = []
    snk_length = 1

    while not exit_game:

        if game_over:
            # highscore before
            with open("Highscore.txt", "w") as f:
                f.write(str(highscore))
            Game_Window.fill(white)
            text_screen("Game Over! Press Enter To Continue", red, 100, 250)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # for quit
                    exit_game = True

                # Game Over !
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcome()

        else:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # for quit
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_LEFT:
                        velocity_x = -init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_UP:
                        velocity_y = -init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0

                    # Cheat codes
                    if event.key == pygame.K_q:
                        score +=10


            # Runs diagonally snake
            snake_x += velocity_x
            snake_y += velocity_y

            # food eating and score
            # sensitivity
            if abs(snake_x - food_x) < 10 and abs(snake_y - food_y) < 10:
                score += 10
                food_x = random.randint(0, screen_width / 2)
                food_y = random.randint(0, screen_height / 2)
                snk_length += 5  # snake length
                if score > int(highscore):
                    highscore = score

            Game_Window.fill(white)
            # Background image
            Game_Window.blit(bgimage, (0, 0))
            text_screen("Score : " + str(score) + "  HighScore: " + str(highscore), red, 5, 5)
            pygame.draw.rect(Game_Window, red, [food_x, food_y, snake_size, snake_size])

            # snake length and list
            # adding elements in list to start the game
            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            # control...
            if len(snk_list) > snk_length:
                del snk_list[0]

            # Game Over when snake collides itself
            if head in snk_list[:-1]:
                game_over = True
                pygame.mixer.music.load('landslide.mp3')
                pygame.mixer.music.play()

            # Game Over!
            if snake_x < 0 or snake_x>screen_width or snake_y < 0 or snake_y>screen_height:
                pygame.mixer.music.load('landslide.mp3')
                pygame.mixer.music.play()
                game_over = True
                # print("Game Over!")

            # Creating snake head
            # pygame.draw.rect(Game_Window, black, [snake_x, snake_y, snake_size, snake_size])
            # pasiing draw.rect in plot_snake
            plot_snake(Game_Window, black, snk_list, snake_size)

        pygame.display.update()  # for update screen
        clock.tick(fps)

    pygame.quit()
    quit()

welcome()



# to Do so... :
# Add image for game over
# Add image for welcome page
# Add various images for game over and welcome
# use different fonts
