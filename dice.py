import random
x=(input('to roll the dice type \'roll\' '))
dice=0
def randomize():
    dice1=random.randint(1,6)
    dice2=random.randint(1,6)
    dicesum=dice1+dice2
    print(f'you got {dicesum} ({dice1},{dice2})')
def tryhard():
    c=(input('wanna roll again?(y/n) '))
    if c=='y':
       randomize()
       tryhard()
    else:
        print('see you')
if x=='roll':
    randomize()
    tryhard()
else: print('see you')