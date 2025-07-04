import pygame
from deck import Deck
from player import Player
from dealer import Dealer

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# background image
BACKGROUND = pygame.image.load('lib/assets/other/red_background.jpg')
BACKGROUND = BACKGROUND.convert() # faster rendering

run = True
idle = True
card_list = []  # List to hold card objects for display

# Initialize deck, player, dealer
deck = Deck(num_decks=6)
player = Player()
dealer = Dealer()
deck.shuffle()


# FUNCTIONS FOR GAME MECHANICS
def initial_deal():
    # clear the card_list (Assuming that a new hand is being dealt)
    card_list.clear()
    # append the cards to the card_list
    card_list.append((player.hit(deck), "player", 1))
    card_list.append((dealer.hit(deck), "dealer", 1))
    card_list.append((player.hit(deck), "player", 2))
    card_list.append((dealer.hit(deck), "dealer", 2))

def display_cards(card_list):
    for card, owner, position in card_list:
        # Load the card image
        card_image = pygame.image.load(card.get_image())
        card_image = pygame.transform.scale(card_image, (100, 150))
        # Calculate the position to draw the card
        if owner == "player":
            x = 100 + (position - 1) * 120
            y = 400
        elif owner == "dealer":
            x = 100 + (position - 1) * 120
            y = 50
        # Draw the card on the screen
        SCREEN.blit(card_image, (x, y))


# game loop
while run:

    # add the background image
    SCREEN.blit(BACKGROUND, (0, 0))

    # draw the deal button:
    if idle:
        pygame.draw.rect(SCREEN, (0, 255, 0), (350, 250, 100, 50))
        font = pygame.font.Font(None, 36)
        text = font.render('Deal', True, (255, 255, 255))
        SCREEN.blit(text, (375, 265))
    
    if not idle:
        # draw the hit and stand buttons
        pygame.draw.rect(SCREEN, (0, 0, 255), (350, 250, 100, 50))
        font = pygame.font.Font(None, 36)
        text = font.render('Hit', True, (255, 255, 255))
        SCREEN.blit(text, (375, 265))
        pygame.draw.rect(SCREEN, (255, 0, 0), (350, 320, 100, 50))
        text = font.render('Stand', True, (255, 255, 255))
        SCREEN.blit(text, (365, 335))

        # Display cards
        display_cards(card_list)


    # event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and idle:
            mouse_x, mouse_y = event.pos
            if 350 <= mouse_x <= 450 and 250 <= mouse_y <= 300:
                # start the game
                idle = False
                print("Deal button clicked. Starting the game...")
                initial_deal()
        elif event.type == pygame.MOUSEBUTTONDOWN and not idle:
            mouse_x, mouse_y = event.pos
            if 350 <= mouse_x <= 450 and 250 <= mouse_y <= 300:
                # player hits
                print("Hit button clicked. Player hits.")
                card_list.append((player.hit(deck), "player", len([c for c, o, p in card_list if o == "player"]) + 1))
            elif 350 <= mouse_x <= 450 and 320 <= mouse_y <= 370:
                # player stands
                print("Stand button clicked. Player stands.")
                idle = True
                # dealer's turn logic can be added here
    


    
    # update the display
    pygame.display.update()



pygame.quit()