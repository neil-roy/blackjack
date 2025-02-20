import numpy as np
import time
# Define a data structure for cards
class Card:
    def __init__(self, rank, suit, value):
        self.rank = rank
        self.suit = suit
        self.value = value
    
    # to string method
    def __str__(self):
        return f"{self.rank} of {self.suit}"


# Define a deck of cards
class Deck:
    def __init__(self, num_decks=1):
        self.cards = []
        self.build(num_decks)

    def build(self, num_decks=1):
        for _ in range(num_decks):
            for s in ["Spades", "Clubs", "Diamonds", "Hearts"]:
                for r in range(1, 14):
                    if r == 1:
                        rank = "Ace"
                        value = 11
                    elif r == 11:
                        rank = "Jack"
                        value = 10
                    elif r == 12:
                        rank = "Queen"
                        value = 10
                    elif r == 13:
                        rank = "King"
                        value = 10
                    else:
                        rank = str(r)
                        value = r
                    self.cards.append(Card(rank, s, value))

    def shuffle(self):
        np.random.shuffle(self.cards)

    def draw(self):
        return self.cards.pop()
    
    def count(self):
        return len(self.cards)
    
    def show(self):
        for card in self.cards:
            print(card)
    

# Define Dealer class
class Dealer:
    def __init__(self):
        self.hand = []
        self.score = 0
    
    def hit(self, deck):
        card = deck.draw()
        self.hand.append(card)
        self.score += card.value
        return card
    
    def show_hand(self):
        for card in self.hand:
            print(card)
    
    def show_score(self):
        print("Score:", self.score)

    def show_up_card(self):
        print(self.hand[0])
    
    def reset(self):
        self.hand = []
        self.score = 0

# Define Player Class
class Player:
    def __init__(self, bal=500):
        self.hand = []
        self.score = 0
        self.money = bal
    
    def hit(self, deck):
        card = deck.draw()
        self.hand.append(card)
        self.score += card.value
        return card
    
    def show_hand(self):
        for card in self.hand:
            print(card)
    
    def show_score(self):
        print("Score:", self.score)
    
    def reset(self):
        self.hand = []
        self.score = 0

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
    