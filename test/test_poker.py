def test_compare_one_pair_vs_high_card():

    """"
    Compare two pairs of cards
    """

    from src.pocker import compare_hand

    hand_with_pair = "8H 8D 2S 5C 9H"
    hand_high_card = "AH 3C 7D 5S 2C"

    result = compare_hand(hand_with_pair, hand_high_card)

    assert result == 1, "la carte avec la paire devrait ganger"


def test_compare_higher_pair_wins():

    """
    testet qu'une paire de 9 bat une paire de 8

    """

    from src.pocker import compare_hand

    pair_of_9 = "9H 9D 2S 5C 3H"
    pair_of_8 = "8H 8D 2S 5C 3H"

    result = compare_hand(pair_of_9, pair_of_8)

    assert result == 1, "la caret 9 devrait battre la carte 8"
