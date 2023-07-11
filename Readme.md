# Snake_Game
Let's Explain how code actually works.

This code is an example of a simple snake game implemented using the Pygame library in Python. Let's go through it step by step:

1. Import necessary modules: The code begins by importing the required modules - pygame, random, and os. These modules are required for graphics, random number generation, and file operations respectively.

2. Initialize Pygame: The `pygame.init()` function is called to initialize all the pygame modules that are required for the game to run. This function is compulsory to run before using any pygame functionality.

3. Set up the window: The dimensions of the game window (screen_width and screen_height) are defined. The `pygame.display.set_mode()` function is used to create the game window with the specified dimensions.

4. Load and set up the background image: The game's background image is loaded using the `pygame.image.load()` function. The image is then scaled to fit the size of the game window using `pygame.transform.scale()`. Finally, the image is converted to the appropriate format using `convert_alpha()`. The image is stored in the variable `bgimage`.

5. Set the game title: The game window's title is set using the `pygame.display.set_caption()` function. In this case, the title is set to "SnakesWithGodThor".

6. Create helper functions: Two helper functions are defined in this code:
   - `text_screen(text, color, x, y)`: This function is used to render and display text on the game window. It takes in parameters like the text to display, color of the text, and the (x, y) coordinate of the text's position on the screen. The `font.render()` function is used to render the text, and `Game_Window.blit()` is used to display it on the screen.
   - `plot_snake(Game_Window, color, snk_list, snake_size)`: This function is used to draw the snake on the game window. It takes in parameters like the game window surface, color of the snake, the list of snake segments, and the size of each snake segment. It uses the `pygame.draw.rect()` function to draw rectangles for each segment of the snake, based on the coordinates stored in the `snk_list` list.

7. Implement the welcome screen: The `welcome()` function is defined to display the welcome screen of the game. It creates a game loop that displays the welcome screen text and waits for user input. If the user presses the space bar, it plays background music and calls the `gameloop()` function to start the game.

8. Implement the game loop: The `gameloop()` function is defined to handle the main game logic. It also manages game over conditions and updates the score. The function first checks if a high score file exists and creates one if it doesn't. It then reads the current high score from the file.

9. Set up game variables: The relevant game variables are initialized, including:
   - `exit_game` and `game_over` flags to control the main game loop.
   - `snake_x` and `snake_y` to store the coordinates of the snake's head.
   - `velocity_x` and `velocity_y` to store the movement speed and direction of the snake.
   - `food_x` and `food_y` to store the coordinates of the food item.
   - `snake_size` to define the size of each segment of the snake.
   - `score` to keep track of the player's score.
   - `init_velocity` as the initial velocity of the snake.
   - `snk_list` to store the coordinates of all the segments of the snake.
   - `snk_length` to track the length of the snake.

10. Game loop logic: The game loop is implemented using a while loop that continues until the `exit_game` flag is set to True. Within the loop, it checks for events (user input, window close, etc.) and performs the necessary actions accordingly.

11. Game over handling: If the `game_over` flag is True, it saves the high score and displays the game over message on the screen. If the player presses the enter key, it calls the `welcome()` function to return to the welcome screen.

12. Snake movement and collision handling: If the game is not over, the function checks for keyboard input to control the snake's movement. It updates the snake's position based on the velocity values. It also handles food eating by checking if the snake's head collides with the food item. If they collide, the player's score is increased, a new food item is randomly placed, and the snake's length is increased. If the snake's head collides with any part of its body, it sets the `game_over` flag to True.

13. Game over conditions: The function also checks for game over conditions like the snake hitting the walls of the game window. If any of these conditions are met, it sets the `game_over` flag to True and plays a game over sound effect.

14. Drawing the game screen: The current score, high score, and the food item are displayed on the game window using the `text_screen()` function. The snake is drawn on the window using the `plot_snake()` function.

15. Update the display and control the frame rate: The `pygame.display.update()` function is called to update the game window, and the `clock.tick(fps)` function is used to control the frame rate of the game.

16. Quit the game: When the game loop ends, the `pygame.quit()` function is called to uninitialize pygame, and the `quit()` function is called to exit the program.

17. Start the game: The `welcome()` function is called at the end of the code to start the game by displaying the welcome screen.

That's a detailed breakdown of the code. This should give you a better understanding of how the snake game is implemented using the Pygame library in Python.
