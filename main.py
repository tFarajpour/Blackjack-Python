"""This project defines a game of Blackjack as a class, then calls BlackJack's play() method.
Created by Tyler Farajpour.
"""
#TODO: Improve documentation.
import random


class BlackJack:
    """This class models a game of Blackjack.
    The game is designed to be played by calling self.play().
    No other method should be called directly.

    Cards are modeled simply by value: There is currently no
    recognition of suit or color, and no differentiation between face cards
    
    If the player and dealer both bust, the player still loses for busting first.
    """

    def __init__ (self):
        self.shoe = [
            11,11,11,11,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,
            6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,
            10,10,10,10,10,10,10,10,10,10,10,10,10,
            ]
        self.player_hand = []
        self.dealer_hand = []
        self.choice_to_hit_or_stand = '0'
        self.choice_to_hit_or_stand_is_valid = False
        self.game_outcome = "unfinished"

    def hit(self, hand_to_hit):
        """This method deals a card from the shoe to a deck and handles special Ace behavior."""
        #If hitting would draw an 11 that would cause a bust, then add as a 1 instead.
        if self.shoe[-1]==11 and sum(hand_to_hit)>=11:
            self.shoe.pop()
            hand_to_hit.append(1)
        else:
            hand_to_hit.append(self.shoe.pop())

        #If hand would bust after hitting and there's an 11 in it, replace the 11 with a 1.
        if sum(hand_to_hit)>21 and 11 in hand_to_hit:
            hand_to_hit[hand_to_hit.index(11)] = 1


    def check_if_bust(self, hand_to_check_for_bust):
        """This method takes a hand as an argument, determines who's hand it is, and checks whether it's greater than 21.
        If either hand busts, this function resolves to "True." Otherwise, this resolves to "False."
        """
        match hand_to_check_for_bust:
            case (self.player_hand):
                if sum(hand_to_check_for_bust) > 21:
                    return True
                else:
                    return False
            case (self.dealer_hand):
                if sum(hand_to_check_for_bust) > 21:
                    return True
                else:
                    return False


    def play(self):
        """Starts the game and controls the game's flow."""

        #shuffle the deck and deal cards
        random.shuffle(self.shoe)
        self.hit(self.dealer_hand)
        self.hit(self.player_hand)
        self.hit(self.dealer_hand)
        self.hit(self.player_hand)

        #Display Dealer first card
        print (f"Dealer's face-up card is {self.dealer_hand[0]}. The other card is face-down.")

        #prompt player to hit or stand. #TODO: Redesign this block to be more readable.
        while self.choice_to_hit_or_stand!='s' and sum(self.player_hand)<21:
            print(f"You have {len(self.player_hand)} cards:")
            for x in self.player_hand:
                print(x)
            print(f"Your hand total is {sum(self.player_hand)}.")
            self.choice_to_hit_or_stand = input("would you  like to '(h)it' or '(s)tand'?\n")
            while not self.choice_to_hit_or_stand_is_valid:
                if self.choice_to_hit_or_stand == 'h':
                    self.choice_to_hit_or_stand_is_valid = True
                    self.hit(self.player_hand)
                    print (f"You are dealt a {self.player_hand[-1]}.")
                elif self.choice_to_hit_or_stand == 's':
                    self.choice_to_hit_or_stand_is_valid = True
                else:
                    self.choice_to_hit_or_stand = input(
                        "Invalid input: Please type only 'h' to hit or 's' to stand.\n")
            self.choice_to_hit_or_stand_is_valid = False
        #TODO: handle natural blackjacks vs 21.

        #TODO: Report player hand total after they hit and bust, without showing redundantly if they don't bust.

        #if player busts, lose early.
        if self.check_if_bust(self.player_hand):
            print(f"You bust with a total of {sum(self.player_hand)}.")
            self.game_outcome = "Lost"
            return self.game_outcome

        #reveal dealer cards and total
        print("The dealer reveals their second card: \n"\
                  f"They have cards {self.dealer_hand[0]} and {self.dealer_hand[1]}. \n"\
                  f"Their total is {sum(self.dealer_hand)}."
                  )

        #Dealer hits until reaching at least 17. then check if they bust.
        while sum(self.dealer_hand) <= 16:
            self.hit(self.dealer_hand)
            print (f"Dealer hits and receives a {self.dealer_hand[-1]}.")

        #Win/lose conditions
        if self.check_if_bust(self.dealer_hand):
            print(f"The Dealer has busted with a total of {sum(self.dealer_hand)}.")
            self.game_outcome = "Won"

        elif sum(self.player_hand) == sum(self.dealer_hand):
            print ("The hands are equal.")
            self.game_outcome = "Pushed"

        elif sum(self.player_hand) < sum(self.dealer_hand):
            print (f"The Dealer's {sum(self.dealer_hand)} beats your {sum(self.player_hand)}.")
            self.game_outcome = "Lost"

        elif sum(self.player_hand) > sum(self.dealer_hand):
            print (f"Your {sum(self.player_hand)} beats the Dealer's {sum(self.dealer_hand)}.")
            self.game_outcome = "Won"

        else:
            print("Something went terribly wrong when comparing the player and dealer hands. This should never happen.")
            self.game_outcome = "Broken"

        return self.game_outcome

game1 = BlackJack()
print(f"The game is {game1.play()}.")
