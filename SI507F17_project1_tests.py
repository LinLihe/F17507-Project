## Do not change import statements.
import unittest
from SI507F17_project1_cards import *

class Testproject1(unittest.TestCase):
	
	def setUp(self):
		self.card0 = Card(1,11)
		self.deck0 = Deck()


	def tearDown(self):
		self.card0 = None
		self.deck0 = None 

	def test_suit_names(self):
		self.assertEqual(self.card0.suit_names,["Diamonds","Clubs","Hearts","Spades"])
	# def test_rank_levels(self):
	# def test_faces(self):

	def test_Card_str(self):
		self.assertEqual(self.card0.__str__(), "Jack of Clubs")

	def test_Deck_str(self):
		a = list(set(map(str,self.deck0.__str__().split("\n"))))
		self.assertEqual(len(a), 52)

	def test_Deck_pop_card(self):
		self.assertEqual(self.deck0.pop_card().__str__(),"King of Spades")






if __name__ == '__main__':
	unittest.main()
## Write your unit tests to test the cards code here.
## You should test to ensure that everything explained in the code description file works as that file says.
## If you have correctly written the tests, at least 3 tests should fail. If more than 3 tests fail, it should be because multiple of the test methods address the same problem in the code.
## You may write as many TestSuite subclasses as you like, but you should try to make these tests well-organized and easy to read the output.
## You should invoke the tests with verbosity=2 (make sure you invoke them!)

###########