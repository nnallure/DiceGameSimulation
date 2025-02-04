# Dice Game Simulation 🎲  

This repository contains a Python script that simulates a simple dice game. The simulation runs 10,000 games and calculates the average and maximum winnings based on the game rules.  

## How It Works  

1. A player rolls a six-sided die.  
2. If the roll is 1, 2, or 3, the game ends, and the player wins nothing.  
3. If the roll is 4, 5, or 6, the roll value is added to the total winnings, and the player rolls again.  
4. The game continues until the player rolls a 1, 2, or 3.  
5. The final winnings for that game are recorded.  
6. The simulation repeats this process 10,000 times and calculates:  
   - The **average winnings** across all games.  
   - The **highest winnings** achieved in a single game.  

## Output Example  
Average amount won = $4.54
Max amount won = $30.00

## How to Run  

Ensure you have Python installed, then execute the script with:  

```bash
python game_simulation.py
