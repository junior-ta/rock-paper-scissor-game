import pygame
import random

# Initialize pygame
pygame.init()

# Screen dimensions
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Rock Paper Scissors")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

# Fonts
font = pygame.font.Font(None, 74)
small_font = pygame.font.Font(None, 36)

# Game images (you'll need to load appropriate images)
rock_img = pygame.image.load('rock-paper-scissors-296854_1280.png')
paper_img = pygame.image.load('rock-paper-scissors-296855_1280.png')
scissor_img = pygame.image.load('rock-paper-scissors-296853_1280.png')

# Rescale images if necessary
rock_img = pygame.transform.scale(rock_img, (150, 150))
paper_img = pygame.transform.scale(paper_img, (150, 150))
scissor_img = pygame.transform.scale(scissor_img, (150, 150))

# Game variables
options = ["rock", "paper", "scissor"]
playerScore = 0
opponentScore = 0
rounds = 3

# Player name input variable
playerName = ""
entering_name = True  # This will control whether we are on the home screen

# Function to display text
def display_message(text, x, y, size="large"):
    if size == "large":
        label = font.render(text, True, BLACK)
    else:
        label = small_font.render(text, True, BLACK)
    screen.blit(label, (x, y))

# Home screen function to ask for the player's name
def home_screen():
    global playerName
    input_box = pygame.Rect(200, 300, 400, 50)
    color_inactive = GRAY
    color_active = BLACK
    color = color_inactive
    active = False
    text = ''
    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # If the user clicked on the input box
                if input_box.collidepoint(event.pos):
                    active = True
                else:
                    active = False
                color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        playerName = text
                        done = True
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode
        
        # Render the current text
        screen.fill(WHITE)
        display_message("Enter Your Name:", 200, 200)
        txt_surface = font.render(text, True, color)
        width = max(400, txt_surface.get_width() + 10)
        input_box.w = width
        screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
        pygame.draw.rect(screen, color, input_box, 2)
        
        pygame.display.flip()

# Function to display the game choices
def draw_choices():
    screen.blit(rock_img, (50, 300))
    screen.blit(paper_img, (300, 300))
    screen.blit(scissor_img, (550, 300))

# Main game loop
def game_loop():
    global playerScore, opponentScore
    running = True
    while running:
        screen.fill(WHITE)

        # Title and player name
        display_message(f"Rock Paper Scissors - {playerName}", 50, 50, size="small")

        # Display score
        display_message(f"Player Score: {playerScore}", 50, 150, size="small")
        display_message(f"Opponent Score: {opponentScore}", 500, 150, size="small")

        # Display choices
        draw_choices()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Check for mouse clicks on images
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()

                # Player clicks on rock
                if 50 <= mouse_pos[0] <= 200 and 300 <= mouse_pos[1] <= 450:
                    playerChoice = "rock"
                # Player clicks on paper
                elif 300 <= mouse_pos[0] <= 450 and 300 <= mouse_pos[1] <= 450:
                    playerChoice = "paper"
                # Player clicks on scissor
                elif 550 <= mouse_pos[0] <= 700 and 300 <= mouse_pos[1] <= 450:
                    playerChoice = "scissor"
                else:
                    playerChoice = None

                if playerChoice:
                    opponentChoice = random.choice(options)
                    if playerChoice == opponentChoice:
                        display_message("Tie! Replay the round!", 250, 500)
                    elif (playerChoice == "rock" and opponentChoice == "scissor") or \
                         (playerChoice == "paper" and opponentChoice == "rock") or \
                         (playerChoice == "scissor" and opponentChoice == "paper"):
                        playerScore += 1
                        display_message(f"{playerChoice.capitalize()} beats {opponentChoice}!", 200, 500)
                    else:
                        opponentScore += 1
                        display_message(f"{opponentChoice.capitalize()} beats {playerChoice}!", 200, 500)

                    pygame.display.flip()
                    pygame.time.wait(2000)  # Pause before next round

        pygame.display.flip()

    pygame.quit()

# Main execution
home_screen()  # Ask for player's name first
game_loop()    # Start the game after the name is entered
