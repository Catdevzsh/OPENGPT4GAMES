import pygame
import random

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Snake')

clock = pygame.time.Clock()
block_size = 10
FPS = 15

font = pygame.font.Font(None, 36)

def snake(block_list):
    for block in block_list:
        pygame.draw.rect(gameDisplay, black, [block[0], block[1], block_size, block_size])

def message_to_screen(msg, color):
    screen_text = font.render(msg, True, color)
    gameDisplay.blit(screen_text, [display_width/2, display_height/2])

def score_to_screen(score):
    score_text = font.render("Score: " + str(score), True, black)
    gameDisplay.blit(score_text, [0, 0])

def gameLoop():
    gameExit = False
    gameOver = False

    lead_x = display_width / 2
    lead_y = display_height / 2
    lead_x_change = 0
    lead_y_change = 0

    block_list = []
    block_num = 1

    score = 0

    fruit_x = round(random.randrange(0, display_width - block_size) / 10.0) * 10.0
    fruit_y = round(random.randrange(0, display_height - block_size) / 10.0) * 10.0

    while not gameExit:
        while gameOver == True:
            gameDisplay.fill(white)
            message_to_screen("Game Over! Press C to play again or Q to quit.", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOver = False
                    gameExit = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    lead_x_change = -block_size
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    lead_x_change = block_size
                    lead_y_change = 0
                elif event.key == pygame.K_UP:
                    lead_y_change = -block_size
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    lead_y_change = block_size
                    lead_x_change = 0

        if lead_x >= display_width or lead_x < 0 or lead_y >= display_height or lead_y < 0:
            gameOver = True

        lead_x += lead_x_change
        lead_y += lead_y_change

        gameDisplay.fill(white)

        pygame.draw.rect(gameDisplay, green, [fruit_x, fruit_y, block_size, block_size])

        block_list.append([lead_x, lead_y])
        if len(block_list) > block_num:
            del block_list[0]

        for eachSegment in block_list[:-1]:
            if eachSegment == [lead_x, lead_y]:
                gameOver = True

        snake(block_list)
        score_to_screen(score)

        pygame.display.update()

        if lead_x == fruit_x and lead_y == fruit_y:
            fruit_x = round(random.randrange(0, display_width - block_size) / 10.0) * 10.0
            fruit_y = round(random.randrange(0, display_height - block_size) / 10.0) * 10.0
            block_num += 1
            score += 1

        clock.tick(FPS)

    pygame.quit()
    quit()

gameLoop() ## PLZ AI really i need thsi to behave and have the score fruit and everything the orgiinaL snake did
