from random import*

mode=""
start=0
p1_start=""
p2_start=""
draws=0
r1=0
r2=0

txt="Игра «21»"
print(txt.center(110))

while True:
    while type(mode)!=int():
        try:
            mode=int(input("\nSelect from 1 or 2\n1. Player vs Bot(no bot's UI)\n2. Player vs Player\n3. Records\n4. Rules\n5. Exit\n"))
            if mode==1:
                q_deck=[6,7,8,9,10,2,3,4,11]
                deck=q_deck*4
                shuffle(deck)
                P_score=0
                B_score=0
                print("START")
                while True:
                    try:
                        start=input("\nWould you like to pick a card? y(yes)/n(no)\n").lower()
                        if start=="y":
                            x=deck.pop(len(deck)-1)
                            P_score+=x
                            y=deck.pop(len(deck)-1)
                            B_score+=y
                            if P_score==21 and B_score==21:
                                print("\nYou got",x,"points\nBot got",y,"points\n\nDraw!\nYour score:",P_score,"\nBot's score:",B_score,"\n")
                            elif P_score>21 and B_score>21:
                                print("\nYou got",x,"points\nBot got",y,"points\n\nDraw!\nYour score:",P_score,"\nBot's score:",B_score,"\n")
                            elif P_score==21 or B_score>21:
                                print("\nYou got",x,"points\nBot got",y,"points\n\nYou WON!\nYour score:",P_score,"\nBot's score:  ",B_score,"\n")
                                break
                            elif B_score==21 or P_score>21:
                                print("\nYou got",x,"points\nBot got",y,"points\n\nYou LOST!\nYour score:",P_score,"\nBot's score:",B_score,"\n")
                                break
                            else:
                                print("\nYou got",x,"points\nBot got",y,"points\n\nYour score:",P_score,"\nBot's score:",B_score)
                        elif start=="n":
                            print("\nYour score:",P_score,"\nBot's score:",B_score,"\n\nGame is ended\n")
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
                                if p1_start=="y":
                                    break
                                elif p1_start=="n":
                                    break
                            except:
                                ValueError
                        if p1_start=="y":
                            x=deck.pop(len(deck)-1)
                            p1+=x
                        while True:
                            try:
                                p2_start=input("\nPlayer 2 would you like to pick a card? y(yes)/n(no)\n").lower()
                                if p2_start=="y":
                                    break
                                elif p2_start=="n":
                                    break
                            except:
                                ValueError
                        if p2_start=="y":
                            y=deck.pop(len(deck)-1)
                            p2+=y
                        if p1_start=="y" and p2_start=="y":
                            print("\nP1 got",x,"points\nP2 got",y,"points\n")
                        elif p1_start=="y":
                            print("\nP1 got",x,"points\n")
                        elif p2_start=="y":
                            print("\nP2 got",y,"points\n")
                        elif p1_start=="n" and p2_start=="n":
                            end=input("Whould you like to end the game? y(yes)/n(no)\n").lower()
                            if end=="y":
                                print("\nP1's score",p1,"\nP2's score",p2,"\n\nDraw!")
                                draws+=1
                                break
                            elif end=="n":
                                continue
                        if p1>20 and p2>20:
                            prit("\nP1's score",p1,"\nP2's score",p2,"\n\nDraw!")
                            draws+=1
                            break
                        elif p1==21:
                            print("\nP1's score",p1,"\nP2's score",p2,"\n\nP1 Won!")
                            r1+=1
                            break
                        elif p2==21:
                            print("\nP1's score",p1,"\nP2's score",p2,"\n\nP2 Won!")
                            r2+=1
                            break
                        elif p1>21:
                            print("\nP1's score",p1,"\nP2's score",p2,"\n\nP2 Won!")
                            r2+=1
                            break
                        elif p2>21:
                            print("\nP1's score",p1,"\nP2's score",p2,"\n\nP1 Won!")
                            r1+=1
                            break
                    except:
                        ValueError
            elif mode==3:
                print("\nPlayer 1 wins:",r1,"\nPlayer 2 wins:",r2,"\nDraws:",draws,"\n")
                continue
            elif mode==4:
                print(txt.center(110))
                print("Your goal to get 21 points. Everytime you take card you get some points (you can get only 2 ,3, 4, 6, 7, 8, 9, 10 or 11) only by your luck. If you get more or less than 21 you lose.\n Good Luck!")
            elif mode==5:
                break
        except:
            ValueError
    break
