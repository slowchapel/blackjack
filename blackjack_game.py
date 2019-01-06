#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from random import shuffle


class Game:
    def __init__(self):
        self.dealer = Dealer()
        self.human = Human()
        self.players = [self.dealer, self.human]
        self.deck = Deck()
    
    def setup_game(self):
        num_decks = int(input("How many decks do you want to play with? "))
        self.deck.get_decks(num_decks)
        print(f'You are playing with {num_decks} deck.')
        self.deck.shuffle_deck()
        #print(deck.sets)
        
    def play_hand(self):
        self.dealer.deal_hand(self.deck, self.players)
        if self.human.hand_value() == 21 and self.dealer.hand_value() == 21:
            print("Dealer and Player both got Blackjack. It's a push. ")
        elif self.human.hand_value() == 21:
            print("You got Blackjack. You Win! ")
        elif self.dealer.hand_value() == 21:
            print("Dealer got Blackjack. You Lose! ")
        else:
            while not self.human.hand_busted():
                self.show_hand()
                while True:
                    ask = input("H for Hit, S for stand?  ")
                    if ask.lower() == "h": 
                        self.human.hit(self.deck)
                        break
                    elif ask.lower() == "s":
                        break
                if ask.lower() == "s":
                    break
            if self.human.hand_busted():
                self.show_hand(False)
                print("You Busted! You Lose! ")
            else:
                while self.dealer.hand_value() < 17 and not self.dealer.hand_busted():
                    self.dealer.hit(self.deck)
                self.show_hand(hidden_card = False)
                if self.dealer.hand_busted():
                    print("Dealer Busted! You Win! ")
                elif self.dealer.hand_value() == self.human.hand_value():
                    print("Push")
                elif self.dealer.hand_value() > self.human.hand_value():
                    print("You Lose! ")
                else:
                    print("You Win! ")
     
    def show_hand(self, hidden_card = True):
        print(f"Dealer showing {self.dealer.hand[1] if hidden_card else [i for i in self.dealer.hand]}")
        print(f"Player has {[i for i in self.human.hand]}")

class Deck:
    def __init__(self):
        self.suits = ['Spades','Clubs', 'Hearts', 'Diamonds']
        self.rank = [i for i in range(1, 13)]
        self.sets = [(i,j)for i in self.suits for j in self.rank] #nested list comp
        
    
    def get_decks(self, num):
        self.sets *= num
        return self.sets
    
    def shuffle_deck(self):
        shuffle(self.sets)
        return self.sets
    
    def get_card(self):
        return self.sets.pop()
            #add logic for empty deck
        
class Player:
    def __init__(self):
        self.hand = []
        self.cards = 0
        
   
    def hit(self, deck):
        self.hand.append(deck.get_card())
        return self.hand
    
    def hand_busted(self):
        rv = 0
        for card in self.hand:
            if 0 < card[1] < 11:
                rv += card[1]
            else:
                rv += 10
                
        return rv > 21
    
    def hand_value(self):
        rv = 0
        ace = 0
        for card in self.hand:
            if 1 < card[1] < 11:
                rv += card[1]
            elif card[1] ==  1:
                ace += 1
            else:
                rv += 10 
        if ace == 0:
            return rv
        return rv + ace if (rv + ace - 1) > 10 else rv + ace + 10
        

class Human(Player):
    pass

class Dealer(Player):
    def deal_hand(self, deck, players):
        for i in range(2):
            for player in players:
                player.hand.append(deck.get_card())
                
def main():
    game = Game()
    game.setup_game()
    game.play_hand()

main() 


# In[ ]:




