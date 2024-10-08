import pandas as pd
import numpy as np

#Generate the cards with random values in each category between 0 and 100
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
    number_of_players = int(input("Please input number of players (max 4)"))
    for index, row in cards.iterrows():
        if row['Position']%number_of_players ==0:
            cards.at[index,'Owner'] = 1
        elif row['Position']%number_of_players ==1:
            cards.at[index,'Owner'] = 2
        elif row['Position']%number_of_players ==2:
            cards.at[index,'Owner'] = 3
        else:
            cards.at[index,'Owner'] = 4
            number_of_players = 4
        cards.at[index,'Position'] = row['Position']//number_of_players
    return number_of_players

def sortCards():
    sorted_cards = cards.sort_values(by = ['Owner','Position'])
    return sorted_cards

def playRound(chooser):
    top_cards = pd.DataFrame(cards[cards['Position'] == 0])
    players_top_card = pd.DataFrame(top_cards[cards['Owner'] == 1])
    print("Your card is....")
    print(players_top_card.to_string())
    if chooser == 1:
        category = input("Please choose a category (Size, Power, Happiness)")
    else:
        #category = computerChooseCategory()
        category = "Size"
    print("Category being compared is...." + category)
    winner = compareCards(category,top_cards,chooser)
    print("Player "+str(winner) +" won this round")
    print("The cards in play were...")
    print(top_cards.to_string())
    winner_number_of_cards = len(cards[cards['Owner'] == winner])
    for i in range(len(top_cards)):
        top_cards.at[i,'Owner'] = winner
        top_cards.at[i,'Position'] = winner_number_of_cards + i
    cards.update(top_cards)
    cards["Position"] = cards["Position"] - 1
    return winner

def compareCards(chosen_category,top_cards,chooser):
    winning_card = top_cards.loc[top_cards[chosen_category].idxmax()]
    return winning_card['Owner']
        
#Generate and deal cards out
cards = makeCards()
number_of_players = dealCards()
cards = sortCards()
#print(cards.to_string())
current_winner = 1
while len(cards)>len(cards[cards['Owner']==1])>0:
    current_winner = playRound(current_winner)
    cards = sortCards()
    print("You now have "+ str(len(cards[cards['Owner']==1]))+ " cards")
    input("Ready to start next round?")