def test_compare_one_pair_vs_high_card()

    """"
    Compare two pairs of cards
    """

    from src.pocker import compare_hands

    hand_with_pair = "8H 8D 2S 5C 9H"
    hand_high_card = "AH 3C 7D 5S 2C"

    result = compare_hands(hand_with_pair, hand_high_card)

    assert result == 1, "la carte avec la paire devrait ganger"