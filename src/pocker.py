def compare_hand(hand1_str, hand2_str):
    """
    Compare hand1 et hand2.
    - Retourne 1 si hand1 > hand2
    - Retourne -1 si hand2 > hand1
    - Retourne 0 si égalité
    """
    hand1_has_pair = has_pair(hand1_str)
    hand2_has_pair = has_pair(hand2_str)


    if hand1_has_pair and not hand2_has_pair:
        return 1


    if hand2_has_pair and not hand1_has_pair:
        return -1

    return 0


def has_pair(hand_str):
    """
    Détecte si la main contient au moins une paire.
    hand_str est une chaîne comme "8H 8D 2S 5C 9H".
    """
    cards = hand_str.split()

    
    ranks = []
    for card in cards:

        rank_str = card[:-1]
        ranks.append(rank_str)

    # Si la longueur de set(ranks) est < 5, ça veut dire qu'il y a un doublon
    return len(set(ranks)) < 5
