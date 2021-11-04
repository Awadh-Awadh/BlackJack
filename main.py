import random

def deal_card():
  """
return a random item in the cards list
"""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  return random.choice(cards)

user_card = []
computer_card = []
is_game_over = False
for _ in range(2):
  user_card.append(deal_card())
  computer_card.append(deal_card())


def calculate_score(score): 
    return sum(score)

def compare(user_score, computer_score):
    if computer_score == user_score:
        return "DRAW"
    elif computer_score == 0:
        return "YOU LOOSE. THE OPPONENT HAS A BLACKJACK"
    elif user_score == 0:
       return "You loose"
    elif user_score > 21:
      return "You loose. Score above 21"
    elif computer_score > 21:
        return "You win.Computer went above"
    elif user_score > computer_score:
        return "You win"
    else:
        return "You loose"




while not is_game_over:
  user_score = calculate_score(user_card)
  computer_score = calculate_score(computer_card)
  print(f"user chose {user_card} and score is {user_score}")
  print(f"computer chose {computer_card[0]}")

  if user_score == 0 or user_score>21 or computer_score == 0:
      is_game_over = True
  else:
      continue_play = input("Type y to contunue and n to stop: ")
      if continue_play == 'y':
          user_card.append(deal_card())
      else:
          is_game_over = True
while computer_score !=0 and computer_score<17:
    computer_card.append(deal_card())
    computer_score = calculate_score(computer_card)

print(f"Your final hand is: {user_card} and final score: {user_score}")
print(f"Computer's final hand is: {user_card} and final score: {computer_score}")


print(compare(user_score=user_score, computer_score=computer_score))