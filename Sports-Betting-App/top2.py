import matplotlib.pyplot as plt
import pandas as pd 

"""
The purpose of this test is to see whether it was consistently profitable to bet single bets on Liverpool and Man City to win every game
Data will be tested from the last 3 seasons
OUTCOMES: invalid strategy
23/24: 40% loss
22/23: 45% loss
21/22: 20% profit
"""

def top2(csv_file, bankroll, bet_size):
    data = pd.read_csv(csv_file)
    cash = []
    cash.append(bankroll)
    match = 0
    matches = []
    matches.append(match)

    for index, row in data.iterrows():
        stake = bankroll * bet_size
        home = row['HomeTeam']
        away = row['AwayTeam']
        result = row['FTR']
        avgH = row['AvgH']
        avgA = row['AvgA']

        if (home == 'Man City' ) or (home == 'Liverpool'):
            match += 1
            if (result == 'H'):
                bankroll += ((avgH * stake) - stake)
            else:
                bankroll -= stake
            matches.append(match)
            cash.append(bankroll) 

        elif (away == 'Man City') or (away == 'Liverpool'):
            match += 1
            if (result == 'A'):
                bankroll += ((avgA * stake) - stake)
            else:
                bankroll -= stake
            matches.append(match)
            cash.append(bankroll)

     

    plt.plot(matches, cash)
    plt.grid(True)
    plt.xlabel('Matches')
    plt.ylabel('Bankroll')
    plt.show()

"""
Paths:
"C:/Users/hp/Desktop/GitHub-Projects/MACHINELEARNING + AI/Sports-Betting-App/2324.csv"
"C:/Users/hp/Desktop/GitHub-Projects/MACHINELEARNING + AI/Sports-Betting-App/2223.csv"
"C:/Users/hp/Desktop/GitHub-Projects/MACHINELEARNING + AI/Sports-Betting-App/2122.csv"
"""

top2("C:/Users/hp/Desktop/GitHub-Projects/MACHINELEARNING + AI/Sports-Betting-App/2122.csv", 1000, 0.1)