############### Blackjack Project #####################
import random
from art import logo
from replit import clear
############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:

def blackjack():
  print(logo)
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  def deal_card():
    """Return a random card"""
    return random.choice(cards)

  # Deal the user and computer 2 cards each using deal_card() and append().
  user_cards = []
  computer_cards = []
  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

  def calculate_score(card):
    """Return score of cards"""
    score = sum(card)
    # check blackjack
    if 11 in card:
      if 10 in card:
        if score == 21:
          score = 0
    # if blackjack --> change into 1 point
    if score > 21 and 11 in card:
      card.remove(11)
      card.append(1)
      score = sum(card)
    return score

  user_scores = calculate_score(user_cards)
  computer_scores = calculate_score(computer_cards)
  print(f"\tYour cards: {user_cards}, current score: {user_scores}")
  print(f"\tComputer first card: {computer_cards[0]}")
  should_continue = True
  while should_continue:
    # if user_scores is blackjact(0) or computer_scores is blackjack(0) or user_scores > 21 --> the game is ended.
    if user_scores == 0 or computer_scores == 0 or user_scores > 21:   
      should_continue = False
      # computer play
      if user_scores > 21 and computer_scores < 17:
        computer_cards.append(deal_card())
        computer_scores = calculate_score(computer_cards)
      print(f"\tYour cards: {user_cards}, current score: {user_scores}")
      print(f"\tComputer final hand: {computer_cards}, current score: {computer_scores}")
    # the game is not ended --> ask users to draw another card.     
    else:
      draw_another_cards = input("Type 'y' to get another cards, 'n' to pass: ")
      # 'y' to draw another card
      if draw_another_cards == 'y':
        user_cards.append(deal_card())
        user_scores = calculate_score(user_cards)
        print(f"\tYour cards: {user_cards}, current score: {user_scores}")
        # computer play
        if computer_scores < 17:
          computer_cards.append(deal_card())
          computer_scores = calculate_score(computer_cards)
        print(f"\tComputer's first card: {computer_cards[0]}")
      # 'n' to pass another card and print out the result
      else:
        should_continue = False
        print(f"\tYour cards: {user_cards}, current score: {user_scores}")
        # computer play
        if computer_scores < 17:
          computer_cards.append(deal_card())
          computer_scores = calculate_score(computer_cards)
        print(f"\tComputer final hand: {computer_cards}, current score: {computer_scores}")
  
  def compare(user_score, computer_score):
    """Return the result win or draw of the user and the computer"""
    if user_score == computer_score:
      return "Draw."
    elif computer_score == 0:
      return "Computer win."
    elif user_score == 0:
      return "You win."
    elif user_score > 21:
      return "Computer win."
    elif computer_score > 21:
      return "You win."
    else:
      if user_score > computer_score:
        return "You win."
      else:
        return "Computer win"
  print(compare(user_scores, computer_scores))
# Ask users if they want to restart the game
restart = True
while restart:
  if input("Do you want to play a game of blackjack? Type 'y' or 'n': ") == 'y':
    clear()
    blackjack()
  else:
    restart = False
