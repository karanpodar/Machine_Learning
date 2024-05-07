'''
Minimum Consecutive Cards to Pick Up

You are given an integer array cards where cards[i] represents the value of the ith card. A pair of cards are matching if the cards have the same value.

Return the minimum number of consecutive cards you have to pick up to have a pair of matching cards among the picked cards. If it is impossible to have matching cards, return -1.

Example 1:

Input: cards = [3,4,2,3,4,7]
Output: 4
Explanation: We can pick up the cards [3,4,2,3] which contain a matching pair of cards with value 3. Note that picking up the cards [4,2,3,4] is also optimal.
Example 2:

Input: cards = [1,0,5,3]
Output: -1
Explanation: There is no way to pick up a set of consecutive cards that contain a pair of matching cards.
 
'''

def consec_cards(cards):
    hold = []
    for i in range(len(cards)):
        if cards[i] in cards[i+1:]:
            j = i + 1
            while j <= len(cards[i+1:]):
            # for j in range(len(cards[i+1:])):
                # print('i', i)
                # print('j', j)
                # print(cards[i+j])
                if cards[j] == cards[i]:
                    hold.append(j-i+1)
                    break
                else:
                    j = j + 1
    print(hold)
    if hold:
        return min(hold)
    else:
        return -1
                
cards = [3,4,2,3,4,7]
print(consec_cards(cards))

cards = [1,0,5,3]
print(consec_cards(cards))

cards = [77,10,11,51,69,83,33,94,0,42,86,41,65,40,72,8,53,31,43,22,9,94,45,80,40,0,84,34,76,28,7,79,80,93,20,82,36,74,82,89,74,77,27,54,44,93,98,44,39,74,36,9,22,57,70,98,19,68,33,68,49,86,20,50,43]
print(consec_cards(cards))