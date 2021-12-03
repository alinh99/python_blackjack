############### Blackjack Project #####################
import random
from art import logo
from replit import clear
#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

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
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: 
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []

#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.

