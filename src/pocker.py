from collections import Counter

def compare_hand(hand1_str, hand2_str):
    hand1_score = get_score(hand1_str)
    hand2_score = get_score(hand2_str)

    if hand1_score > hand2_score:
        return 1
    elif hand1_score < hand2_score:
        return -1
    else:
        return 0

def get_score(hand_str):
    ranks_map = {
        '2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
        '7': 7, '8': 8, '9': 9, '10': 10,
        'J': 11, 'Q': 12, 'K': 13, 'A': 14
    }

    cards_str = hand_str.split()
    numeric_ranks = [ranks_map[c[:-1]] for c in cards_str]
    numeric_ranks.sort(reverse=True)

    rank_counts = Counter(numeric_ranks)
    sorted_by_count_then_value = sorted(
        rank_counts.items(),
        key=lambda x: (x[1], x[0]),
        reverse=True
    )

    pattern = sorted([count for (_, count) in rank_counts.items()], reverse=True)

    if pattern == [3,1,1]: #Brelan
        brelan = sorted_by_count_then_value[0][0]
        kickers = [sorted_by_count_then_value [1][0], sorted_by_count_then_value [2][0]]
        return(3, [brelan]+ kickers)

    if pattern == [2,2,1]:  # detection de deux paires
        pair1_value = sorted_by_count_then_value[0][0]
        pair2_value = sorted_by_count_then_value[1][0]
        kicker = sorted_by_count_then_value[2][0]  # La carte restante
        return (2, [pair1_value, pair2_value, kicker])

    if pattern == [2,1,1,1]:  # detection d'une seule paire
        pair_value = sorted_by_count_then_value[0][0]
        kickers = [x[0] for x in sorted_by_count_then_value[1:]]
        return (1, [pair_value] + kickers)

    return (0, numeric_ranks)  # Carte haute


def has_pair(hand_str):
    cards = hand_str.split()
    ranks = [c[:-1] for c in cards]
    return len(set(ranks)) < 5
