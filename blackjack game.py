import random

# ---------- Card / Deck Logic ----------

SUITS = ["Hearts", "Diamonds", "Clubs", "Spades"]
RANKS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
SUIT_SYMBOLS = {
    "Hearts": "♥",
    "Diamonds": "♦",
    "Clubs": "♣",
    "Spades": "♠"
}


def create_shoe(num_decks=6):
    deck = [(rank, suit) for rank in RANKS for suit in SUITS]
    shoe = deck * num_decks
    random.shuffle(shoe)
    return shoe


def draw_card(shoe):
    return shoe.pop()


# ---------- Display Helpers ----------

def draw_card_ascii(rank, suit_symbol):
    print(" ┌───────┐")
    print(f" |{rank:<2}     |")
    print(f" |{suit_symbol:^7}|")
    print(f" |     {rank:>2}|")
    print(" └───────┘")


def draw_face_down():
    print(" ┌───────┐")
    print(" |  ***  |")
    print(" |  ***  |")
    print(" |  ***  |")
    print(" └───────┘")


def show_hand(label, hand, hide_first=False):
    print(f"\n{label}'s hand:")
    if hide_first:
        # Show first card face down
        draw_face_down()
        for rank, suit in hand[1:]:
            draw_card_ascii(rank, SUIT_SYMBOLS[suit])
    else:
        for rank, suit in hand:
            draw_card_ascii(rank, SUIT_SYMBOLS[suit])
        print(f"Total: {hand_value(hand)}")


# ---------- Hand Value Logic ----------

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


# ---------- Game Flow ----------

def player_turn(shoe, player_hand, bankroll, bet):
    while True:
        print(f"\nYour total: {hand_value(player_hand)}")
        choice = input("(H)it, (S)tand, (D)ouble? ").strip().lower()

        if choice == "h":
            card = draw_card(shoe)
            player_hand.append(card)
            print("\nYou draw:")
            draw_card_ascii(card[0], SUIT_SYMBOLS[card[1]])

            if hand_value(player_hand) > 21:
                print("\nYou bust!")
                return "bust", bankroll, bet

        elif choice == "d":
            if bankroll >= bet:
                bankroll -= bet
                bet *= 2
                print(f"\nYou double down. New bet: {bet}")
                card = draw_card(shoe)
                player_hand.append(card)
                print("\nYou draw:")
                draw_card_ascii(card[0], SUIT_SYMBOLS[card[1]])
                if hand_value(player_hand) > 21:
                    print("\nYou bust!")
                    return "bust", bankroll, bet
                return "stand", bankroll, bet
            else:
                print("Not enough bankroll to double.")

        elif choice == "s":
            return "stand", bankroll, bet

        else:
            print("Invalid choice. Please enter H, S, or D.")


def dealer_turn(shoe, dealer_hand):
    print("\nDealer reveals:")
    show_hand("Dealer", dealer_hand, hide_first=False)

    while hand_value(dealer_hand) < 17:
        print("\nDealer hits.")
        card = draw_card(shoe)
        dealer_hand.append(card)
        draw_card_ascii(card[0], SUIT_SYMBOLS[card[1]])

    total = hand_value(dealer_hand)
    print(f"\nDealer stands at {total}")
    if total > 21:
        print("Dealer busts!")
    return total


def resolve_round(player_hand, dealer_hand, bankroll, bet):
    player_total = hand_value(player_hand)
    dealer_total = hand_value(dealer_hand)

    print(f"\nYour total: {player_total}")
    print(f"Dealer total: {dealer_total}")

    if player_total > 21:
        print("You lose.")
    elif dealer_total > 21 or player_total > dealer_total:
        print("You win!")
        bankroll += bet * 2
    elif dealer_total > player_total:
        print("You lose.")
    else:
        print("Push (tie).")
        bankroll += bet

    return bankroll


# ---------- Main Game Loop ----------

def welcome():
    print("Welcome to Degenerate Blackjack!")
    while True:
        ans = input("Would you like to play? (yes/no) ").strip().lower()
        if ans == "yes":
            name = input("What is your name? ")
            print(f"Hello {name}, let's begin.\n")
            return
        elif ans == "no":
            print("Alright, maybe next time.")
            exit()
        else:
            print("Please answer yes or no.")


def main():
    welcome()
    shoe = create_shoe()
    bankroll = 100

    while True:
        if len(shoe) < 30:
            print("\nReshuffling shoe...")
            shoe = create_shoe()

        print(f"\nYour bankroll: {bankroll}")
        try:
            bet = int(input("Enter your bet (0 to quit): "))
        except ValueError:
            print("Invalid bet.")
            continue

        if bet == 0:
            print("Thanks for playing.")
            break
        if bet < 0 or bet > bankroll:
            print("Invalid bet amount.")
            continue

        bankroll -= bet

        # Initial deal
        player_hand = [draw_card(shoe), draw_card(shoe)]
        dealer_hand = [draw_card(shoe), draw_card(shoe)]

        show_hand("Player", player_hand)
        show_hand("Dealer", dealer_hand, hide_first=True)

        # Check for blackjack
        if is_blackjack(player_hand) and is_blackjack(dealer_hand):
            print("\nBoth have blackjack. Push.")
            bankroll += bet
            continue
        elif is_blackjack(player_hand):
            print("\nBlackjack! You win 3:2.")
            bankroll += int(bet * 2.5)
            continue
        elif is_blackjack(dealer_hand):
            print("\nDealer has blackjack. You lose.")
            continue

        # Player turn
        result, bankroll, bet = player_turn(shoe, player_hand, bankroll, bet)
        if result == "bust":
            continue

        # Dealer turn
        dealer_total = dealer_turn(shoe, dealer_hand)

        # Resolve
        bankroll = resolve_round(player_hand, dealer_hand, bankroll, bet)

        if bankroll <= 0:
            print("\nYou're out of money. Game over.")
            break


if __name__ == "__main__":
    main()
