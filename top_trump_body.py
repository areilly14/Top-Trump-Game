import pandas as pd
import numpy as np

#Generate the cards with random values in each category between 1 and 100
def makeCards():
    cards =pd.read_csv('country.csv')
    numberOfCards = len(cards)
    cards['Size'] = np.random.randint(100, size=numberOfCards)
    cards['Power'] = np.random.randint(100, size=numberOfCards)
    cards['Happiness'] = np.random.randint(100, size=numberOfCards)
    cards['Owner'] = np.zeros(numberOfCards)
    cards['Position'] = range(numberOfCards)
    return cards

#Deal cards into two piles
def dealCards():
    for index, row in cards.iterrows():
        if row['Position']%2 ==0:
            cards.at[index,'Owner'] = 1
        else:
            cards.at[index,'Owner'] = 2
        cards.at[index,'Position'] = row['Position']//2
        
#Generate and deal cards out
cards = makeCards()
dealCards()
print(cards.to_string())