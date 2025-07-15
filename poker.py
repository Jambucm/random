import numpy as np

np.random.seed(369)

cards = [i for i in range(1,14,1)]
court = ['K', 'Q', 'J']
suits = ['H', 'S', 'C', 'D']

cards = [str(num) for num in cards]

full_deck = []
for card in cards:
    for suit in suits:
        card_suit = card+suit
        full_deck.append(card_suit)

print(f'Full deck card count: {len(full_deck)}')

nr_players = 3

players_hands = {}
updated_deck = full_deck.copy()

for i in range(1, nr_players+1, 1):
    cards = np.random.choice(full_deck, 2)
    players_hands[i] = cards.tolist()
    for card in cards:
        updated_deck.remove(card)

print(f'Player(s) hands: {players_hands}')
print(f'Deck current card count: {len(updated_deck)}')

table = []
flop = np.random.choice(updated_deck, 3)
for card in flop.tolist():
    updated_deck.remove(card)
    table.append(card)

print(f'Flop: {flop}')
print(f'Deck current card count: {len(updated_deck)}')

turn = np.random.choice(updated_deck, 1)
for card in turn.tolist():
    updated_deck.remove(card)
    table.append(card)

print(f'Turn: {turn}')
print(f'Deck current card count: {len(updated_deck)}')

river = np.random.choice(updated_deck, 1)
for card in river.tolist():
    updated_deck.remove(card)
    table.append(card)

print(f'River: {river}')
print(f'Deck current card count: {len(updated_deck)}')

print(f'Table cards: {table}')

player_hands_table = players_hands.copy()
for cards in player_hands_table.values():
    for card in table:
        cards.append(card)

print(f'Player(s) hand(s) with table: \n{player_hands_table}')

player_nums = player_hands_table.copy()
for player, hand in player_nums.items():
    player_nums[player] = [int(card[:-1]) for card in hand]

print(f'Player(s) nums: {player_nums}')

player_suits = player_hands_table.copy()
for player, hand in player_suits.items():
    player_suits[player] = [card[-1] for card in hand]

print(f'Player(s) suits: {player_suits}')



