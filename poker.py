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
    If sequence exists - highest sequence
    If sequence does not exist - None
    '''

    num_hand = numbers(hand, sort=True) #turns player hand into numbers
    num_hand.sort()

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
    '''
    Checks if there are 5 cards with equal suits (flush) in the players hand (2 picked cards + table) and returns the flush's suit.

    Args:
    hand - hand list

    Returns:
    If is flush - flush's suit
    If is not flush - None
    '''

    suits_hand = suits(hand) #extracts suits from hand
    counts = Counter(suits_hand) #dictionary for suits counts

    for suit, count in counts.items(): #loops through dicts items (keys and values)
        if count >= 5: 
            flush_cards = [card for card in hand if card[-1] == suit]
            return flush_cards

print('Flush test:')
print(flush(straight_hand_one))
print(flush(flush_hand))

def muliple(hand:list, n_equal:int):
    '''
    Checks if there are 2 equal cards.

    Args:
    hand - hand list

    Returns:
    If pair - pair card
    If not - None
    '''

    num_hand = numbers(hand) #extracts cards from hand
    counts = Counter(num_hand) #dictionary for cards counts

    high = 0

    for card, count in counts.items(): #loops through dicts items (keys and values)
        if count >= n_equal and card > high:
            high = card

    if high > 0:
        return [high] * n_equal
            
print('Multiple test:')
print(muliple(straight_hand_one, 2))
print(muliple(pair_hand, 2))
print(muliple(pair_hand, 3))
print(muliple(three_of_a_kind_hand, 3))
print(muliple(four_of_a_kind_hand, 4))

def full_house(hand:list):
    '''
    Checks if there is a combination of 3 and 2 equal cards.

    Args:
    hand - hand list

    Returns:
    If is full house - full house hand (5 cards)
    If is not full house - None
    '''

    num_hand = numbers(hand) #extracts cards from hand
    counts = Counter(num_hand) #dictionary for cards counts
    card_2 = []
    card_3 = []
    full_house_cards = []

    for card, count in counts.items(): #loops through dicts items (keys and values)
        if count >= 2:
            card_2.append(card)
        if count == 3:
            card_3.append(card)

    high_3 = 0
    for card in card_3:
        if card > high_3:
            high_3 = card

    high_2 = 0
    for card in card_2:
        if card > high_2 and card != high_3:
            high_2 = card

    if high_2 == 0 or high_3 == 0:
        return None
    else:
        for i in range(3):
            full_house_cards.append(high_3)
        for i in range(2):
            full_house_cards.append(high_2)
        return full_house_cards
    
print('Full house test:')
print(full_house(full_house_hand))
print(full_house(pair_hand))
print(full_house(three_of_a_kind_hand))
print(full_house(['2A', '2A', '2A', '5A', '5A', '5A', '10A']))


def high_card(hand:list):
    '''
    Finds highest card in hand.

    Args:
    hand - hand list

    Returns:
    Highest card
    '''

    num_hand = numbers(hand) #extracts cards from hand
    high = 0 #initializes high card

    for card in num_hand:
        if card > high:
            high = card #updates high card for each loop, if card is higher than previous

    return [high]

print('High card test:')
print(high_card(high_card_hand))
print(high_card(pair_hand))
print(high_card(three_of_a_kind_hand))

def two_pair(hand:list):

    num_hand = numbers(hand) #extracts cards from hand
    counts = Counter(num_hand) #dictionary for cards counts

    high_1 = 0
    high_2 = 0

    two_pair_cards = []

    for card, count in counts.items():
        if count >= 2:
            if card > high_1:
                high_2 = high_1
                high_1 = card
            elif card > high_2:
                high_2 = card

    if high_1 == 0 or high_2 == 0:
        return None
    else:
        for i in range(2):
            two_pair_cards.append(high_1)
        for i in range(2):
            two_pair_cards.append(high_2)
        return two_pair_cards

print('Two pair test:')
print(two_pair(two_pair_hand))
print(two_pair(pair_hand))
print(two_pair(three_of_a_kind_hand))
print(two_pair(['2A','2A','2A','3A','3A','7A','7A']))

def straight_flush(hand:list):

    flush_cards = flush(hand)
    new_hand = hand.copy()
    
    if flush_cards:
        flush_suit = flush_cards[0][-1]
    else:
        return None

    for card in hand:
        if card[-1] != flush_suit:
            new_hand.remove(card)

    if new_hand:
        straight_new_hand = straight(new_hand)
        if straight_new_hand:
            return new_hand
        
print('Straight flush test:')
print(straight_flush(straight_flush_hand))
print(straight_flush(straight_hand))
print(straight_flush(flush_hand))
        
def royal_flush(hand:list):

    straight_cards = straight_flush(hand)

    if straight_cards:
        if 1 in numbers(straight_cards):
            return straight_cards

print('Royal flush test:')
print(royal_flush(royal_flush_hand))
print(royal_flush(straight_flush_hand))
print(royal_flush(straight_hand))
print(royal_flush(flush_hand))


def best_hand(hand:list):

    best = 1

    if muliple(hand, 2):
        best = 2
    if two_pair(hand):
        best = 3
    if muliple(hand, 3):
        best = 4
    if straight(hand):
        best = 5
    if flush(hand):
        best = 6
    if full_house(hand):
        best = 7
    if muliple(hand, 4):
        best = 8
    if straight_flush(hand):
        best = 9
    if royal_flush(hand):
        best = 10

    return best

print('Best hand test:')
print(best_hand(high_card_hand))
print(best_hand(pair_hand))
print(best_hand(two_pair_hand))
print(best_hand(three_of_a_kind_hand))
print(best_hand(straight_hand))
print(best_hand(flush_hand))
print(best_hand(full_house_hand))
print(best_hand(four_of_a_kind_hand))
print(best_hand(straight_flush_hand))
print(best_hand(royal_flush_hand))







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
