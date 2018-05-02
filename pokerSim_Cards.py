
# coding: utf-8

# In[2]:


CARD_SUIT_HEART = 0
CARD_SUIT_DIAMOND = 1
CARD_SUIT_CLUB = 2
CARD_SUIT_SPADE = 3

CARD_RANK_ACE = 0
CARD_RANK_TWO = 1
CARD_RANK_THREE = 2
CARD_RANK_FOUR = 3
CARD_RANK_FIVE = 4
CARD_RANK_SIX = 5
CARD_RANK_SEVEN = 6
CARD_RANK_EIGHT = 7
CARD_RANK_NINE = 8
CARD_RANK_TEN = 9
CARD_RANK_JACK = 10
CARD_RANK_QUEEN = 11
CARD_RANK_KING = 12

def convert_rank(rank):
    return{
        0:"ACE",
        1:"TWO",
        2:"THREE",
        3:"FOUR",
        4:"FIVE",
        5:"SIX",
        6:"SEVEN",
        7:"EIGHT",
        8:"NINE",
        9:"TEN",
        10:"JACK",
        11:"QUEEN",
        12:"KING",
    }[rank]
def convert_suit(suit):
    return{
        0:"HEARTS",
        1:"DIAMONDS",
        2:"CLUBS",
        3:"SPADES",
    }[suit]


    


# In[3]:


class pokerSim_Card:
    def __init__(self,rank,suit):
        self.rank = rank
        self.suit = suit
    def __init__(self,index):
        self.rank = index%13
        self.suit = index//13

    def __str__(self):
        rank = convert_rank(self.rank)
        suit = convert_suit(self.suit)
        return rank+" of "+suit


# In[4]:


from random import shuffle
class pokerSim_Deck:
    def __init__(self):
        self.deckInIndex = []
        self.deck = []
        for i in range(52):
            self.deckInIndex.append(i)
        shuffle(self.deckInIndex)
        for index in self.deckInIndex:
            card = pokerSim_Card(index)
            self.deck.append(card)
    def __str__(self):
        result = ""
        for i in self.deck:
            result += str(i)+", "
        return result


# In[5]:


SHOW_DOWN_ROYAL_FLUSH = 9
SHOW_DOWN_STRAIGHT_FLUSH = 8
SHOW_DOWN_FOUR_OF_A_KIND = 7
SHOW_DOWN_FULL_HOUSE = 6
SHOW_DOWN_FLUSH = 5
SHOW_DOWN_STRAIGHT = 4
SHOW_DOWN_THREE_OF_A_KIND = 3
SHOW_DOWN_TWO_PAIR = 2
SHOW_DOWN_ONE_PAIR = 1
SHOW_DOWN_HIGH_CARD = 0
SHOW_DOWN_NEGATIVE = -1

def checkRoyalFlush(hands):
    cards_rank = []
    cards_suit = []
    for i in hands:
        cards_rank.append(i.rank)
        cards_suit.append(i.suit)
    cards_rank.sort()
    if(cards_rank[0]==0 and cards_rank[1]==9 and cards_rank[2]==10 and cards_rank[3]==11 and cards_rank[4]==12):#it's 10JQKA
        if(cards_suit[0]==cards_suit[1] and cards_suit[0]==cards_suit[2] and cards_suit[0]==cards_suit[3] and cards_suit[0]==cards_suit[4]): #it's same suits
            return SHOW_DOWN_ROYAL_FLUSH
        else: return SHOW_DOWN_NEGATIVE
    else: return SHOW_DOWN_NEGATIVE

