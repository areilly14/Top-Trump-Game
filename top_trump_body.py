import pandas as pd
import numpy as np

def makeCards():
    cards =pd.read_csv('country.csv')
    numberOfCards = len(cards)
    cards['Size'] = np.random.randint(100, size=numberOfCards)
    cards['Power'] = np.random.randint(100, size=numberOfCards)
    cards['Happiness'] = np.random.randint(100, size=numberOfCards)
    cards['Owner'] = np.zeros(numberOfCards)
    cards['Position'] = range(numberOfCards)
    print(cards.to_string())
    return cards

def dealCards():
    for index, row in cards.iterrows():
        if row['Position']%2 ==0:
            row['Owner'] = 1
        else:
            row['Owner'] = 2
        row['Position'] = row['Position']//2

cards = makeCards()
dealCards()
print(cards.to_string())