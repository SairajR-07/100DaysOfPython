import random

def deal_card():
    # Cards are now integers instead of strings
    cards = [2, 6, 10, 4, 9, 7, 8, 10, 3, 11, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    # If the player has a blackjack (21 with two cards), return 0 for a blackjack
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    # If the player has an ace (11) and the score is over 21, convert the ace to a 1
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(u_score, c_score):
    if u_score == c_score:
        return 'Draw'
    elif c_score == 0:
        return 'Lose, opponent has Blackjack!'
    elif u_score == 0:
        return 'Win with a Blackjack!'
    elif u_score > 21:
        return 'You went over. You lose!'
    elif c_score > 21:
        return 'Opponent went over. You win!'
    elif u_score > c_score:
        return 'You win!'
    else:
        return 'You lose!'

user_cards = []
comp_cards = []
is_game_over = False

# Deal two cards to both the user and the computer at the start
for _ in range(2):
    user_cards.append(deal_card())
    comp_cards.append(deal_card())

while not is_game_over:
    user_score = calculate_score(user_cards)
    comp_score = calculate_score(comp_cards)
    print(f"Your cards: {user_cards}, current score: {user_score}")
    print(f"Computer's first card: {comp_cards[0]}")

    if user_score == 0 or comp_score == 0 or user_score > 21:
        is_game_over = True
    else:
        user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
        if user_should_deal.lower() == 'y':
            user_cards.append(deal_card())
        else:
            is_game_over = True

# Once the user is done, it's the computer's turn to draw cards
while comp_score != 0 and comp_score < 17:
    comp_cards.append(deal_card())
    comp_score = calculate_score(comp_cards)

print(f"Your final hand: {user_cards}, final score: {user_score}")
print(f"Computer's final hand: {comp_cards}, final score: {comp_score}")
print(compare(user_score, comp_score))
