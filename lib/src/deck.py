import numpy as np

from card import Card

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
                        value = 11 # or 1
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