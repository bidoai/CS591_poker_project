

import random
import math

# Simply represent the deck of cards as a list of integers [0,1,2,...,51]
cards = list(range(52))

# Map set of cards to integers. Define map as Clubs: 0, Diamonds: 1, Hearts: 2, Spades: 3.
def Set(card):
    if card <= 12:
        return 0
    elif card <= 25:
        return 1
    elif card <= 38:
        return 2
    else:
        return 3

# Maps the cards to numbers 0 - 12, where 0 is 1,..., 11 is King, 12 is Ace
def Number(card):
    return card % 13


def English(card):
    # takes an integer representing a card and tells you what suit and number it is
    cards = ["Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten"
            , "Jack", "Queen", "King", "Ace"]
    if Set(card) == 0:
        return cards[Number(card)] + " of Clubs"
    elif Set(card) == 1:
        return cards[Number(card)] + " of Diamonds"
    elif Set(card) == 2:
        return cards[Number(card)] + " of Hearts"
    else:
        return cards[Number(card)] + " of Spades"
def EnglishHand(cards):
    # param cards: a list of cards
    # output: prints out the English of each card
    for card in cards:
        print(English(card))


# In[6]:

def RoyalFlush(cards):
    
    numbers = []
    for card in cards:
        numbers += [Number(card)]
    set_numbers = set(numbers)
    #print(set_numbers)
    #print(len(set_numbers))
    #print(max(set_numbers))
    #print(min(set_numbers))
    if len(set_numbers) == 5 and max(set_numbers) == 12 and min(set_numbers) == 8:
        #print("I was here!!!")
        if Flush(cards):
            return True
    return False


# In[7]:

def StraightFlush(cards):
    number_cards = [Number(card) for card in cards]
    set_cards = set(number_cards)
    straights = [{12,0,1,2,3},{0,1,2,3,4}, {1,2,3,4,5}, {2,3,4,5,6}, {3,4,5,6,7}, {4,5,6,7,8}, {5,6,7,8,9}, {6,7,8,9,10}, {7,8,9,10,11}
                , {8,9,10,11,12}]
    if Flush(cards)[0]:
        for i in range(len(straights)):
            if set_cards == straights[i]:
                return True, i
    return False, 14
        


# In[8]:

def FourKind(cards):
    numbers = [0 for i in range(13)]
    four_card = [14,14]
    for card in cards:
        numbers[Number(card)] += 1
    for i in range(len(numbers)):
        if numbers[i] == 4:
            four_card[0] = i
        if numbers[i] == 1:
            four_card[1] = i
    return four_card[0] != 14, four_card


# In[9]:

def FullHouse(cards):
    numbers = [0 for i in range(13)]
    set_pair = [14,14]
    for card in cards:
        numbers[Number(card)] += 1
    for i in range(len(numbers)):
        if numbers[i] == 3:
            set_pair[0] = i
        if numbers[i] == 2:
            set_pair[1] = i
    # print(set_pair)
    if 14 not in set_pair:
        return True, set_pair
    else:
        return False, 0


# In[10]:

def Flush(cards):
    sets = [0,0,0,0]
    for card in cards:
        sets[Set(card)] += 1
        #print(sets)
    numbers = [Number(card) for card in cards]
    return max(sets) == 5, sorted(numbers)[-1::-1]


# In[11]:

def Straight(cards):
    number_cards = [Number(card) for card in cards]
    set_cards = set(number_cards)
    straights = [{12,0,1,2,3},{0,1,2,3,4}, {1,2,3,4,5}, {2,3,4,5,6}, {3,4,5,6,7}, {4,5,6,7,8}, {5,6,7,8,9}, {6,7,8,9,10}, {7,8,9,10,11}
                , {8,9,10,11,12}]
    for i in range(len(straights)):
        if set_cards == straights[i]:
            return True, i
    return False, set_cards
        
        


# In[13]:

def ThreeKind(cards):
    numbers = [0 for i in range(13)]
    for card in cards:
        numbers[Number(card)] += 1
    set_card_card = [14,14,14]
    temp = 14
    for i in range(len(numbers)):
        if numbers[i] == 3:
            set_card_card[0] = i
        elif numbers[i] == 1:
            if temp == 14:
                temp = i
            else:
                set_card_card[1] = max(temp, i)
                set_card_card[2] = min(temp, i)
    if 14 not in set_card_card:
        return True, set_card_card
    else:
        return False, 0
            


# In[14]:

