import numpy as np

from card import Card


# IMAGE LISTS
SPADES = ["placeholder", "lib/assets/cards/ace_of_spades.png", "lib/assets/cards/2_of_spades.png", "lib/assets/cards/3_of_spades.png", "lib/assets/cards/4_of_spades.png", "lib/assets/cards/5_of_spades.png", "lib/assets/cards/6_of_spades.png", "lib/assets/cards/7_of_spades.png", "lib/assets/cards/8_of_spades.png", "lib/assets/cards/9_of_spades.png", "lib/assets/cards/10_of_spades.png", "lib/assets/cards/jack_of_spades.png", "lib/assets/cards/queen_of_spades.png", "lib/assets/cards/king_of_spades.png"]
HEARTS = ["placaeholder", "lib/assets/cards/ace_of_hearts.png", "lib/assets/cards/2_of_hearts.png", "lib/assets/cards/3_of_hearts.png", "lib/assets/cards/4_of_hearts.png", "lib/assets/cards/5_of_hearts.png", "lib/assets/cards/6_of_hearts.png", "lib/assets/cards/7_of_hearts.png", "lib/assets/cards/8_of_hearts.png", "lib/assets/cards/9_of_hearts.png", "lib/assets/cards/10_of_hearts.png", "lib/assets/cards/jack_of_hearts.png", "lib/assets/cards/queen_of_hearts.png", "lib/assets/cards/king_of_hearts.png"]
DIAMONDS = ["placeholder", "lib/assets/cards/ace_of_diamonds.png", "lib/assets/cards/2_of_diamonds.png", "lib/assets/cards/3_of_diamonds.png", "lib/assets/cards/4_of_diamonds.png", "lib/assets/cards/5_of_diamonds.png", "lib/assets/cards/6_of_diamonds.png", "lib/assets/cards/7_of_diamonds.png", "lib/assets/cards/8_of_diamonds.png", "lib/assets/cards/9_of_diamonds.png", "lib/assets/cards/10_of_diamonds.png", "lib/assets/cards/jack_of_diamonds.png", "lib/assets/cards/queen_of_diamonds.png", "lib/assets/cards/king_of_diamonds.png"]
CLUBS = ["placeholder", "lib/assets/cards/ace_of_clubs.png", "lib/assets/cards/2_of_clubs.png", "lib/assets/cards/3_of_clubs.png", "lib/assets/cards/4_of_clubs.png", "lib/assets/cards/5_of_clubs.png", "lib/assets/cards/6_of_clubs.png", "lib/assets/cards/7_of_clubs.png", "lib/assets/cards/8_of_clubs.png", "lib/assets/cards/9_of_clubs.png", "lib/assets/cards/10_of_clubs.png", "lib/assets/cards/jack_of_clubs.png", "lib/assets/cards/queen_of_clubs.png", "lib/assets/cards/king_of_clubs.png"]

# Define a deck of cards
class Deck:
    def __init__(self, num_decks=1):
        self.cards = []
        self.build(num_decks)

    def build(self, num_decks=1):
        for _ in range(num_decks):
            for s in ["Spades", "Clubs", "Diamonds", "Hearts"]:
                if s == "Spades":
                    image_list = SPADES
                elif s == "Clubs":
                    image_list = CLUBS
                elif s == "Diamonds":
                    image_list = DIAMONDS
                elif s == "Hearts":
                    image_list = HEARTS
                for r in range(1, 14):
                    if r == 1:
                        rank = "Ace"
                        value = 11 # or 1
                        image = image_list[r]
                    elif r == 11:
                        rank = "Jack"
                        value = 10
                        image = image_list[r]
                    elif r == 12:
                        rank = "Queen"
                        value = 10
                        image = image_list[r]
                    elif r == 13:
                        rank = "King"
                        value = 10
                        image = image_list[r]
                    else:
                        rank = str(r)
                        value = r
                        image = image_list[r]
                    self.cards.append(Card(rank, s, value, image))

    def shuffle(self):
        np.random.shuffle(self.cards)

    def draw(self):
        return self.cards.pop()
    
    def count(self):
        return len(self.cards)
    
    def show(self):
        for card in self.cards:
            print(card)


# # test deck
# if __name__ == "__main__":
#     deck = Deck(num_decks=1)
#     deck.shuffle()
#     print(f"Deck contains {deck.count()} cards.")
#     deck.show()
    
#     # Draw a card
#     drawn_card = deck.draw()
#     print(f"Drawn card: {drawn_card}")
#     print(f"Deck now contains {deck.count()} cards.")
    
#     # Show the remaining cards
#     for card in deck.cards:
#         print(card, card.get_image())
