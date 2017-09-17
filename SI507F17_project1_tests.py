# Do not change import statements.
# Write your unit tests to test the cards code here.
import unittest
from SI507F17_project1_cards import *
from helper_functions import *


class Testproject1(unittest.TestCase):

    def setUp(self):
        self.card0 = Card(1, 11)  # Bug case
        self.deck0 = Deck()
        self.war_game = play_war_game(True)

    def tearDown(self):
        self.card0 = None
        self.deck0 = None
        self.war_game = None

# test Deck below ----------------------------------------#  

    def test_suit_names(self):  # Show if input is correct
        self.assertEqual(self.card0.suit_names, [
                         "Diamonds", "Clubs", "Hearts", "Spades"])

    def test_rank_levels(self):  # Checnk if "rank_levels" includes right info
        self.assertEqual(self.card0.rank_levels, [
                         1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])

    def test_faces(self):  # Check if "faces" includes right info
        self.assertEqual(self.card0.faces, {
                         1: "Ace", 11: "Jack", 12: "Queen", 13: "King"})

    def test_Card_str(self):
        self.assertEqual(self.card0.__str__(), "Jack of Clubs")

    def test_str1(self):  # Check if a deck includes 52 different cards
        a = self.deck0.__str__().split("\n")
        b = []  # from 32 lines of text
        for i in range(0, len(self.card0.suit_names)):
            for j in range(1, len(self.card0.rank_levels)+1):
                if j in self.card0.faces:
                    number = self.card0.faces[j]
                else:
                    number = j
                suit = self.card0.suit_names[i]
                result0 = "{} of {}".format(number, suit)
                b.append(result0)
        self.assertEqual(a, b)
        # b should be satisfied the list in the description

# test Card below ----------------------------------------#          

    def test_self_cards(self):
        # Test the type of element of "cards"
        self.assertIsInstance(self.deck0.cards[0], Card)

    def test_pop_card(self):  # check if "pop_card" works
        for _ in range(0, 52):
            self.deck0.pop_card()
        # After 52 times pop, "cards" list should be empty
        self.assertEqual(len(self.deck0.cards), 0)

    def test_shuffle(self):
        cards_string0 = [str(card) for card in self.deck0.cards]
        # print (self.deck0.cards[0].__str__())
        self.deck0.shuffle()
        cards_string1 = [str(card) for card in self.deck0.cards]
        self.assertEqual(cards_string1, cards_string0)

    def test_replace_card(self):  # check if "replace_card" works
        for _ in range(0, 52):
            self.deck0.pop_card()

        card0 = Card(1, 2)
        card1 = Card(1, 3)
        self.deck0.replace_card(card0)
        self.assertEqual(str(self.deck0.cards[0]), "2 of Clubs")
        self.assertEqual(len(self.deck0.cards), 1)

        self.deck0.replace_card(card0)
        self.assertEqual(len(self.deck0.cards), 1)
        self.deck0.replace_card(card1)
        self.assertEqual(len(self.deck0.cards), 2)
        self.assertEqual(str(self.deck0.cards[1]), "3 of Clubs")

    def test_sort_cards(self):
        for _ in range(13):
            self.deck0.pop_card()

        card_string0 = str(self.deck0).split('\n')
        self.deck0.shuffle()
        self.deck0.sort_cards()
        card_string1 = str(self.deck0).split('\n')
        self.assertEqual(card_string0, card_string1)

    def test_deal_hand(self):
        for _ in range(3):
            self.deck0.pop_card()
        self.deck0.deal_hand(27)

# test play_war_game below ----------------------------------------#        

    def test_play_war_game(self):
        self.assertIsInstance(self.war_game, tuple)  # check the type of output
        for _ in range(0, 50):  # check 50 times if results are right
            if int(self.war_game[2]) > int(self.war_game[1]):
                self.assertEqual(self.war_game[0], "Player2")
            elif int(self.war_game[2]) < int(self.war_game[1]):
                self.assertEqual(self.war_game[0], "Player1")
            else:
                self.assertEqual(self.war_game[0], "Tie")

# test show_song below ----------------------------------------#

    def test_show_song(self):
        song = show_song()
        self.assertIsInstance(song, Song)
        song2 = show_song("Bowie")
        self.assertTrue("Bowie" in str(song2))

if __name__ == '__main__':
    unittest.main(verbosity=2)
# You should test to ensure that
# everything explained in the code description file works as that file says.
# If you have correctly written the tests, at least 3 tests should fail.
# If more than 3 tests fail, it should be because multiple of
# the test methods address the same problem in the code.
# You may write as many TestSuite subclasses as you like, but you
# should try to make these tests well-organized and easy to read the output.
# You should invoke the tests with verbosity=2 (make sure you invoke them!)

###########