def TwoPair(cards):
    numbers = [0 for i in range(13)]
    for card in cards:
        numbers[Number(card)] += 1
    pair_pair_card = [14,14,14]
    temp = 14
    for i in range(len(numbers)):
        if numbers[i] == 2:
            if temp == 14:
                temp = i
            else:
                pair_pair_card[0] = max(temp, i)
                pair_pair_card[1] = min(temp, i)
        if numbers[i] == 1:
            pair_pair_card[2] = i
    if 14 not in pair_pair_card:
        return True, pair_pair_card
    else:
        return False, 0


# In[15]:

def Pair(cards):
    numbers = [0 for i in range(13)]
    for card in cards:
        numbers[Number(card)] += 1
    pair_card_card_card = [14,14,14,14]
    temp0 = 14
    temp1 = 14
    for i in range(len(numbers)):
        if numbers[i] == 2:
            pair_card_card_card[0] = i
        if numbers[i] == 1:
            if temp0 == 14:
                temp0 = i
            elif temp1 == 14:
                temp1 = i
            else:
                singles = sorted([temp0, temp1, i])
                pair_card_card_card[1] = singles[-1]
                pair_card_card_card[2] = singles[1]
                pair_card_card_card[3] = singles[0]
    if len(cards) == 2:
          return pair_card_card_card[0] != 14, [pair_card_card_card[0]]
    elif 14 not in pair_card_card_card:
        return True, pair_card_card_card
    else:
        return False, 0
        


# In[16]:

# Function that reads a sequence of 5 cards, and returns the rank
# Royal flush: 9, Straight flush: 8,..., high card: 0 
def Rank(cards):
    
    if RoyalFlush(cards):
        return 9, 0
    elif StraightFlush(cards)[0]:
        return 8, StraightFlush(cards)[1]
    elif FourKind(cards)[0]:
        return 7, FourKind(cards)[1]
    elif FullHouse(cards)[0]:
        return 6, FullHouse(cards)[1]
    elif Flush(cards)[0]:
        return 5, Flush(cards)[1]
    elif Straight(cards)[0]:
        return 4, Straight(cards)[1]
    elif ThreeKind(cards)[0]:
        return 3, ThreeKind(cards)[1]
    elif TwoPair(cards)[0]:
        return 2, TwoPair(cards)[1]
    elif Pair(cards)[0]:
        return 1, Pair(cards)[1]
    else:
        numbers = [Number(card) for card in cards]
        return 0, sorted(numbers)[-1::-1]


# In[17]:

def InterpretRank(rank):
    # takes input the rank of a combination of cards, and prints
    # out in English what hand you have
    if rank[0] == 9:
        print("Royal Flush")
    elif rank[0] == 8:
        print("Straight Flush: " + str(rank[1]))
    elif rank[0] == 7:
        print("Four of a Kind: " + str(rank[1]))
    elif rank[0] == 6:
        print("Full House: " + str(rank[1]))
    elif rank[0] == 5:
        print("Flush: " + str(rank[1]))
    elif rank[0] == 4:
        print("Straight: " + str(rank[1]))
    elif rank[0] == 3:
        print("Three of a Kind: " + str(rank[1]))
    elif rank[0] == 2:
        print("Two pair: " + str(rank[1]))
    elif rank[0] == 1:
        print("One pair: " + str(rank[1]))
    else:
        print("High Card: " + str(rank[1]))


# In[18]:

def Compare(cards1, cards2):
    # Returns True if cards1 rank higher than cards2 and False if cards1 ranks lower. Returns "Draw" if hands are equal
    rank1 = Rank(cards1)
    rank2 = Rank(cards2)
    if rank1[0] > rank2[0]:
        return True
    elif rank1[0] < rank2[0]:
        return False
    else: 
        # Case where both cards have the same rank (ex: same pair) and need to compare remaining cards.
        # This part needs to be finished
        if rank1[0] in [0,1,2,3,5,6,7]:
            # Cases where CompHighCard can solve
            return CompHighCard(rank1[1], rank2[1])
        elif rank1[0] in [4,8]:
            if rank1[1] > rank2[1]:
                return True
            elif rank1[1] < rank2[1]:
                return False
            else:
                return "Draw"
            # both players have a straight or straight flush
        elif rank1[0] == 9:
            # both players have a royal flush lol
            return "Draw"
                    
        return 0


# In[20]:

def CompHighCard(x1, x2):
    # compares two hands that are both rank 0
    for i in range(len(x1)):
        if Number(x1[i]) > Number(x2[i]):
            return True
        elif Number(x1[i]) < Number(x2[i]):
            return False
    return "Draw"


