import random
import tkinter as tk 

shapes = {
       "Hearts": "♥",
       "Diamonds": "♦",
       "Clubs": "♣",
       "Spades": "♠"
   }
 
def welcome():
   
   welcoming = input("welcome to Degenerate BlackJack, would you like to play? (yes/no)\n")
   if welcoming.lower() == "yes":  # used lower() function to use all the upper/lower case letter 
      print("Awesome!\n")
      player_name = input("what is your name? \n")
      print(f"Hello {player_name}, you may begin ")

   elif welcoming.lower() == "no":
      print("Alright see you next time")
      exit()

   else:
         print("Error! Could not understand\n")
         exit()
         
 

def shuffling_deck ():
   
   ranks = ['A', '2', '3','4', '5','6','7','8','9', '10','J','Q', 'K']
   suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades'] 

   deck = []
   for i in ranks:
       for j in suits:
           deck.append((i , j)) #tuple which stores multiple values in a variable needs its own parantethis 
                                #this appends the individual suits and ranks for the combination of them all, not all of them 
   global shoe 
   shoe = deck * 6 
   random.shuffle(shoe)
   return shoe 

def draw_cards(ranks, suits):
    
    print(" ┌───────┐")
    print(f" |{ranks:<2}     |")
    print(f" |{suits:^7}|")
    print(f" |     {ranks:>2}|")
    print(" └───────┘")

def draw_face_down():
    print(" ┌───────┐  ")
    print(" |  ***  |  ")
    print(" |  ***  |  ")
    print(" |  ***  |  ")
    print(" └───────┘  ")


def dealing_cards(shoe):
    rank, suit = shoe.pop() 
    symbol = shapes[suit]
    draw_cards(rank, symbol)
    return (rank, suit)

def player_decision (shoe, player_hand):
    while True:
                if decision.lower() == "h":
                    card = dealing_cards(shoe)
                    player_hand.append(card) 
    
                elif decision.lower() == "s":
                    dealer_hand.append(card)
                else:
                    print("Invalid choice, enter (H)it or (S)tand ")
                break 





def game_play():
    welcome()
    shuffling_deck()
    print("Player's hand : \n")
    player_hand = [dealing_cards(shoe), dealing_cards(shoe)]
    print("Dealer's hand : \n")
    global dealer_hand
    dealer_hand = [dealing_cards(shoe)]
    print("Dealer's second card is face down")
    print(" \n")
    global decision 
    decision = input("Press (H)it or (S)tand \n")
    player_decision()
    print(" \n")






# STRAT FROM DEBUGGING THE LOGIC OF THE DECISION FUNCTUONS AND ADD DEALER_CARDS THEN ADDDIG ONE CARD NOT APPENDING THE THING.

# root = tk.Tk ()
# root.title("Degenerate BalckJack")

# root.mainloop()


 



