
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