def checkStraightFlush(hands):
    cards_rank = []
    cards_suit = []
    for i in hands:
        cards_rank.append(i.rank)
        cards_suit.append(i.suit)
    cards_rank.sort()
    if(cards_rank[0]==cards_rank[1]-1 and cards_rank[1]==cards_rank[2]-1 and cards_rank[2]==cards_rank[3]-1 and cards_rank[3]==cards_rank[4]-1): #it's straight
        if(cards_suit[0]==cards_suit[1] and cards_suit[0]==cards_suit[2] and cards_suit[0]==cards_suit[3] and cards_suit[0]==cards_suit[4]):
            return (SHOW_DOWN_STRAIGHT_FLUSH,cards_rank[0])
    return (SHOW_DOWN_NEGATIVE,0)
def checkFourOfAHand(hands):
    cards_rank = []
    for i in hands:
        cards_rank.append(i.rank)
    cards_rank.sort()     
    if(cards_rank[0]==cards_rank[1] and cards_rank[1]==cards_rank[2] and cards_rank[2]==cards_rank[3]):
        return (SHOW_DOWN_FOUR_OF_A_KIND,cards_rank[0],cards_rank[4])
    if(cards_rank[1]==cards_rank[2] and cards_rank[2]==cards_rank[3] and cards_rank[3]==cards_rank[4]):
        return (SHOW_DOWN_FOUR_OF_A_KIND,cards_rank[4],cards_rank[0])
    return (SHOW_DOWN_NEGATIVE,0,0)
def checkFullHouse(hands):
    cards_rank = []
    for i in hands:
        cards_rank.append(i.rank)
    cards_rank.sort()     
    if(cards_rank[0]==cards_rank[1] and cards_rank[1]==cards_rank[2] and cards_rank[3]==cards_rank[4]):
        return (SHOW_DOWN_FULL_HOUSE,cards_rank[0],cards_rank[3]) #type,rank of three matching, rank of two matching
    if(cards_rank[0]==cards_rank[1] and cards_rank[2]==cards_rank[3] and cards_rank[3]==cards_rank[4]):
        return (SHOW_DOWN_FULL_HOUSE,cards_rank[2],cards_rank[0]) #type,rank of three matching, rank of two matching
    return (SHOW_DOWN_NEGATIVE,0,0)
def checkFlush(hands):
    cards_rank = []
    cards_suit = []
    for i in hands:
        cards_rank.append(i.rank)
        cards_suit.append(i.suit)
    cards_rank.sort()
    if(cards_suit[0]==cards_suit[1] and cards_suit[0]==cards_suit[2] and cards_suit[0]==cards_suit[3] and cards_suit[0]==cards_suit[4]):
        return (SHOW_DOWN_FLUSH,cards_rank[4],cards_rank[3],cards_rank[2],cards_rank[1],cards_rank[0])
    return (SHOW_DOWN_NEGATIVE,0,0,0,0,0)
def checkStraight(hands):
    cards_rank = []
    cards_suit = []
    for i in hands:
        cards_rank.append(i.rank)
        cards_suit.append(i.suit)
    cards_rank.sort()
    if(cards_rank[0]==0 and cards_rank[1]==9 and cards_rank[2]==10 and cards_rank[3]==11 and cards_rank[4]==12): #10JQKA
        return (SHOW_DOWN_STRAIGHT,cards_rank[0])
    if(cards_rank[0]==cards_rank[1]-1 and cards_rank[1]==cards_rank[2]-1 and cards_rank[2]==cards_rank[3]-1 and cards_rank[3]==cards_rank[4]-1):
        return(SHOW_DOWN_STRAIGHT,cards_rank[4])
    return(SHOW_DOWN_NEGATIVE,0)
def checkThreeOfAKind(hands):
    cards_rank = []
    for i in hands:
        cards_rank.append(i.rank)
    cards_rank.sort()
    if(cards_rank[0]== cards_rank[1] and cards_rank[1]== cards_rank[2]):
        return (SHOW_DOWN_THREE_OF_A_KIND,cards_rank[0],cards_rank[4],cards_rank[3])
    if(cards_rank[1]== cards_rank[2] and cards_rank[2]== cards_rank[3]):
        return (SHOW_DOWN_THREE_OF_A_KIND,cards_rank[1],cards_rank[4],cards_rank[0])
    if(cards_rank[2]== cards_rank[3] and cards_rank[3]== cards_rank[4]): 
        return (SHOW_DOWN_THREE_OF_A_KIND,cards_rank[2],cards_rank[1],cards_rank[0])
    return(SHOW_DOWN_NEGATIVE,0)
