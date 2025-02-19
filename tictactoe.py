import pygame
from gameLogic import TicTacToe

pygame.init()
screenWidth = 600
screenHeight = 600
screen = pygame.display.set_mode((screenWidth, screenHeight)) #creates and assigns game window
pygame.display.set_caption('Tic-Tac-Toe') #window name
icon_image = pygame.image.load('Images/tictac.jpg').convert_alpha() #loads in icon
icon_image = pygame.transform.scale(icon_image, (32, 32))  # resize to 32x32
pygame.display.set_icon(icon_image)

screen.fill((255, 255, 255)) #background color
gridLines = [
    pygame.Rect(200, 0, 1, 600), pygame.Rect(400, 0, 1, 600), #vertical gridlines
    pygame.Rect(0, 200, 600, 1), pygame.Rect(0, 400, 600, 1) #horizontal gridlines
]
for lines in gridLines:
    pygame.draw.rect(screen, (0, 0, 0), lines) #draws gridlines

game = TicTacToe() #class instance

oImage = pygame.image.load('Images/O.png').convert_alpha() #loads in O
xImage = pygame.image.load('Images/X.png').convert_alpha() #loads in X

def reset_game():
    global game
    game = TicTacToe()  # Reset the TicTacToe instance
    screen.fill((255, 255, 255))  # Clear the screen and redraw the grid
    for lines in gridLines:
        pygame.draw.rect(screen, (0, 0, 0), lines)  # Redraw the grid
    pygame.display.update()  # Update display

def imageLoader(x, y, image):
    newImage = pygame.transform.scale(image, (175, 175)) #resizes images
    screen.blit(newImage, (x * 199 + 12, y * 199 + 12)) #draws images onto game window

font = pygame.font.Font(None, 60)
text2 = font.render(f"It's a draw!", True, (255, 255, 255))
text3 = font.render(f'Restart', True, (255, 255, 255))
text3_rect = text3.get_rect(center=(300, 350))

def show_winner_screen(text):
    overlay = pygame.Surface((600, 600), pygame.SRCALPHA) # Create a transparent overlay
    overlay.fill((128, 128, 128, 25))  # Dark overlay

    text_rect = text.get_rect(center=(300, 300))

    screen.blit(overlay, (0, 0))  # Draw overlay on top of everything
    screen.blit(text, text_rect)  # Draw winner text
    screen.blit(text3, text3_rect)
    pygame.display.update()  # Update the display

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if event.type == pygame.MOUSEBUTTONDOWN and game.winner is None and not game.draw: #checks for mouse click, and that there isn't a winner
        x, y = pygame.mouse.get_pos() #x, y coordinate of mouse click
        row, col = y // 200, x // 200 #finds which square was clicked
        if game.board[row][col] is None:
            game.makeMove(row, col) #runs makeMove function from TicTacToe class
            if game.turn == 'X':
                imageLoader(col, row, oImage)
            elif game.turn == 'O':
                imageLoader(col, row, xImage)
    if game.winner is not None:
        text1 = font.render(f"{game.winner} Wins!", True, (255, 255, 255))
        pygame.draw.line(screen, (128, 128, 128), game.winLineStart, game.winLineEnd, 7) #draws line through winning three letters
        show_winner_screen(text1)
        if event.type == pygame.MOUSEBUTTONUP:
            if text3_rect.collidepoint(event.pos):
                reset_game()
    if game.draw is True:
        show_winner_screen(text2)
        if event.type == pygame.MOUSEBUTTONUP:
            if text3_rect.collidepoint(event.pos):
                reset_game()


    pygame.display.update()

pygame.quit() #closes window
