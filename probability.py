import math


# # the probability of drawing an Ace with the help of Python
# # Sample Space
# cards = 52

# # Outcomes
# aces = 4

# # Divide possible outcomes by the sample set
# ace_probability = aces / cards

# # Print probability rounded to two decimal places
# print(round(ace_probability, 2))
# =====================================================================================

# # Create function that returns probability percent rounded to one decimal place
def event_probability(event_outcomes, sample_space):
    probability = (event_outcomes / sample_space) * 100
    return round(probability, 1)

# # Sample Space
# cards = 52

# # Determine the probability of drawing a heart
# hearts = 13
# heart_probability = event_probability(hearts, cards)

# # Determine the probability of drawing a face card
# face_cards = 12
# face_card_probability = event_probability(face_cards, cards)

# # Determine the probability of drawing the queen of hearts
# queen_of_hearts = 1
# queen_of_hearts_probability = event_probability(queen_of_hearts, cards)

# # Print each probability
# print(str(heart_probability) + '%')
# print(str(face_card_probability) + '%')
# print(str(queen_of_hearts_probability) + '%')
# =====================================================================================

# # Permutations Code
# n = 4
# k = 2

# # Determine permutations and print result
# Permutations = math.factorial(n) / math.factorial(k)
# print(Permutations)
# ====================================================================================

# # Combinations Code
# n = 52
# k = 2

# # Determine Permutations
# Permutations = math.factorial(n) / math.factorial(n - k)

# # Determine Combinations and print result
# Combinations = Permutations / math.factorial(k)
# print(Combinations)
# ===================================================================================


# # Sample Space
# cards = 52
# cards_drawn = 1 
# cards = cards - cards_drawn 

# # Determine the probability of drawing an Ace after drawing a King on the first draw
# aces = 4
# ace_probability1 = event_probability(aces, cards)

# # Determine the probability of drawing an Ace after drawing an Ace on the first draw
# aces_drawn = 1
# aces = aces - aces_drawn
# ace_probability2 = event_probability(aces, cards)

# # Print each probability
# print(ace_probability1)
# print(ace_probability2)
# ====================================================================================

# # Sample Space
# cards = 52
# hole_cards = 2
# turn_community_cards = 4
# cards = cards - (hole_cards + turn_community_cards)

# # Outcomes
# diamonds = 13
# diamonds_drawn = 4
# # In poker, cards that complete a draw are known as "outs"
# outs = diamonds - diamonds_drawn

# #Determine river flush probability
# probability = event_probability(outs, cards)
# print(probability)
# ================================================================================

# # Sample Space
# cards = 52

# # Calculate the probability of drawing a heart or a club
# hearts = 13
# clubs = 13
# heart_or_club = event_probability(hearts, cards) + event_probability(clubs, cards)

# # Calculate the probability of drawing an ace, king, or a queen
# aces = 4
# kings = 4
# queens = 4
# ace_king_or_queen = event_probability(aces, cards) + event_probability(kings, cards) + event_probability(queens, cards)

# print(heart_or_club)
# print(ace_king_or_queen)
# ===============================================================================

# Sample Space
cards = 52

# Calculate the probability of drawing a heart or an ace
hearts = 13
aces = 4
ace_of_hearts = 1
heart_or_ace = event_probability(hearts, cards) + event_probability(aces, cards) - event_probability(ace_of_hearts, cards)

# Calculate the probability of drawing a red card or a face card
red_cards = 26
face_cards = 12
red_face_cards = 6
red_or_face_cards = event_probability(red_cards, cards) + event_probability(face_cards, cards) - event_probability(red_face_cards, cards)

print(round(heart_or_ace, 1))
print(round(red_or_face_cards, 1))