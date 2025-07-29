import numpy as np
from collections import Counter

np.random.seed(369)

#Defining cards numbers, courts (as 11, 12, 13) and suits
cards = [i for i in range(1,14,1)]
suits_names = ['H', 'S', 'C', 'D']

#Updating cards to string format
cards = [str(num) for num in cards]

#hand list for testing
high_card_hand = ['2H', '5D', '9S', '11C', '13H', '3S', '7C']
pair_hand = ['10H', '10D', '4S', '6C', '13S', '2D', '8C']
two_pair_hand = ['5H', '5S', '3D', '3C', '12H', '6D', '10S']
three_of_a_kind_hand = ['7H', '7D', '7S', '2C', '9H', '5S', '12D']
straight_hand = ['4H', '5D', '6S', '7C', '8H', '1S', '10C']
straight_hand_one = ['4H', '5D', '1S', '10C', '11H', '12S', '13C']
flush_hand = ['2C', '5C', '8C', '11C', '13C', '4H', '7D']
full_house_hand = ['6H', '6D', '6S', '3C', '3D', '8H', '12C']
four_of_a_kind_hand = ['9H', '9D', '9S', '9C', '2H', '6C', '13S']
straight_flush_hand = ['5S', '6S', '7S', '8S', '9S', '2C', '11D']
royal_flush_hand = ['10H', '11H', '12H', '13H', '1H', '4D', '7S']

#Concatenating numbers/courts and suits
full_deck = []
for card in cards:
    for suit in suits_names:
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
for card in list(flop):
    updated_deck.remove(card)
    table.append(card)

print(f'Deck current card count: {len(updated_deck)}') #deck cards count for sanity check

#picks flop cards (1 random card) without replacement, updates deck and table.
turn = np.random.choice(updated_deck, 1, replace=False)
for card in list(turn):
    updated_deck.remove(card)
    table.append(card)

print(f'Deck current card count: {len(updated_deck)}') #deck cards count for sanity check

#picks flop cards (1 random card) without replacement, updates deck and table.
river = np.random.choice(updated_deck, 1, replace=False)
for card in list(river):
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
print(f'Numbers test: {numbers(high_card_hand)}') #sanity check


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
print(f'Suits test: {suits(high_card_hand)}') #sanity check

def straight(hand:list):
    '''
    Checks if there is a card sequence in the players hand (2 picked cards + table) and returns the highest sequence.

    Args:
    hand - hand list

    Returns:
    Highest player hand
    '''

    num_hand = numbers(hand, sort=True) #turns player hand into numbers

    straight_hand = [] #initializes sequence hand empty list
    for i in range(len(num_hand) - 4): #loops through all cards from 1st to 3rd (only possible 5 cards sequences in a 7 card hand)
        floor = num_hand[i] #selects lowest card for loop sequence
        sequence_hand = num_hand[i:i+5] #filters lists 5 card sequence from floor card
        sequence = [j for j in range(floor, floor + 5, 1)] #creates sequence from floor card to 4 following cards to compare
        if sequence_hand == sequence: #compare hand sequence and expected sequence for loop
            straight_hand = sequence_hand.copy() #replaces sequence hand

    royal_hand = [10,11,12,13,1] #sets royal sequence (from 10 to Ace)
    seq_real = num_hand[-4:] + [num_hand[0]] #concatenates last 4 cards and first card (ace)
    if royal_hand == seq_real: #compares as before
        straight_hand = royal_hand.copy() #replaces sequence hand

    if straight_hand:
        return straight_hand #returns highest sequence or None

print('Straight test:')
print(straight(straight_hand_one))
print(straight(straight_hand))
print(straight(flush_hand))
print(straight(['1A', '2A', '3A', '4A', '5A', '6A', '7A']))

def flush(hand:list):

    suits_hand = suits(hand)
    counts = Counter(suits_hand)

    for suit, count in counts.items():
        if count >= 5:
            return suit

print('Flush test:')
print(flush(straight_hand_one))
print(flush(flush_hand))
print(flush_hand)


def sanity_check():
    print(f'Full deck card count: {len(full_deck)}')
    print(f'Player(s) hands: {players_hands}')
    print(f'Flop: {flop}')
    print(f'Turn: {turn}')
    print(f'River: {river}')
    print(f'Table cards: {table}')
    print(f'Player(s) hand(s) with table: \n{player_hands_table}')
    print(f'Player(s) nums: {player_hands_table[0]}')
    print(f'Player(s) suits: {player_hands_table[0]}')
    print(straight(player_hands_table[0]))

#sanity_check()