# In[21]:

from itertools import combinations as comb
def AllCombs(hand, board):
    # returns a list of all combinations of your hand (2 cards) + the board (3 cards)
    # only really need to think of turn and river
    if len(board) == 0:
        return hand
    elif len(board) == 3:
        return hand + board
    elif len(board) >= 4:
        temp = comb(board, 3)
        temp_results = []
        for combo in temp:
            temp_results += [list(hand) + list(combo)]
        return temp_results
            
        


# In[22]:

def BestHand(hand, board):
    if len(board) == 3:
        return list(hand) + list(board)
    all_hands = AllCombs(hand, board)
    temp = all_hands[0]
    for i in range(1, len(all_hands)):
        if Compare(all_hands[i], temp):
            temp = all_hands[i]
    return temp


def ProbWin(hand, board):
    # Takes the players hand, and the cards on the board, and returns the probability that player wins as is.
    #print(hand)
    cards = list(range(52))
    if len(board) == 0:
        for card in hand:
            cards.remove(card)
        remaining_hands = comb(cards, 2)
        wins = 0
        losses = 0
        for temp in remaining_hands:
            if Compare(hand, temp):
                wins += 1
            else:
                losses += 1
        prob_win = wins / (wins + losses)
        return prob_win
    else:
        best_hand = BestHand(hand, board)
        for card in hand:
            cards.remove(card)
        for card in board:
            cards.remove(card)
        opponent_hands = list(comb(cards, 2))
        #print("I am in ProbWin")
        #print(len(opponent_hands))
        #print(best_hand)
        wins = 0
        losses = 0
        #print(board)
        for temp in opponent_hands:
            # print(temp)
            opp_best = BestHand(temp, board)
            #print(opp_best)
            if Compare(best_hand, opp_best):
                wins += 1
            elif Compare(best_hand, opp_best) == False:
                #print(opp_best)
                losses += 1
            else:
                wins +=1
        #print(losses)                    
        prob_win = wins / (wins + losses)
        return prob_win
        
       


def Preflop(hand, board, pot, BB, stacks, turn, bet, alpha, prob_win):
    # stacks: 
    if turn == 0:
        # You go first in preflop
        if stacks[0] / BB < 4:
            BET = stacks[0]
            return 4, BET
        if FewBlindsLeft(stacks[0], BB):
            # go all in if only few big blinds left
            if prob_win > 1 - alpha**2:
                BET = stacks[0]
                return 4,BET
        numbers = [Number(card) for card in cards]
        if 12 in numbers:
            # starting hand has an ace, raise
            if random.random() < 0.8:
                # raise 80% of starting cards that has ace
                return 4, math.floor(random.gauss(2.5, 0.5) * BB)
        if prob_win < random.gauss(0.2, 0.1):
            # really bad hand, need to bluf if want to win
            if random.random() < alpha:
                # bluff with prob alpha
                return 4, math.floor(random.gauss(3, 0.5) * BB)
            else: # are we here1
                # Fold bad hands in some cases
                return 2, 0
              
        if random.random() < prob_win:
            BET = 2 * BB
            return BET
        else: # are we here2
            # limp in
            return 5, BB/2
            
    if turn == 1:
        # you go second preflop.
        if pot == 2 * BB:
            # the opponent limped in
            if prob_win > 0.8:
                # if you have good cards, raise your opponent sometimes 
                if random.random() < prob_win:
                    BET = 2.5 * BB
                    return 4, BET
                else:
                    # Check back
                    return 3, 0
                
            elif prob_win < 0.2:
                if random.random() < alpha ** 2:
                    BET = 3 * BB
                    return 4, BET
                else:
                    return 3, 0
            else:
                # Check back
                return 3, 0
        else: 
            # your opponent bet you
            ex_val = prob_win * pot
            if ex_val > bet:
                if prob_win > random.gauss(0.8, 0.1):
                    # raise opponent if you have good cards
                    return 4, 2 * bet
                elif prob_win > 0.55:
                    # call with a decent hand
                    
                    return 1, bet
                else: 
                    if random.random() < 0.5 * alpha:
                        # call sometimes even when have bad hands
                        return 1, bet
                    else: 
                        # Fold
                        return 2
            else: # are we here6
                if prob_win > 0.8:
                    return 1, bet
                elif prob_win > 0.6:
                    if random.random() < alpha * 0.5:
                        return 1, bet
                    else:
                        return 2, 0
                else: # are we here7
                    if random.random() < alpha * 0.25:
                        return 1, bet
                    else:
                        return 2, 0
                            