def checkTwoPair(hands):
    cards_rank = []
    for i in hands:
        cards_rank.append(i.rank)
    cards_rank.sort()
    if(cards_rank[0]== cards_rank[1] and cards_rank[2]== cards_rank[3]):
        return (SHOW_DOWN_TWO_PAIR,cards_rank[2],cards_rank[0],cards_rank[4]) #rank of first pair, rank of second pair, single
    if(cards_rank[0]== cards_rank[1] and cards_rank[3]== cards_rank[4]):
        return (SHOW_DOWN_TWO_PAIR,cards_rank[3],cards_rank[0],cards_rank[2]) #rank of first pair, rank of second pair, single
    if(cards_rank[1]== cards_rank[2] and cards_rank[3]== cards_rank[4]):
        return (SHOW_DOWN_TWO_PAIR,cards_rank[3],cards_rank[1],cards_rank[0]) #rank of first pair, rank of second pair, single
    return(SHOW_DOWN_NEGATIVE,0,0,0)
def checkOnePair(hands):
    cards_rank = []
    for i in hands:
        cards_rank.append(i.rank)
    cards_rank.sort()
    if(cards_rank[0]== cards_rank[1]):
        return (SHOW_DOWN_ONE_PAIR,cards_rank[0],cards_rank[2],cards_rank[3],cards_rank[4]) #rank of pair, rank of the remaining cards
    if(cards_rank[1]== cards_rank[2]):
        return (SHOW_DOWN_ONE_PAIR,cards_rank[1],cards_rank[0],cards_rank[3],cards_rank[4]) #rank of pair, rank of the remaining cards
    if(cards_rank[2]== cards_rank[3]):
        return (SHOW_DOWN_ONE_PAIR,cards_rank[2],cards_rank[0],cards_rank[1],cards_rank[4]) #rank of pair, rank of the remaining cards
    if(cards_rank[3]== cards_rank[4]):
        return (SHOW_DOWN_ONE_PAIR,cards_rank[3],cards_rank[0],cards_rank[1],cards_rank[2]) #rank of pair, rank of the remaining cards
    return(SHOW_DOWN_NEGATIVE,0,0,0)
def checkHighCard(hands):
    cards_rank = []
    for i in hands:
        cards_rank.append(i.rank)
    cards_rank.sort()
    return(SHOW_DOWN_HIGH_CARD,cards_rank[0],cards_rank[1],cards_rank[2],cards_rank[3],cards_rank[4])
def getHighestHands(hands):
    if(checkRoyalFlush(hands)>SHOW_DOWN_NEGATIVE):
        return SHOW_DOWN_ROYAL_FLUSH
    elif(checkStraightFlush(hands)[0]>SHOW_DOWN_NEGATIVE):
        return SHOW_DOWN_STRAIGHT_FLUSH
    elif(checkFourOfAHand(hands)[0]>SHOW_DOWN_NEGATIVE):
        return SHOW_DOWN_FOUR_OF_A_KIND
    elif(checkFullHouse(hands)[0]>SHOW_DOWN_NEGATIVE):
        return SHOW_DOWN_FULL_HOUSE
    elif(checkFlush(hands)[0]>SHOW_DOWN_NEGATIVE):
        return SHOW_DOWN_FLUSH
    elif(checkStraight(hands)[0]>SHOW_DOWN_NEGATIVE):
        return SHOW_DOWN_STRAIGHT
    elif(checkThreeOfAKind(hands)[0]>SHOW_DOWN_NEGATIVE):
        return SHOW_DOWN_THREE_OF_A_KIND
    elif(checkTwoPair(hands)[0]>SHOW_DOWN_NEGATIVE):
        return SHOW_DOWN_TWO_PAIR
    elif(checkOnePair(hands)[0]>SHOW_DOWN_NEGATIVE):
        return SHOW_DOWN_ONE_PAIR
    else:
        return SHOW_DOWN_HIGH_CARD
    


