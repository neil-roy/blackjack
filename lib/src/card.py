class Card:
    def __init__(self, rank, suit, value):
        self.rank = rank
        self.suit = suit
        self.value = value
    
    # to string method
    def __str__(self):
        return f"{self.rank} of {self.suit}"