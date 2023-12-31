# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/00_cards.ipynb.

# %% auto 0
__all__ = ['suits', 'rank', 'Card']

# %% ../nbs/00_cards.ipynb 2
from fastcore.utils import *

# %% ../nbs/00_cards.ipynb 4
suits = ["Clubs", "Diamonds", "Spades", "Hearts"]
rank = [None, "A"] + [str(x) for x in range(2,11)] + ["J", "Q", "K"]

# %% ../nbs/00_cards.ipynb 8
class Card:
    "A playing card"
    def __init__(self, 
                 suit:int, # An index into `suits` 
                 rank:int): # An index into `ranks`
        self.suit, self.rank = suit, rank

    def __str__(self):
        return f"{rank[self.rank]}{suits[self.suit]}"

    __repr__ = __str__

# %% ../nbs/00_cards.ipynb 12
@patch
def __eq__(self:Card,a:Card):  # When used within the defining class, the class name must be in quotes.
        return (self.suit, self.rank) == (a.suit, a.rank)

# %% ../nbs/00_cards.ipynb 13
@patch
def __lt__(self:Card, a:Card): 
    return (self.suit, self.rank) < (a.suit, a.rank)

# %% ../nbs/00_cards.ipynb 15
@patch
def __gt__(self:Card, a:Card):
    return (self.suit, self.rank) > (a.suit, a.rank)