# In[6]:


HANDS_ONE_WIN = 1
HANDS_TWO_WIN = 2
HANDS_DRAW = 0

def compareStraightFlush(hands1, hands2):
    if(hands1[1]>hands2[1]):
        return HANDS_ONE_WIN
    elif(hands1[1]<hands2[1]):
        return HANDS_TWO_WIN
    else: return HANDS_DRAW
    
def compareFourOfAHand(hands1, hands2):
    fourHandsOne = int(hands1[1])
    fourHandsTwo = int(hands2[1])
    singleHandsOne = int(hands1[2])
    singleHandsTwo = int(hands2[2])
    if(fourHandsOne == 0):
        fourHandsOne=13
    if(fourHandsTwo == 0):
        fourHandsTwo=13
    if(singleHandsOne == 0):
        singleHandsOne=13        
    if(singleHandsTwo == 0):
        singleHandsTwo=13         
    if(fourHandsOne>fourHandsTwo):
        return HANDS_ONE_WIN
    elif(fourHandsOne<fourHandsTwo):
        return HANDS_TWO_WIN
    elif(singleHandsOne>singleHandsTwo):
        return HANDS_ONE_WIN
    elif(singleHandsOne<singleHandsTwo):
        return HANDS_TWO_WIN
    else:
        return HANDS_DRAW

def compareFullHouse(hands1, hands2):
    ThreeMatchOne = int(hands1[1])
    ThreeMatchTwo = int(hands2[1])
    TwoMatchOne = int(hands1[2])
    TwoMatchTwo = int(hands2[2])
    if(ThreeMatchOne == 0):
        ThreeMatchOne=13
    if(ThreeMatchTwo == 0):
        ThreeMatchTwo=13
    if(TwoMatchOne == 0):
        TwoMatchOne=13        
    if(TwoMatchTwo == 0):
        TwoMatchTwo=13         
    if(ThreeMatchOne>ThreeMatchTwo):
        return HANDS_ONE_WIN
    elif(ThreeMatchOne<ThreeMatchTwo):
        return HANDS_TWO_WIN
    elif(TwoMatchOne>TwoMatchTwo):
        return HANDS_ONE_WIN
    elif(TwoMatchOne<TwoMatchTwo):
        return HANDS_TWO_WIN
    else:
        return HANDS_DRAW
    return HANDS_DRAW    
    
def compareFlush(hands1, hands2):
    #(SHOW_DOWN_FULL_HOUSE,cards_rank[0],cards_rank[3])
    h1 = []
    h2 = []
    h1.append(int(hands1[1]))
    h1.append(int(hands1[2])) 
    h1.append(int(hands1[3])) 
    h1.append(int(hands1[4])) 
    h1.append(int(hands1[5]))
    h2.append(int(hands2[1]))
    h2.append(int(hands2[2])) 
    h2.append(int(hands2[3])) 
    h2.append(int(hands2[4])) 
    h2.append(int(hands2[5]))
    for i in range(len(h1)):
        if(h1[i]==0):
            h1[i] = 13
    for i in range(len(h2)):
        if(h2[i]==0):
            h2[i] = 13      
    h1.sort(reverse=True)
    h2.sort(reverse=True)
    for i in range(len(h1)):
        if(h1[i]>h2[i]):
            return HANDS_ONE_WIN
        elif(h1[i]<h2[i]):
            return HANDS_TWO_WIN
    return HANDS_DRAW

def compareStraight(hands1, hands2):
    #return(SHOW_DOWN_STRAIGHT,cards_rank[4])
    StraightOne = int(hands1[1])
    StraightTwo = int(hands2[1])
    if(StraightOne == 0):
        StraightOne=13
    if(StraightTwo == 0):
        StraightTwo=13       
    if(StraightOne>StraightTwo):
        return HANDS_ONE_WIN
    elif(StraightOne<StraightTwo):
        return HANDS_TWO_WIN
    return HANDS_DRAW
def compareThreeOfAKind(hands1, hands2):
    AKindOne = int(hands1[1])
    AKindTwo = int(hands2[1])

    if(AKindOne == 0):
        AKindOne=13
    if(AKindTwo == 0):
        AKindTwo=13   
    if(AKindOne>AKindTwo):
        return HANDS_ONE_WIN
    elif(AKindOne<AKindTwo):
        return HANDS_TWO_WIN
    
    h1 = []
    h2 = []
    h1.append(int(hands1[2]))
    h2.append(int(hands2[2]))
    h1.append(int(hands1[3]))
    h2.append(int(hands2[3]))
    for i in range(len(h1)):
        if(h1[i]==0):
            h1[i] = 13
    for i in range(len(h2)):
        if(h2[i]==0):
            h2[i] = 13      
    h1.sort(reverse=True)
    h2.sort(reverse=True)    
    for i in range(len(h1)):
        if(h1[i]>h2[i]):
            return HANDS_ONE_WIN
        elif(h1[i]<h2[i]):
            return HANDS_TWO_WIN
    return HANDS_DRAW

def compareTwoPair(hands1, hands2):
    firstPairOne = int(hands1[1])
    firstPairTwo = int(hands2[1])
    secondPairOne = int(hands1[2])
    secondPairTwo = int(hands2[2])
    
    if(firstPairOne == 0):
        firstPairOne=13
    if(firstPairTwo == 0):
        firstPairTwo=13
    if(secondPairOne == 0):
        secondPairOne=13        
    if(secondPairTwo == 0):
        secondPairTwo=13         
    if(firstPairOne>firstPairTwo):
        return HANDS_ONE_WIN
    elif(firstPairOne<firstPairTwo):
        return HANDS_TWO_WIN
    elif(secondPairOne>secondPairTwo):
        return HANDS_ONE_WIN
    elif(secondPairOne<secondPairTwo):
        return HANDS_TWO_WIN
    singleOne = int(hands1[3])
    singleTwo = int(hands2[3])
    if(singleOne == 0):
        singleOne=13
    if(singleTwo == 0):
        singleTwo=13  
    if(singleOne>singleTwo):
        return HANDS_ONE_WIN
    elif(singleOne<singleTwo):
        return HANDS_TWO_WIN          
    return HANDS_DRAW
def compareOnePair(hands1, hands2):
    PairOne = int(hands1[1])
    PairTwo = int(hands2[1])
    if(PairOne == 0):
        PairTwo=13
    if(PairOne == 0):
        PairTwo=13
    if(PairOne>PairTwo):
        return HANDS_ONE_WIN
    elif(PairOne<PairTwo):
        return HANDS_TWO_WIN
    h1 = []
    h2 = []
    h1.append(int(hands1[2]))
    h2.append(int(hands2[2]))
    h1.append(int(hands1[3]))
    h2.append(int(hands2[3]))     
    h1.append(int(hands1[4]))
    h2.append(int(hands2[4]))   
    for i in range(len(h1)):
        if(h1[i]==0):
            h1[i] = 13
    for i in range(len(h2)):
        if(h2[i]==0):
            h2[i] = 13      
    h1.sort(reverse=True)
    h2.sort(reverse=True)
    for i in range(len(h1)):
        if(h1[i]>h2[i]):
            return HANDS_ONE_WIN
        elif(h1[i]<h2[i]):
            return HANDS_TWO_WIN
    return HANDS_DRAW
