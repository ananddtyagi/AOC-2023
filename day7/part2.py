from collections import defaultdict
import functools


with open("data.txt") as data:
    
    lines = data.readlines()
    
    hand_to_bet = {}
    hands = []
    def value(card):
        if card.isdigit():
            return int(card)
        if card == "T": return 10
        if card == "J": return 1
        if card == "Q": return 12
        if card == "K": return 13
        if card == "A": return 14
        
    def get_hand_type(hand):
        max_count_card = 0
        max_card = hand[0]
        cards = defaultdict(lambda: 0)
        num_j = 0
        for card in hand:
            if card == "J": 
                num_j +=1
                continue
            cards[card] += 1
            if max_count_card < cards[card]:
                max_count_card = cards[card]
                max_card = card

        cards[max_card] += num_j
        max_count_card += num_j
        if len(cards) == 5:
            return "high_card"
        elif len(cards) == 4:
            return "one_pair"
        elif len(cards) == 3:
            if max_count_card == 3:
                return "three_of_a_kind"
            else:
                return "two_pair"
        elif len(cards) == 2:
            if max_count_card == 3:
                return "full_house"
            else:
                return "four_of_a_kind"
        else:
            return "five_of_a_kind"
    
    hand_type_values = {
     "high_card": 1,
     "one_pair": 2,
     "two_pair": 3,
     "three_of_a_kind": 4,
     "full_house": 5,
     "four_of_a_kind": 6,
     "five_of_a_kind": 7
    }
    
    def compare_hand_types(hand1_type, hand2_type):
        return hand_type_values[hand2_type] - hand_type_values[hand1_type]
    
    def compare_hands(hand1, hand2):
        hand1_type = get_hand_type(hand1)
        hand2_type = get_hand_type(hand2)
        
        if hand1_type != hand2_type:
            return compare_hand_types(hand1_type, hand2_type)
        
        for i in range(5):
            if hand1[i] == hand2[i]:
                continue
            if value(hand1[i]) > value(hand2[i]):
                return -1
            else:
                return 1
        return 0
        
    for line in lines:
        hand, bet = line.split()
        hand_to_bet[hand] = int(bet)
        hands.append(hand)
        
    hands.sort(key=functools.cmp_to_key(compare_hands), reverse=True)

    total = 0 
    for rank, hand in enumerate(hands, 1):
        total+=rank*hand_to_bet[hand]
    print(total)