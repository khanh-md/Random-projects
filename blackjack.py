import random

# Making a singular card
class Card:
    suitName= [str(chr(0x2660)), str(chr(0x2665)), str(chr(0x2666)), str(chr(0x2663))]
    rankName= ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

    def __init__(self, suit=0, rank=0):
        self.suit= suit
        self.rank= rank

    def __repr__(self):
        return self.rankName[self.rank]+ self.suitName[self.suit]


class Deck:
    def __init__(self):
        self.hand= []
        self.cards = []
        # append cards into an empty list to make a deck of card
        for suits in range(4):
            for ranks in range(13):
                card= Card(suits, ranks)
                self.cards.append(card)

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        # making a starting hand of 2 random cards for player
        self.shuffle()
        Card1= random.choice(self.cards)
        Card2= random.choice(self.cards)
        self.hand.append(Card1)
        self.hand.append(Card2)
        return self.hand

    def total(self):
        total=0
        for n in self.hand:
            if n.rank>=10:
                total+=10
            elif n.rank==0:
                if total>=11:
                    total+=1
                else:
                    total+=11
            else:
                total+=int(n.rank)+1
        return total


class Player:
    def __init__(self):
        self.d = Deck()
        self.d.deal()
        self.cards1= self.d.hand

    def hit(self):
        hit= random.choice(self.d.cards)
        self.cards1.append(hit)
        print(self.cards1)
        

class Dealer:
    def __init__(self):
        self.d2 = Deck()
        self.d2.deal()
        self.cards2 = self.d2.hand

    def hit(self):
        hit2= random.choice(self.d2.cards)
        self.cards2.append(hit2)

    def payment(self):
        while self.d2.total() <17:
            print("Dealer takes a hit")
            self.hit()
            print("Dealer's hand is: "+ str(self.cards2)+
                  " Dealer's cards totally worth: "+str(self.d2.total()))

class Chips:
    def __init__(self, total=100):
        self.total= total

    def takeBet(self):
        self.bet =input("How much do you want to bet? ")

        if int(self.bet) > self.total:
            print("You don't have enough chips, you currently have: " + str(self.total))
            self.takeBet()

    def winBet(self):
        self.total += int(self.bet)

    def loseBet(self):
        self.total -= int(self.bet)
        

class Game:
    def __init__(self,player1, player2):
        self.check= True
        if player1 =='player':
            self.player = Player()
        if player2 == 'dealer':
            self.dealer = Dealer()

    def compare(self): #comparation of two cards
        if self.player.d.total() > self.dealer.d2.total():
            self.win()
        elif self.player.d.total() == self.dealer.d2.total():
            print("It's a tie")
            self.check= False
            return
        else:
            self.loss()
            return

    def win(self):
        s.score1 +=1
        chips.winBet()
        print("You wins")
        self.check= False
        return

    def loss(self):
        s.score2 +=1
        chips.loseBet()
        print("Dealer wins")
        self.check= False
        return

    def bustCheck1(self):
        if self.player.d.total() > 21:
            self.loss()
            print("You bust yourself")
        else:
            return

    def blackJack1(self):
        if self.player.d.total() == 21:
            self.win()
            print("and with a black jack!!")
            return

    def bustCheck2(self):
        if self.dealer.d2.total() > 21:
            self.win()
            print("Dealer busts himself")
        else:
            return

    def blackJack2(self):
        if self.dealer.d2.total() == 21:
            self.loss()
            print("and with a black jack")
            return

    def getScore(self):
        return print("The player win "+str(s.score1)+" round(s), and lose "+str(s.score2) + " round(s)")

    def getMoney(self):
        if chips.total == 0:
            print("The player have no more chip to play.")
        else:
            return print("The player have " +str(chips.total)+" chips left.")

    def game(self):
        #starting of game
        print(self.player.cards1)
        chips.takeBet()
        self.blackJack1()
        if self.check == False:
            self.getScore()
            self.getMoney()
            return

        #hits?
        while self.player.d.total() < 21:
            x = input("Current card in your hand is "+str(self.player.cards1)+" and totally worth "
                      +str(self.player.d.total())+". Do you want to hit or stand (h/s)? ")
            
            if x == "h":
                self.player.hit()
                self.blackJack1()
                self.bustCheck1()
                if self.check == False:
                    self.getScore()
                    self.getMoney()
                    return
            else:
                print("\n")
                break

        #dealer turn
        print("Dealer's hand is: "+ str(self.dealer.cards2))
        self.dealer.payment()
        self.blackJack2()
        self.bustCheck2()

        if self.check == False:
            self.getScore()
            self.getMoney()
            return

        #compare and done
        self.compare()
        self.getScore()
        self.getMoney()
       
class Score:
    def __init__(self):
        self.score1 = 0
        self.score2 = 0

chips = Chips()
s = Score()
g = Game('player', 'dealer')
print("Let's play Blackjack!" + "\n")
g.game()

while True:
    if chips.total == 0:
        break
    else:
        rep=input('\nagain? y/n: ')
        if rep=='y':
            g = Game('player', 'dealer')
            g.game()
        else:
            break

if __name__ == '__main__':
    main()