def compareHighCard(hands1, hands2):
    h1 = []
    h2 = []
    h1.append(int(hands1[1]))
    h1.append(int(hands1[2])) 
    h1.append(int(hands1[3])) 
    h1.append(int(hands1[4])) 
    h1.append(int(hands1[5]))
    h2.append(int(hands2[1]))
    h2.append(int(hands2[2])) 
    h2.append(int(hands2[3])) 
    h2.append(int(hands2[4])) 
    h2.append(int(hands2[5]))
    for i in range(len(h1)):
        if(h1[i]==0):
            h1[i] = 13
    for i in range(len(h2)):
        if(h2[i]==0):
            h2[i] = 13      
    h1.sort(reverse=True)
    h2.sort(reverse=True)
    for i in range(len(h1)):
        if(h1[i]>h2[i]):
            return HANDS_ONE_WIN
        elif(h1[i]<h2[i]):
            return HANDS_TWO_WIN
    return HANDS_DRAW

def compareTwoHands(hands1,hands2):
    highestOfHands1 = getHighestHands(hands1)
    highestOfHands2 = getHighestHands(hands2)
    if(highestOfHands1>highestOfHands2):
        return HANDS_ONE_WIN
    elif(highestOfHands1<highestOfHands2):
        return HANDS_TWO_WIN
    else:
        if(highestOfHands1==SHOW_DOWN_ROYAL_FLUSH):
            return HANDS_DRAW #impossible
        elif(highestOfHands1==SHOW_DOWN_STRAIGHT_FLUSH):
            return compareStraightFlush(checkStraightFlush(hands1),checkStraightFlush(hands2))
        elif(highestOfHands1==SHOW_DOWN_FOUR_OF_A_KIND):
            return compareFourOfAHand(checkFourOfAHand(hands1),checkFourOfAHand(hands2))
        elif(highestOfHands1==SHOW_DOWN_FULL_HOUSE):
            return compareFullHouse(checkFullHouse(hands1),checkFullHouse(hands2))        
        elif(highestOfHands1==SHOW_DOWN_FLUSH):
            return compareFlush(checkFlush(hands1),checkFlush(hands2))
        elif(highestOfHands1==SHOW_DOWN_STRAIGHT):
            return compareStraight(checkStraight(hands1),checkStraight(hands2))
        elif(highestOfHands1==SHOW_DOWN_THREE_OF_A_KIND):
            return compareThreeOfAKind(checkThreeOfAKind(hands1),checkThreeOfAKind(hands2))
        elif(highestOfHands1==SHOW_DOWN_TWO_PAIR):
            return compareTwoPair(checkTwoPair(hands1),checkTwoPair(hands2))
        elif(highestOfHands1==SHOW_DOWN_ONE_PAIR):
            return compareOnePair(checkOnePair(hands1),checkOnePair(hands2))
        else:#high card
            return compareHighCard(checkHighCard(hands1),checkHighCard(hands2))


# In[7]:


def getAllPossibilities(playerHand,communityCards):
    allCards = playerHand+communityCards
    allPossibilities = []
    for firstCardIndex in range(3):
        for secondCardIndex in range(firstCardIndex+1,4):
            for thirdCardIndex in range(secondCardIndex+1,5):
                for fourthCardIndex in range(thirdCardIndex+1,6):
                    for fifthCardIndex in range(fourthCardIndex+1,7):
                        single = []
                        single.append(allCards[firstCardIndex])
                        single.append(allCards[secondCardIndex])
                        single.append(allCards[thirdCardIndex])
                        single.append(allCards[fourthCardIndex])
                        single.append(allCards[fifthCardIndex])
                        allPossibilities.append(single)
    return allPossibilities

def findBest(allPossibility):
    best = allPossibility[0]
    for comparison in allPossibility:
        if(compareTwoHands(best,comparison)==HANDS_TWO_WIN):
            best = comparison
    return best


# In[8]:




