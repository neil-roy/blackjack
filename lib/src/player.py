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