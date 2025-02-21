import time

from deck import Deck
from player import Player
from dealer import Dealer

def play_hand(player, dealer, bet, deck):
    # take away money from bet
    player.money -= bet
    bust = 0

    # Initial deal
    player.hit(deck)
    dealer.hit(deck)
    player.hit(deck)
    dealer.hit(deck)

    print("Dealer's up card:")
    dealer.show_up_card()
    print("-------")
    print("Player's hand:")
    player.show_hand()
    print("-------")

    # Check for blackjack
    if player.score == 21 and dealer.score != 21:
        print("Blackjack! Player wins!")
        player.money += 1.5 * bet + bet
        time.sleep(2)
        return

    if dealer.score == 21 and player.score != 21:
        print("Blackjack! Dealer wins!")
        dealer.show_hand()
        time.sleep(2)
        return
    
    # Player's turn
    while player.score < 21:
        print("-------")
        action = input("Would you like to hit or stand? (h/s): ")
        if action == "h":
            player.hit(deck)
            player.show_hand()
            player.show_score()

        if player.score > 21:
            print("Bust! Dealer wins!")
            bust = 1
            break
        if action == "s":
            break
        if player.score == 21:
            break
    time.sleep(2)
    print("-----------------------------------")

    # Dealer's turn
    print("Dealer's hand:")
    dealer.show_hand()
    dealer.show_score()

    # wait for 3 seconds
    time.sleep(2)

    while dealer.score < 17:
        print("-------")
        dealer.hit(deck)
        dealer.show_hand()
        dealer.show_score()
        time.sleep(2)

    if dealer.score > 21 and not bust:
        print("Dealer busts! Player wins!")
        player.money += bet * 2
        return
    
    if dealer.score > player.score or bust:
        print("Dealer wins!")
        return
    elif dealer.score < player.score and not bust:
        print("Player wins!")
        player.money += bet * 2
        return
    else:
        print("Push! It's a tie!")
        player.money += bet
        return

# Define main function
def main():
    deck_penetration = 52
    start_money = 750


    deck = Deck(num_decks=6)
    deck.shuffle()

    dealer = Dealer()
    player = Player(bal=start_money)

    while player.money > 0 and deck.count() > deck_penetration:
        print("-----------------------------")
        print("Player's money:", player.money)
        bet = float(input("Enter bet amount: "))
        if (bet == 0 or bet > player.money):
            break
        print("-----------------------------")
        play_hand(player, dealer, bet, deck)
        dealer.reset()
        player.reset()
        print("-----------------------------")

    print("\n\n-----------------------------------")
    print("Game over!")
    print("Player's money:", player.money)
    print("Thanks for playing!\n\n")
main()
    