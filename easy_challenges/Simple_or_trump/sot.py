# This is for challenge Simple or Trump @ https://www.codeeval.com/open_challenges/235/

import sys

face_cards = {'J': 11, 'Q': 12, 'K': 13, 'A': 14}


def sot():
    with open(sys.argv[1], 'r') as card_list:
        for line in card_list:
            # Splits first half and second half via pipe.
            card_list_split = line.split(' | ')
            cards = card_list_split[0]
            trump = card_list_split[1]
            # Splits both cards into 2 entries in an array
            each_card = cards.split()
            # For debugging
            # print(cards)
            # print(trump)
            # print(each_card)
            if trump[0] in each_card[0] and trump in each_card[1]:
                print("Double_neither in")
                double_neither(each_card)
            elif trump in each_card[0]:
                print("Running first elif")
                print(each_card[0])
            elif trump in each_card[1]:
                print("Running second elif")
                print(each_card[1])
            else:
                print("Double_neither not in")
                double_neither(each_card)


def double_neither(each_card):
    print("Running double_neither")
    # First letter of each string in the array.
    x = each_card[0][:1]
    y = each_card[1][:1]
    # If first letter of string is in face_cards it assigns the variable the corresponding number.
    if x in face_cards:
        x = face_cards[x]
    if y in face_cards:
        y = face_cards[y]
    if int(x) == int(y):
        print(each_card[0], each_card[1])
    elif int(x) > int(y):
        print(each_card[0])
    else:
        print(each_card[1])

sot()

