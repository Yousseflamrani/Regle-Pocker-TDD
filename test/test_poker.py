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


def test_compare_higher_pair_wins():

    """
    testet deux paire

    """

    from src.pocker import compare_hand

    hand1 = "JH JC 4S 4H AD"
    hand2 = "JS JD 4C 4D 10S"

    result = compare_hand(hand1, hand2)

    assert result == 1, "la caret 9 devrait battre la carte 8"


def test_compare_Brelan():

    from src.pocker import compare_hand
    hand3 = "9H 9D 9S 5C 3H"
    hand4 = "8H 8D 8S AC 10H"

    result = compare_hand(hand3, hand4)
    assert result == 1, "Le Brelan de 9 doit battre le Brelan de 8"

def test_compare_straight():

    from src.pocker import compare_hand
    hand5= "5H 6C 7D 8S 9H"
    hand6= "4H 5C 6D 7S 8H"
    result = compare_hand(hand5, hand6)
    assert result == 1, "La Quinte hauteur 9 doit battre la Quinte hauteur 8"

def test_compare_straight_with_ace():
    from src.pocker import compare_hand


    hand7 = "2H 3C 4D 5S AH"

    hand8 = "5H 6C 7D 8S 9H"

    result = compare_hand(hand7, hand8)

    assert result == -1, "La Quinte hauteur 9 doit battre la Quinte basse A-2-3-4-5"


def test_compare_flush():

    from src.pocker import compare_hand
    hand9= "2H 5H 7H 9H AH"
    hand10= "4S 8S QS 10S KS"
    result = compare_hand(hand9, hand10)
    assert result ==1

def test_compare_flush_vs_straight():

    from src.pocker import compare_hand
    flush= "2H 5H 7H 9H KH"
    straight= "2C 3D 4H 5D 6S"

    result = compare_hand(flush, straight)

    assert result ==1, "Une Couleur doit battre une Quinte."

def test_compare_full_house():
    from src.pocker import compare_hand


    hand1 = "10H 10D 10S 4C 4H"

    hand2 = "9H 9D 9S AC AS"

    result = compare_hand(hand1, hand2)

    assert result == 1, "Le Full House aux 10 doit battre le Full House aux 9"

def test_compare_full_house_vs_flush():
    from src.pocker import compare_hand

    full_house = "10H 10D 10S 4C 4H"

    flush = "2H 5H 7H 9H KH"

    result = compare_hand(full_house, flush)

    assert result == 1, "Un Full House doit battre une Couleur"