# In[77]:


def Postflop(hand, board, pot, BB, stacks, turn, bet, alpha, prob_win):
    print("Bonnie is cute")
    if turn == 0:
        print("but she don't reply?")
        if prob_win > random.gauss(0.7, 0.1):
            # you bet first on the flop with some prob if good cards
            if random.random() < prob_win:
                BET = random.gauss(0.4, 0.15) * pot
                return 4, math.floor(BET)
            else:
                print("here every single time??")
                return 3, 0
        elif prob_win < 0.2:
            # if you have bad cards, bluff with some prob
            if random.random() < alpha * 0.6:
                BET = random.gauss(0.5, 0.2) * pot
                return math.floor(BET)
            else:
                print("no way")
                return 3, 0
        # if not betting just check
        return 3, 0    
    if turn == 1:
        # you play second
        if bet == 0:
            # your opponent checks the flop to you
            # decide to bet, check
            if prob_win > random.gauss(0.65, 0.1):
            # you bet first with some prob if good cards
                if random.random() < prob_win:
                    BET = random.gauss(0.4, 0.15) * pot
                    return 4, math.floor(BET)
                else:
                    return 3, 0
            elif prob_win < 0.2:
            # if you have bad cards, bluff with some prob
                if random.random() < alpha * 0.6:
                    BET = random.gauss(0.5, 0.2) * pot
                    return math.floor(BET)
                else:
                    return 3, 0
            else:
                return 3, 0
        else: 
            # the opponent bets you
            # decide to call, raise, or fold
            ex_val = prob_win * pot
            if ex_val > bet:
                if prob_win > 0.9:
                    # raise opponent if you have good cards
                    return 4, math.floor(random.gauss(2, 0.5) * bet)
                elif prob_win > 0.6:
                    # call with a decent hand
                    BET = bet
                    return 1, BET
            else: 
                if random.random() < 0.45 * alpha:
                    # call sometimes even when have bad hands
                    return 1, bet
                else:
                    # Fold
                    #print("I folded")
                    return 2, 0


# In[103]:


def Turn(hand, board, pot, BB, stacks, turn, bet, alpha, prob_win):
    
    if turn == 0:
        if prob_win > random.gauss(0.7,0.1):
            # you bet first on the flop with some prob if good cards
            if random.random() < prob_win:
                BET = random.gauss(0.45, 0.25) * pot
                return 4, math.floor(BET)
            else:
                return 3, 0
        elif prob_win < 0.2:
            # if you have bad cards, bluff with some prob
            if random.random() < alpha / 3:
                BET = random.gauss(0.7, 0.2) * pot
                return 4, math.floor(BET)
            else:
                return 3, 0
        elif prob_win > 0.5:
            if random.random() < alpha:
                BET = random.gauss(0.5, 0.2) * pot
                return 4, math.floor(BET)
        # just check if not betting
        else:
            return 3, 0
    if turn == 1:
        # you play second
        if bet == 0:
            # your opponent checks the flop to you
            # decide to bet, check
            if prob_win > random.gauss(0.5, 0.1):
            # you bet first with some prob if good cards
                if random.random() < prob_win:
                    BET = random.gauss(prob_win, 0.1) * pot
                    return 4, math.floor(BET)
                else:
                    # Bet just one big blind for fun here!
                    return 4, BB
            elif prob_win < 0.2:
            # if you have bad cards, bluff with some prob
                if random.random() < alpha * 0.3:
                    BET = random.gauss(0.5, 0.2) * pot
                    return 4, math.floor(BET)
                else:
                    return 3, 0
            elif prob_win > 0.5:
                if random.random() < alpha:
                    BET = random.gauss(0.5, 0.2) * pot
                    return 4, math.floor(BET)
            else:
                return 3, 0
        else:
            # the opponent bets you
            # decide to call, raise, or fold
            ex_val = prob_win * pot
            print("hello")
            print("ex_val: " + str(ex_val))
            print(prob_win)
            if ex_val > bet:
                if prob_win > 0.7:
                        # raise opponent if you have good cards
                    return math.floor(random.gauss(2, 0.5) * bet)
                elif prob_win < random.gauss(0.3, 0.15):
                    print("Fold")
                    # Fold if prob win is too low
                    return 2, 0
                else:
                    return 1, bet
            else:
                if random.random() < 0.45* alpha:
                    # call sometimes even when have bad hands
                    return bet
                else:
                    # Fold
                    return 2, 0


