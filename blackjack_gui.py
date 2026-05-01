import random
import tkinter as tk
from tkinter import messagebox

# ------------------ CARD / DECK LOGIC ------------------

SUITS = ["Hearts", "Diamonds", "Clubs", "Spades"]
RANKS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
SUIT_SYMBOLS = {"Hearts": "♥", "Diamonds": "♦", "Clubs": "♣", "Spades": "♠"}


def create_shoe(num_decks=6):
    deck = [(rank, suit) for rank in RANKS for suit in SUITS]
    shoe = deck * num_decks
    random.shuffle(shoe)
    return shoe


def draw_card(shoe):
    return shoe.pop()


def hand_value(hand):
    value = 0
    aces = 0
    for rank, suit in hand:
        if rank in ["J", "Q", "K"]:
            value += 10
        elif rank == "A":
            value += 11
            aces += 1
        else:
            value += int(rank)

    while value > 21 and aces > 0:
        value -= 10
        aces -= 1

    return value


def is_blackjack(hand):
    return len(hand) == 2 and hand_value(hand) == 21


# ------------------ GUI BLACKJACK CLASS ------------------

class BlackjackGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Degenerate Blackjack")

        self.shoe = create_shoe()
        self.bankroll = 100
        self.bet = 10

        self.player_hand = []
        self.dealer_hand = []

        # Layout
        self.dealer_label = tk.Label(root, text="Dealer's Hand:", font=("Arial", 14))
        self.dealer_label.pack()

        self.dealer_cards = tk.Label(root, text="", font=("Consolas", 16))
        self.dealer_cards.pack()

        self.player_label = tk.Label(root, text="Player's Hand:", font=("Arial", 14))
        self.player_label.pack()

        self.player_cards = tk.Label(root, text="", font=("Consolas", 16))
        self.player_cards.pack()

        self.info_label = tk.Label(root, text="", font=("Arial", 12))
        self.info_label.pack()

        # Buttons
        self.button_frame = tk.Frame(root)
        self.button_frame.pack()

        self.hit_button = tk.Button(self.button_frame, text="Hit", width=10, command=self.hit)
        self.hit_button.grid(row=0, column=0)

        self.stand_button = tk.Button(self.button_frame, text="Stand", width=10, command=self.stand)
        self.stand_button.grid(row=0, column=1)

        self.double_button = tk.Button(self.button_frame, text="Double", width=10, command=self.double)
        self.double_button.grid(row=0, column=2)

        self.bankroll_label = tk.Label(root, text=f"Bankroll: ${self.bankroll}", font=("Arial", 12))
        self.bankroll_label.pack()

        self.start_round()

    # ------------------ GAME FLOW ------------------

    def start_round(self):
        if len(self.shoe) < 30:
            self.shoe = create_shoe()

        self.player_hand = [draw_card(self.shoe), draw_card(self.shoe)]
        self.dealer_hand = [draw_card(self.shoe), draw_card(self.shoe)]

        self.update_display(hide_dealer=True)

        if is_blackjack(self.player_hand):
            self.end_round("Blackjack! You win 3:2.")
            self.bankroll += int(self.bet * 1.5)
            return

    def update_display(self, hide_dealer=False):
        # Player cards
        player_text = "  ".join([f"{r}{SUIT_SYMBOLS[s]}" for r, s in self.player_hand])
        self.player_cards.config(text=player_text)

        # Dealer cards
        if hide_dealer:
            dealer_text = f"??  {self.dealer_hand[1][0]}{SUIT_SYMBOLS[self.dealer_hand[1][1]]}"
        else:
            dealer_text = "  ".join([f"{r}{SUIT_SYMBOLS[s]}" for r, s in self.dealer_hand])

        self.dealer_cards.config(text=dealer_text)

        self.bankroll_label.config(text=f"Bankroll: ${self.bankroll}")

    # ------------------ PLAYER ACTIONS ------------------

    def hit(self):
        self.player_hand.append(draw_card(self.shoe))
        self.update_display(hide_dealer=True)

        if hand_value(self.player_hand) > 21:
            self.end_round("You bust!")

    def stand(self):
        self.dealer_play()

    def double(self):
        if self.bankroll < self.bet:
            messagebox.showinfo("Error", "Not enough bankroll to double.")
            return

        self.bankroll -= self.bet
        self.bet *= 2

        self.player_hand.append(draw_card(self.shoe))
        self.update_display(hide_dealer=True)

        if hand_value(self.player_hand) > 21:
            self.end_round("You bust!")
        else:
            self.dealer_play()

    # ------------------ DEALER LOGIC ------------------

    def dealer_play(self):
        self.update_display(hide_dealer=False)

        while hand_value(self.dealer_hand) < 17:
            self.dealer_hand.append(draw_card(self.shoe))
            self.update_display(hide_dealer=False)

        self.resolve()

    # ------------------ ROUND RESOLUTION ------------------

    def resolve(self):
        player_total = hand_value(self.player_hand)
        dealer_total = hand_value(self.dealer_hand)

        if dealer_total > 21:
            self.end_round("Dealer busts! You win.")
            self.bankroll += self.bet * 2
        elif player_total > dealer_total:
            self.end_round("You win!")
            self.bankroll += self.bet * 2
        elif dealer_total > player_total:
            self.end_round("Dealer wins.")
        else:
            self.end_round("Push.")
            self.bankroll += self.bet

    def end_round(self, message):
        self.update_display(hide_dealer=False)
        messagebox.showinfo("Round Over", message)

        if self.bankroll <= 0:
            messagebox.showinfo("Game Over", "You're broke.")
            self.root.destroy()
            return

        self.bet = 10
        self.start_round()


# ------------------ RUN GAME ------------------

root = tk.Tk()
game = BlackjackGUI(root)
root.mainloop()
