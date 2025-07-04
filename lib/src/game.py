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
state = "start"
bet_amount = 0
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
    display_cards(card_list)
    pygame.display.update()
    pygame.time.delay(500) # PLACE HOLDER UNTIL ANIMATION
    card_list.append((dealer.hit(deck), "dealer", 1))
    display_cards(card_list)
    pygame.display.update()
    pygame.time.delay(500)
    card_list.append((player.hit(deck), "player", 2))
    display_cards(card_list)
    pygame.display.update()
    pygame.time.delay(500)
    card_list.append((dealer.hit(deck), "dealer", 2))
    display_cards(card_list)
    pygame.display.update()
    pygame.time.delay(500)

def display_cards(card_list):
    for card, owner, position in card_list:
        # Load the card image
        card_image = pygame.image.load(card.get_image())
        card_image = pygame.transform.scale(card_image, (100, 150))
        # Calculate the position to draw the card
        if owner == "player":
            x = 100 + (position - 1) * 50
            y = 400
        elif owner == "dealer":
            x = 100 + (position - 1) * 50
            y = 50
        # Draw the card on the screen
        SCREEN.blit(card_image, (x, y))

def dealer_turn():
    # Dealer's turn logic
    # print("Dealer's turn...")
    while dealer.score < 17:
        card = dealer.hit(deck)
        card_list.append((card, "dealer", len([c for c, o, p in card_list if o == "dealer"]) + 1))
        display_cards(card_list)
        pygame.display.update()
        pygame.time.delay(700)
        # print(f"Dealer hits: {card}")
        if dealer.score > 21:
            display_cards(card_list)
            pygame.display.update()
            pygame.time.delay(700)
            break
    # print(f"Dealer's final score: {dealer.score}")


# game loop
while run:
    # DEBUG WHERE MOUSE IS
    # mouse_x, mouse_y = pygame.mouse.get_pos()
    # print(f"Mouse Position: ({mouse_x}, {mouse_y})")

    # add the background image
    SCREEN.blit(BACKGROUND, (0, 0))

    # draw the player balance in the top right
    font = pygame.font.Font(None, 36)
    balance_text = font.render(f'Balance: ${player.money}', True, (255, 255, 255))
    SCREEN.blit(balance_text, (SCREEN_WIDTH - balance_text.get_width() - 10, 10))

    # draw the deal button:
    if state == "start":
        # reset max bet
        if bet_amount > player.money:
            bet_amount = player.money
        pygame.draw.rect(SCREEN, (0, 255, 0), (350, 250, 100, 50))
        font = pygame.font.Font(None, 36)
        text = font.render('Deal', True, (255, 255, 255))
        SCREEN.blit(text, (375, 265))
        # draw the bet amount adjuster
        font = pygame.font.Font(None, 36)
        bet_text = font.render(f'Bet: ${bet_amount}', True, (255, 255, 255))
        SCREEN.blit(bet_text, (SCREEN_WIDTH // 2 - bet_text.get_width() // 2, 200))
        # draw the bet amount increase and decrease buttons
        pygame.draw.rect(SCREEN, (0, 0, 255), (300, 200, 50, 30))
        text = font.render('+', True, (255, 255, 255))
        SCREEN.blit(text, (320, 205))
        pygame.draw.rect(SCREEN, (255, 0, 0), (450, 200, 50, 30))
        text = font.render('-', True, (255, 255, 255))
        SCREEN.blit(text, (470, 205))


        
    
    if state == "player_turn":
        # draw the hit and stand buttons
        pygame.draw.rect(SCREEN, (0, 0, 255), (350, 250, 100, 50))
        font = pygame.font.Font(None, 36)
        text = font.render('Hit', True, (255, 255, 255))
        SCREEN.blit(text, (375, 265))
        pygame.draw.rect(SCREEN, (255, 0, 0), (350, 320, 100, 50))
        text = font.render('Stand', True, (255, 255, 255))
        SCREEN.blit(text, (365, 335))
        font = pygame.font.Font(None, 36)
        bet_text = font.render(f'Bet: ${bet_amount}', True, (255, 255, 255))
        SCREEN.blit(bet_text, (SCREEN_WIDTH // 2 - bet_text.get_width() // 2, 200))

        # Display cards
        display_cards(card_list)
    
    if state == "dealer_turn":
        font = pygame.font.Font(None, 36)
        bet_text = font.render(f'Bet: ${bet_amount}', True, (255, 255, 255))
        SCREEN.blit(bet_text, (SCREEN_WIDTH // 2 - bet_text.get_width() // 2, 200))
        dealer_turn()
        # Display cards after dealer's turn
        display_cards(card_list)
        pygame.display.update()
        pygame.time.delay(1000)
        state = "end"
    
    if state == "end":
        # Display final results
        SCREEN.fill((0, 0, 0))
        font = pygame.font.Font(None, 36)
        if player.score > 21:
            text = font.render('Player Busts! Dealer Wins!', True, (255, 0, 0))
        elif dealer.score > 21 or player.score > dealer.score:
            text = font.render('Player Wins!', True, (0, 255, 0))
            player.money += bet_amount * 2  # Player wins the bet amount back plus the bet
        elif player.score < dealer.score:
            text = font.render('Dealer Wins!', True, (255, 0, 0))
        else:
            text = font.render('Push!', True, (255, 255, 0))
            player.money += bet_amount  # Player gets the bet amount back
        SCREEN.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, SCREEN_HEIGHT // 2 - text.get_height() // 2))
        pygame.display.update()
        pygame.time.delay(2000)
        # reset the game
        card_list.clear()
        player.reset()
        dealer.reset()
        state = "start"



    # event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and state == "start":
            mouse_x, mouse_y = event.pos
            if 350 <= mouse_x <= 450 and 250 <= mouse_y <= 300:
                # start the game
                state = "player_turn"
                # update player balance
                player.money -= bet_amount
                # print("Deal button clicked. Starting the game...")
                initial_deal()
            elif 300 <= mouse_x <= 350 and 200 <= mouse_y <= 230:
                # print("TEST 2")
                if bet_amount < player.money:
                    bet_amount += 10
                    # print("TEST")
            elif 450 <= mouse_x <= 500 and 200 <= mouse_y <= 230:
                if bet_amount > 0:
                    bet_amount -= 10
        elif event.type == pygame.MOUSEBUTTONDOWN and state == "player_turn":
            mouse_x, mouse_y = event.pos
            if 350 <= mouse_x <= 450 and 250 <= mouse_y <= 300:
                card_list.append((player.hit(deck), "player", len([c for c, o, p in card_list if o == "player"]) + 1))
                if player.score >= 21:
                    state = "dealer_turn"
            elif 350 <= mouse_x <= 450 and 320 <= mouse_y <= 370:
                state = "dealer_turn"
    


    
    # update the display
    pygame.display.flip()



pygame.quit()