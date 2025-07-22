import numpy as np
from collections import Counter

np.random.seed(369)

#Defining cards numbers, courts (as 11, 12, 13) and suits
cards = [i for i in range(1,14,1)]
suits = ['H', 'S', 'C', 'D']

#Updating cards to string format
cards = [str(num) for num in cards]

#hand list for testing
hand = ['1H','5D','7S','10C','11H','12D','13S']

#Concatenating numbers/courts and suits
full_deck = []
for card in cards:
    for suit in suits:
        card_suit = card+suit
        full_deck.append(card_suit)

#Defining number of players
nr_players = 2

#Generating players hands dictionary and updated_deck (this one will be updated as game flows)
players_hands = {}
updated_deck = full_deck.copy()

#Picking random cards for each player
for i in range(1, nr_players+1, 1):                             #iterates over amount of players 1 by 1
    cards = np.random.choice(updated_deck, 2, replace=False)    #picks 2 cards randomly from the updated deck without replacement
    players_hands[i] = cards.tolist()                           #updates dictionary with player hand
    for card in cards:                                          #iterates over selected cards
        updated_deck.remove(card)                               #updates deck by removing picked cards

print(f'Deck current card count: {len(updated_deck)}') #deck cards count for sanity check

#Initializing table list
table = [] 

#picks flop cards (3 random cards) without replacement, updates deck and table.
flop = np.random.choice(updated_deck, 3, replace=False)
for card in flop.tolist():
    updated_deck.remove(card)
    table.append(card)

print(f'Deck current card count: {len(updated_deck)}') #deck cards count for sanity check

#picks flop cards (1 random card) without replacement, updates deck and table.
turn = np.random.choice(updated_deck, 1, replace=False)
for card in turn.tolist():
    updated_deck.remove(card)
    table.append(card)

print(f'Deck current card count: {len(updated_deck)}') #deck cards count for sanity check

#picks flop cards (1 random card) without replacement, updates deck and table.
river = np.random.choice(updated_deck, 1, replace=False)
for card in river.tolist():
    updated_deck.remove(card)
    table.append(card)

print(f'Deck current card count: {len(updated_deck)}') #deck cards count for sanity check

#Initializes new dictionary to include table cards in player's hands 
player_hands_table = players_hands.copy()
for cards in player_hands_table.values():   #iterates over player's hands (lists)
    for card in table:                      #iterates over table cards
        cards.append(card)                  #adds table cards to hands

#Creating function to keep only numbers from hands
def numbers(hand:list, sort:bool=False):
    '''
    Extracts numbers from hand and returns clean list with only numbers either sorted or not

    Args:
    hand - hand list
    sort - whether to sort hand or not

    Returns:
    Updated clean list
    '''

    hand = [int(card[:-1]) for card in hand] #selects all characters except last (numbers) from each string (card) in hand
    if sort:
        hand.sort() #sorts if chosen
    return hand
print(f'Numbers test: {numbers(hand)}') #sanity check


def suits(hand:list, sort=False):
    '''
    Extracts suits from hand and returns clean list with only suits either sorted or not

    Args:
    hand - hand list
    sort - whether to sort hand or not

    Returns:
    Updated clean list
    '''

    hand = [card[-1] for card in hand] #selects last character (suit) from each string (card) in hand
    if sort:
        hand.sort() #sorts if chosen
    return hand
print(f'Suits test: {suits(hand)}') #sanity check

def is_sequence(hand:list):

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

    real_hand = [10,11,12,13,1]
    seq_real = num_hand[-4:] + [num_hand[0]]
    if real_hand == seq_real:
        sequence_hand = real_hand.copy()

    if sequence_hand:
        return sequence_hand

print('Teste real:')
print(is_sequence(hand))
    
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