# In[105]:


def River(hand, board, pot, BB, stacks, turn, bet, alpha, prob_win):
    if turn == 0:
        if prob_win > random.gauss(0.6, 0.2):
            # you bet first on the river with some prob if good cards
            if random.random() < prob_win:
                # Bet for value when high prob win
                BET = prob_win * pot
                return 4, math.floor(BET)
            else:
                BET = random.gauss(0.4, 0.15) * pot
                return 4, math.floor(BET)
        elif prob_win < random.gauss(0.2, 0.1):
            # if you have bad cards, bluff with some prob
            if random.random() < alpha * 0.6:
                # need to overbet when bluffing
                BET = random.gauss(0.75, 0.2) * pot
                return 4, math.floor(BET)
            else:
                return 3, 0
        elif prob_win > 0.5:
            # decent odds at winning, bet sometimes
            prob_lose = 1 - prob_win
            bet_size = pot * random.gauss(prob_lose, 0.15)
            if random.random() < alpha:
                return 4, math.floor(bet_size)
            else:
                return 3, 0
        else:
            return 3, 0
                    
    if turn == 1:
        # you play second
        if bet == 0:
            # your opponent checks the flop to you
            # decide to bet, check
            if prob_win > 0.6:
            # you bet first with some prob if good cards
                if random.random() < prob_win:
                    BET = random.gauss(0.7, 0.15) * pot
                    return 4, math.floor(BET)
            if prob_win < 0.2:
            # if you have bad cards, bluff with some prob
                if random.random() < alpha / 3:
                    BET = random.gauss(0.5, 0.4) * pot
                    return 4, math.floor(BET)
            return 0
        else:
            # the opponent bets you
            # decide to call, raise, or fold
            ex_val = prob_win * pot
            if ex_val > bet:
                if prob_win > random.gauss(0.85, 0.1):
                    # go all in if prob win > 0.9
                    return 4, stacks[1]
                elif prob_win > random.gauss(0.5, 0.15):
                    # call with a decent hand
                    return 1, bet
            else:
                if random.random() < 0.33 * alpha:                                                    
                    # call sometimes even when have bad hands
                    return 1, bet
                    
                else:
                    return 2, 0





def Move(hand, board, pot, BB, stacks, turn, bet, state, alpha):
    prob_win = ProbWin(hand, board)
    print("Winning Prob:" + str(prob_win))
    if state == 0:
        # Preflop
        """Some notes of starting hands:
                    Tier 1: AA(1), KK(99.5), QQ(99), Ak(94)
                    Tier 2: JJ(98.5), TT(98), 99(97.5)
                    Tier 3: 88(97), 77(96.5), AQ(93)
                    Tier 4: 66(98)~ 22(94), AJ(92) ~ A8(89)
                    Tier 5: A7(88) ~ A2(83), KQ (79), 
                    Tier 6: QJ(65), JT(53), T9, 98, 87, 76, 65
        """
        return Preflop(hand, board, pot, BB, stacks, turn, bet, alpha, prob_win)
        
                            
                    
    elif state == 1:
        # Postflop
        return Postflop(hand, board, pot, BB, stacks, turn, bet, alpha, prob_win)
    elif state == 2:
        # Turn
        return Turn(hand, board, pot, BB, stacks, turn, bet, alpha, prob_win)
        
    else:
        # River
        return River(hand, board, pot, BB, stacks, turn, bet, alpha, prob_win)
                    
        
def FewBlindsLeft(stack_size, BB):
    # outputs True if less than 10 BB's left, and false otherwise
    return stack_size / BB <= 10


def FlopFirst(hand):
    if Pair(hand)[0]:
        # You get dealt a pair
        if Pair(hand)[1] >= 6:
            # always play pocket pairs higher than 8
            return 1
        elif Pair(hand)[1] >= 4:
            return 0.95
        elif Pair(hand)[1] >= 2:
            # play pairs 3,4 with prob 0.9
            return 0.9
        else:
            # Play pair of twoes with prob 0.8
            return 0.8
    else:
        # You have a high card
        # need to adjust this
        return ProbWin(hand, board)
def Suited(hand):
    return Set(hand[0]) == Set(hand[1])
def Connected(hand):
    num1 = Number(hand[0])
    num2 = Number(hand[1])
    return abs(num1 - num2) == 1


# In[292]:



