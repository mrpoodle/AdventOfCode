### for day 07

def read_input(input_file):
    lines = [line.strip("\n").split(" ") for line in open(input_file)]

    return lines

def get_hand_value_noJ(hand):
    """returns the value of a hand"""
    # 5	of	a	Kind
    if len(set(hand)) == 1:
        value='G'
    # four of a kind
    elif len(set(hand)) == 2:
        if hand.count(hand[0]) == 4 or hand.count(hand[0]) == 1:
            value='F'
        # full house
        else:
            value='E'
    # 3 of a kind
    elif len(set(hand)) == 3:
        if hand.count(hand[0]) == 3 or hand.count(hand[1]) == 3 or hand.count(hand[2]) == 3:
            value='D'
        # 2 pairs
        else:
            value='C'
    # 1 pair
    elif len(set(hand)) == 4:
        value='B'
    # high card
    else:
        value='A'

    # values for cards in order: A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, 2
    card_values = {
        '2': 'a',
        '3': 'b',
        '4': 'c',
        '5': 'd',
        '6': 'e',
        '7': 'f',
        '8': 'g',
        '9': 'h',
        'T': 'i',
        'J': 'j',
        'Q': 'k',
        'K': 'l',
        'A': 'm'
    }
    for card in hand:
        value += card_values[card]

    return value

def get_hand_value_J(hand):
    """returns the value of a hand"""
    # 5	of	a	Kind
    if len(set(hand)) == 1 or (len(set(hand)) == 2 and "J" in hand):
        value='G'
    # four of a kind
    elif len(set(hand)) == 2 or (len(set(hand)) == 3 and "J" in hand):
        sub_set = list(set(filter(lambda a: a != "J", hand)))
        jokers = hand.count("J")

        if hand.count(sub_set[0])+jokers == 4 or hand.count(sub_set[1])+jokers == 4:
            value='F'
        # full house
        else:
            value='E'
    # 3 of a kind
    elif len(set(hand)) == 3 or (len(set(hand)) == 4 and "J" in hand):
        sub_set = list(set(filter(lambda a: a != "J", hand)))
        jokers = hand.count("J")

        if hand.count(sub_set[0])+jokers == 3 or hand.count(sub_set[1])+jokers == 3 or hand.count(sub_set[2])+jokers == 3:
            value='D'
        # 2 pairs
        else:
            value='C'
    # 1 pair
    elif len(set(hand)) == 4 or (len(set(hand)) == 5 and "J" in hand):
        value='B'
    # high card
    else:
        value='A'

    # values for cards in order: A, K, Q, T, 9, 8, 7, 6, 5, 4, 3, 2, J
    card_values = {
        '2': 'b',
        '3': 'c',
        '4': 'd',
        '5': 'e',
        '6': 'f',
        '7': 'g',
        '8': 'h',
        '9': 'i',
        'T': 'j',
        'J': 'a',
        'Q': 'k',
        'K': 'l',
        'A': 'm'
    }
    for card in hand:
        value += card_values[card]
    return value

def solve(input_file, function):
    lines = sorted(read_input(input_file), key=lambda x: function(x[0]))

    out = 0
    multiplyer = 1
    for line in lines:
        #print(multiplyer, "*", int(line[1]))
        out += multiplyer * int(line[1])
        multiplyer += 1
    return out

def part_1(input_file):
    return solve(input_file, get_hand_value_noJ)

def part_2(input_file):
    return solve(input_file, get_hand_value_J)
