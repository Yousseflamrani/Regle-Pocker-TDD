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
    global is_straight
    ranks_map = {
        '2': 2, '3': 3, '4': 4, '5': 5, '6': 6,
        '7': 7, '8': 8, '9': 9, '10': 10,
        'J': 11, 'Q': 12, 'K': 13, 'A': 14
    }

    cards_str = hand_str.split()
    numeric_ranks = [ranks_map[c[:-1]] for c in cards_str]
    numeric_ranks.sort(reverse=True)
    suits = [c[-1] for c in cards_str]

    from collections import Counter
    rank_counts = Counter(numeric_ranks)
    sorted_by_count_then_value = sorted(
        rank_counts.items(),
        key=lambda x: (x[1], x[0]),
        reverse=True
    )

    pattern = sorted([count for (_, count) in rank_counts.items()], reverse=True)

    is_straight = len(set(numeric_ranks)) == 5 and (max(numeric_ranks) - min(numeric_ranks) == 4)
    is_flush= len(set(suits)) == 1

    if set(numeric_ranks)== {14, 2, 3, 4, 5}: # Vérification de la Quinte
        is_straight = True
        numeric_ranks = [5, 4, 3, 2, 1]


    if is_flush and is_straight and max(numeric_ranks) == 14:    # Quinte Flush Royale
        return (9, [14])


    if is_flush and is_straight:  #Quinte Flush (Straight + Flush)
        return (8, [max(numeric_ranks)])

    if is_flush:# Flush (Couleur)
        return (5, numeric_ranks)

    if is_straight:
        return(4,[max(numeric_ranks)])


    if pattern == [4,1]: # Carré (Four of a Kind)
        four_of_a_kind = sorted_by_count_then_value[0][0]
        kicker = sorted_by_count_then_value[1][0]
        return (7, [four_of_a_kind, kicker])


    if pattern == [3,2]:    # Full House (Brelan + Paire)
        three_of_a_kind = sorted_by_count_then_value[0][0]
        pair_value = sorted_by_count_then_value[1][0]
        return (6, [three_of_a_kind, pair_value])


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



def get_hand_from_input(prompt):
    """
    Demande à l'utilisateur d'entrer une main de poker au format correct.
    """
    while True:
        hand = input(prompt).strip().upper()
        cards = hand.split()

        if len(cards) != 5:
            print("Erreur : Une main doit contenir exactement 5 cartes.")
            continue

        valid_ranks = {'2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'}
        valid_suits = {'H', 'D', 'S', 'C'}

        valid = True
        for card in cards:
            rank, suit = card[:-1], card[-1]
            if rank not in valid_ranks or suit not in valid_suits:
                print(f"Erreur : {card} n'est pas une carte valide.")
                valid = False
                break

        if valid:
            return hand

if __name__ == "__main__":
    print("=== Comparateur de Mains de Poker ===")

    hand1 = get_hand_from_input("Entrez la première main (ex: '10H 9H 8H 7H 6H') : ")
    hand2 = get_hand_from_input("Entrez la deuxième main (ex: 'AH KH QH JH 10H') : ")

    result = compare_hand(hand1, hand2)

    if result == 1:
        print(f"La main 1 ({hand1}) est gagnante.")
    elif result == -1:
        print(f"La main 2 ({hand2}) est gagnante.")
    else:
        print("Égalité parfaite !")



