from random import*

mode=""
start=0
p1_start=""
p2_start=""
r1=0
r2=0

while True:
    while type(mode)!=int():
        try:
            mode=int(input("Select from 1 or 2\n1. Player vs Bot\n2. Player vs Player\n3. Exit\n"))
            if mode==1:
                q_deck=[6,7,8,9,10,2,3,4,11]
                deck=q_deck*4
                shuffle(deck)
                P_score=0
                B_score=0
                print("START")
                while True:
                    try:
                        start=input("\nWould you like to pick a card? y(yes)/n(no)\n")
                        if start.lower()=="y":
                            x=deck.pop(len(deck)-1)
                            P_score+=x
                            y=deck.pop(len(deck)-1)
                            B_score+=y
                            if P_score==21 or B_score>21:
                                print("\nYou got",x,"points\nYou WON!\nYour score:",P_score,"\nBot's score:  ",B_score,"\n")
                                break
                            elif B_score==21 or P_score>21:
                                print("\nYou got",x,"points\nYou LOST!\nYour score:",P_score,"\nBot's score:  ",B_score,"\n")
                                break
                            else:
                                print("\nYour score:",P_score)
                        elif start.lower()=="n":
                            print("\nYour score:",P_score,"\nGame is ended")
                            break
                        else:
                            print("Please write 'n' or 'y'")
                    except:
                        ValueError
            elif mode==2:
                q_deck=[6,7,8,9,10,2,3,4,11]
                deck=q_deck*4
                shuffle(deck)
                p1=0 #score for player 1
                p2=0 #score for player 2
                print("START")
                while True:
                    try:
                        print("\nP1 score:",p1,"\nP2 score:",p2)
                        while True:
                            try:
                                p1_start=input("\nPlayer 1 would you like to pick a card? y(yes)/n(no)\n").lower()
                                if p1_start.lower()=="y":
                                    break
                                elif p1_start.lower()=="n":
                                    break
                            except:
                                ValueError
                        if p1_start.lower()=="y":
                            x=deck.pop(len(deck)-1)
                            p1+=x
                            if p1==21:
                                print("\nPlayer 1 got",y,"points\n\nPlayer 1 WON!\n\nPlayer's 1 score:",p1,"\nPlayer's 2 score:",p2,"\n")
                                r1+=1
                                break
                            elif p1>21:
                                print("\nPlayer 1 got",y,"points\n\nPlayer 2 WON!\n\nPlayer's 1 score:",p1,"\nPlayer's 2 score:",p2,"\n")
                                r2+=1
                                break
                            else:
                                print("\nPlayer's 1 score:",p1,"\nPlayer's 2 score:",p2)
                        elif p1_start.lower()=="n":
                            print("\nP1 score:",p1,"\nP2 score:",p2,"\nGame is ended\n")
                            break
                        print("\nP1 score:",p1,"\nP2 score:",p2)
                        while True:
                            try:
                                p2_start=input("\nPlayer 1 would you like to pick a card? y(yes)/n(no)\n").lower()
                                if p2_start.lower()=="y":
                                    break
                                elif p2_start.lower()=="n":
                                    break
                            except:
                                ValueError
                        if p2_start.lower()=="y":
                            y=deck.pop(len(deck)-1)
                            p2+=y
                            print("\nPlayer 2 got",y,"points\nPlayer's 2 score:",p2)
                            if p2==21:
                                print("\nPlayer 2 got",y,"points\n\nPlayer 2 WON!\n\nPlayer's 1 score:",p1,"\nPlayer's 2 score:",p2,"\n")
                                r2+=1
                                break
                            elif p2>21:
                                print("\nPlayer 2 got",y,"points\n\nPlayer 1 WON!\n\nPlayer's 1 score:",p1,"\nPlayer's 2 score:",p2,"\n")
                                r1+=1
                                break
                            else:
                                print("\nPlayer's 1 score:",p1,"\nPlayer's 2 score:",p2)
                        elif p2_start.lower()=="n":
                            print("\nP1 score:",p1,"\nP2 score:",p2,"\nGame is ended\n")
                            break
                    except:
                        ValueError
            elif mode==3:
                break
        except:
            ValueError
    break

