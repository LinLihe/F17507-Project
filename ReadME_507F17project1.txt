ReadME_507F17project1

This python program is used for testing the "SI507F17_project1_cards" python program works like what the description says. In this program, I only use the package "Unittest".

* For class Card
	* Use the first three methods to test if all inputs are correct.
	* Test the __str__ of class card by the instance "self.card0" which is created in "setUp".
	* Create a deck which is same as the deck in description, then use it to compare with the deck made by original program, see if they are same.

* For class Deck
	* Test the type of information included in "cards" list.
	* Test the "pop_card", see if it can be used 52 times.
	* Test "shuffle": create a cope of list "cards" as cards_string0, then shuffle the list "cards" and copy it as cards_string1. See if cards_string0 is same as cards_string1.
	* Test "replace_card" in 2 situations: 1. Whether the replace_card can add a card to the deck If the deck does not have this card; 2. If the deck has the same card I want to add.
	* Test "sort_cards", see if it works for a complete deck and an incomplete deck, such as lacking of one suit)
	* Test "deal_hand", see if it works for any hand size.

* For play_war_game
	* see if the game result is right

* For show_song:
	* Check the type of show_song()
	* Given a key word, check if it is in the output string.