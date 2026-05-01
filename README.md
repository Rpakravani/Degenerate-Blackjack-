# 🎰 Degenerate Blackjack — Python + Tkinter GUI

A fully playable Blackjack game built in Python, featuring a clean Tkinter GUI, a 6‑deck shoe, bankroll management, dealer AI, and full game logic.  
This project demonstrates GUI programming, event‑driven design, and modular game architecture.

---

## 🃏 Features

- Tkinter GUI (Hit, Stand, Double buttons)
- 6‑deck shoe with automatic reshuffling
- Dealer AI (hits until 17)
- Blackjack detection
- Bankroll system with adjustable bets
- Double‑down support
- Card rendering using suit symbols
- Clean separation of game logic and GUI

---

## 🧠 Technical Highlights

### **Game Logic**
- Card representation using `(rank, suit)` tuples  
- Hand value calculation with Ace adjustment  
- Blackjack detection  
- Dealer decision loop  
- Shoe creation + random shuffle  

### **GUI Layer (Tkinter)**
- Dynamic card display using Unicode suit symbols  
- Buttons triggering event‑driven actions  
- Pop‑up messages for round results  
- Automatic round resets  
- Bankroll updates in real time  

### **Architecture**
- `BlackjackGUI` class encapsulates all GUI behavior  
- Logic functions (deck, hand value, blackjack check) kept separate  
- Easy to extend with:
  - Splitting  
  - Insurance  
  - Card images  
  - Animations  

---

## 📂 Project Structure

blackjack/

│── blackjack_gui.py

│── README.md

---

## ▶️ How to Run

### **1. Install Python 3**
Python 3.8+ recommended.

### **2. Run the game**

The GUI window will open automatically.

---

## 🎮 Gameplay

- Start with a bankroll of **$100**
- Default bet: **$10**
- Actions:
  - **Hit** → draw a card  
  - **Stand** → end your turn  
  - **Double** → double your bet, draw one card, then stand  
- Dealer reveals cards after you stand  
- Standard Blackjack rules apply  

---

## 🔧 Future Improvements

- Add card image sprites instead of text  
- Add betting input box  
- Add split hands  
- Add sound effects  
- Add animations (card slide‑in)  
- Add a dark‑mode theme  

---

## 🏁 Summary

This project showcases:

- GUI programming with Tkinter  
- Event‑driven design  
- Game logic implementation  
- Clean Python structuring  
- A complete, playable Blackjack experience  






