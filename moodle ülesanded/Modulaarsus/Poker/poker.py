"""Simple Poker implementation."""


class Card:
    """A card in a poker game."""

    def __init__(self, value, suit):
        """Initialze Card."""
        self.value = value
        self.suit = suit

    def __repr__(self):
        """
        Return a string representation of the card.

        "{value} of {suit}"
        "2 of hearts" or "Q of spades"
        """
        return f"{self.value} of {self.suit}"


class Hand:
    """The hand in a poker game."""

    suits = ["diamonds", "clubs", "hearts", "spades"]
    values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

    def __init__(self):
        """Initialize Hand."""
        self.cards = []
        self.card_dict = {}
        self.type = ""

    def can_add_card(self, card: Card) -> bool:
        """
        Check for card validity.

        Can only add card if:
        - A card with the same suit and value is already not being held.
        - The player is holding less than five cards
        - The card has both a valid value and a valid suite.
        """
        print(card.__repr__())
        print(card in self.cards)
        if card.value in self.values and card.suit in self.suits:
            if card not in self.cards and len(self.cards) < 5:
                return True
        return False

    def add_card(self, card: Card):
        """
        Add a card to hand.

        Before adding a card, you would have to check if it can be added.
        """
        if self.can_add_card(card):
            self.cards.append(card)
            cards_with_value = self.card_dict.get(card.value, [])
            cards_with_value.append(card)
            self.card_dict[card.value] = cards_with_value

    def can_remove_card(self, card: Card):
        """
        Check if a card can be removed from hand.

        The only consideration should be that the card is already being held.
        """
        return card in self.cards

    def remove_card(self, card: Card):
        """
        Remove a card from hand.

        Before removing the card, you would have to check if it can be removed.
        """
        if self.can_remove_card(card):
            self.cards.remove(card)
            cards_with_value = self.card_dict.get(card.value)
            cards_with_value.remove(card)
            self.card_dict[card.value] = cards_with_value

    def get_cards(self):
        """Return a list of cards as objects."""
        return self.cards

    def is_straight(self):
        """
        Determine if the hand is a straight.

        A straight hand will have all cards in the order of value.
        Sorting will help you here as the order will vary.

        Examples:
        4 5 6 7 8
        K J 10 Q A

        For the sake of simplicity - A 2 3 4 5 will not be tested.
        You can always consider A to be the highest ranked card.
        """
        values = []
        for card in self.cards:
            index = 0
            for v in self.values:
                if v == card.value:
                    break
                else:
                    index += 1
            values.append(index)

        values = sorted(values, key=int)

        if values[0] + 4 == values[-1]:
            return True
        return False

    def is_flush(self):
        """
        Determine if the hand is a flush.

        In a flush hand all cards are the same suit. Their number value is not important here.
        """
        first_suit = self.cards[0].suit
        for card in self.cards:
            if card.suit != first_suit:
                return False
        return True

    def is_straight_flush(self):
        """
        Determine if the hand is a straight flush.

        Such a hand is both straight and flush at the same time.

        """
        flush = self.is_flush()
        straight = self.is_straight()
        return flush, straight

    def is_full_house(self):
        """
        Determine if the hand is a full house.

        A house will have three cards of one value, and two cards of a second value.
        For example:
        2 2 2 6 6
        K J K J K
        """
        values_list = []
        for card in self.cards:
            values_list.append(card.value)
        values_list = sorted(values_list)
        count_a = values_list.count(values_list[0])
        count_b = values_list.count(values_list[-1])
        if count_a == 1 or count_b == 1:
            return False
        elif count_a + count_b == 5:
            return True
        return False

    def is_four_of_a_kind(self):
        """
        Determine if there are four cards of the same value in hand.

        For example:
        2 2 K 2 2
        9 4 4 4 4

        """
        values = []
        for card in self.cards:
            values.append(card.value)

        values = sorted(values)
        if values.count(values[0]) == 4 or values.count(values[-1]) == 4:
            return True
        return False

    def is_three_of_a_kind(self):
        """
        Determine if there are three cards of the same value in hand.

        For Example:
        Q 4 Q Q 7
        5 5 1 5 2

        """
        values = []
        for card in self.cards:
            values.append(card.value)
        values = sorted(values)
        if values.count(values[0]) == 3 or values.count(values[-1]) == 3:
            return True
        return False

    def is_pair(self):
        """
        Determine if there are two kinds of the same value in hand.

        For example:
        5 A 2 K A
        8 7 6 6 5

        """
        values = []
        for card in self.cards:
            values.append(card.value)
        values = sorted(values)
        if values.count(values[0]) == 2 or values.count(values[-1]) == 2:
            return True
        return False

    def get_hand_type(self):
        """
        Return a string representation of the hand.

        Return None (or nothing), if there are less than five cards in hand.

        "straight flush" - Both a straight and a flush
        "flush" - The cards are all of the same suit
        "straight" - The cards can be ordered
        "full house" - Three cards are of the same value while the other two also share a value.
        "four of a kind" - Four cards are of the same value
        "three of a kind" - Three cards are of the same value
        "pair" - Two cards are of the same value
        "high card" - None of the above

        """
        if len(self.cards) > 5 or len(self.cards) < 5:
            return None

        flush, straight = self.is_straight_flush()
        if flush and straight:
            self.type = "straight flush"
            return self.type
        elif flush:
            self.type = "flush"
            return self.type
        elif straight:
            self.type = "straight"
            return self.type
        elif self.is_full_house():
            self.type = "full house"
            return self.type
        elif self.is_four_of_a_kind():
            self.type = "four of a kind"
            return self.type
        elif self.is_three_of_a_kind():
            self.type = "three of a kind"
            return self.type
        elif self.is_pair():
            self.type = "pair"
            return self.type
        else:
            self.type = "high card"
            return self.type

    def __repr__(self):
        """
        Return a string representation of the hand.

        I got a {type} with cards: {card list}
        I got a straight with cards: 2 of diamonds, 4 of spades, 5 of clubs, 3 of diamonds, 6 of hearts

        If a hand type cannot be yet determined, return a list of cards as so:

        I'm holding {cards}
        I'm holding 2 of diamonds, 4 of spades.

        Order of the cards is not important.
        """
        self.get_hand_type()
        cards_text = ""
        for card in self.cards:
            cards_text += card.value + " of " + card.suit + ", "
        cards_text = cards_text[:-2]
        if len(self.cards) == 5:
            return f"I got a {self.type} with cards: {cards_text}."
        else:
            return f"I'm holding {cards_text}."


if __name__ == "__main__":
    hand = Hand()
    cards = [Card("2", "diamonds"), Card("4", "spades"), Card("5", "clubs"), Card("3", "diamonds"), Card("6", "hearts")]
    [hand.add_card(card) for card in cards]
    assert hand.get_hand_type() == "straight"
    print(hand.__repr__())

    hand = Hand()
    cards = [Card("10", "diamonds"), Card("2", "diamonds"), Card("A", "diamonds"), Card("6", "diamonds"),
             Card("9", "diamonds")]
    [hand.add_card(card) for card in cards]
    assert hand.get_hand_type() == "flush"

    hand = Hand()
    cards = [Card("A", "hearts"), Card("A", "clubs"), Card("A", "spades"), Card("A", "diamonds"),
             Card("9", "diamonds")]
    [hand.add_card(card) for card in cards]
    assert hand.get_hand_type() == "four of a kind"
