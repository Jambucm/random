import numpy as np
from collections import Counter

np.random.seed(369)

#Defining cards numbers, courts (as 11, 12, 13) and suits
cards = [i for i in range(1,14,1)]
suits = ['H', 'S', 'C', 'D']

#Updating cards to string format
cards = [str(num) for num in cards]

#Concatenating numbers/courts and suits
full_deck = []
for card in cards:
    for suit in suits:
        card_suit = card+suit
        full_deck.append(card_suit)

#Defining number of players
nr_players = 2

players_hands = {}
updated_deck = full_deck.copy()

for i in range(1, nr_players+1, 1):
    cards = np.random.choice(updated_deck, 2, replace=False)
    players_hands[i] = cards.tolist()
    for card in cards:
        updated_deck.remove(card)

print(f'Deck current card count: {len(updated_deck)}')

table = []
flop = np.random.choice(updated_deck, 3, replace=False)
for card in flop.tolist():
    updated_deck.remove(card)
    table.append(card)

print(f'Deck current card count: {len(updated_deck)}')

turn = np.random.choice(updated_deck, 1, replace=False)
for card in turn.tolist():
    updated_deck.remove(card)
    table.append(card)

print(f'Deck current card count: {len(updated_deck)}')

river = np.random.choice(updated_deck, 1, replace=False)
for card in river.tolist():
    updated_deck.remove(card)
    table.append(card)

print(f'Deck current card count: {len(updated_deck)}')

player_hands_table = players_hands.copy()
for cards in player_hands_table.values():
    for card in table:
        cards.append(card)

player_nums = player_hands_table.copy()
for player, hand in player_nums.items():
    player_nums[player] = [int(card[:-1]) for card in hand]

player_suits = player_hands_table.copy()
for player, hand in player_suits.items():
    player_suits[player] = [card[-1] for card in hand]

def numbers(hand, sort=False):
    hand = [int(card[:-1]) for card in hand]
    if sort:
        hand.sort()
    return hand

def suits(hand, sort=False):
    hand = [card[-1] for card in hand]
    if sort:
        hand.sort()
    return hand

def is_sequence(hand:list):
    #PRECISA CHECAR PARA SEQUENCIA REAL COM ÁS
    
    num_hand = numbers(hand, sort=True)

    sequence_hand = []
    for i in range(len(num_hand) - 4):
        floor = num_hand[i]
        seq_hand = num_hand[i:i+5]
        sequence = [j for j in range(floor, floor + 5, 1)]
        if seq_hand == sequence:
            sequence_hand.clear()            
            for num in sequence:
                sequence_hand.append(num)

    if sequence_hand:
        return sequence_hand
    
def is_repeated(hand:list):

    counts = Counter(hand)




def sanity_check():
    print(f'Full deck card count: {len(full_deck)}')
    print(f'Player(s) hands: {players_hands}')
    print(f'Flop: {flop}')
    print(f'Turn: {turn}')
    print(f'River: {river}')
    print(f'Table cards: {table}')
    print(f'Player(s) hand(s) with table: \n{player_hands_table}')
    print(f'Player(s) nums: {player_nums}')
    print(f'Player(s) suits: {player_suits}')
    print(is_sequence(player_hands_table[2]))

sanity_check()