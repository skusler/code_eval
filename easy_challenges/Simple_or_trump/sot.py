# This is for challenge Simple or Trump @ https://www.codeeval.com/open_challenges/235/

import sys


def sot():
    with open(sys.argv[1], 'r') as card_list:
        for line in card_list:
            face_cards = {'J': 11, 'Q': 12, 'K': 13, 'A': 14}
            card_list_split = line.split(' | ')
            cards = card_list_split[0]
            trump = card_list_split[1]
            each_card = cards.split()
            if trump in each_card[0] and trump in each_card[1]:
                x = each_card[0][:1]
                y = each_card[1][:1]
                if x in face_cards:
                    x = face_cards[x]
                if y in face_cards:
                    y = face_cards[y]
                if int(x == y):
                    print(each_card[0], each_card[1])
                elif int(x > y):
                    print(each_card[0])
                else:
                    print(each_card[1])
            elif trump in each_card[0]:
                print(each_card[0])
            elif trump in each_card[1]:
                print(each_card[1])
