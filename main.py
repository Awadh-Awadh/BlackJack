import random

def deal_card():
  """
return a random item in the cards list
"""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  return random.choice(cards)

user_card = []
computer_card = []
for _ in range(2):
  user_card.append(deal_card())
  computer_card.append(deal_card())


def calculate_score(score):
    return sum(score)

