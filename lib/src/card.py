class Card:
    def __init__(self, rank, suit, value, image):
        self.rank = rank
        self.suit = suit
        self.value = value
        self.image = image
    
    # to string method
    def __str__(self):
        return f"{self.rank} of {self.suit}"
    
    def get_image(self):
        return self.image