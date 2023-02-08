import random
start=(input("Ready to learn your grade? y/n "))

def graderand():
    mark=random.randint(2,5)
    if mark==2:
        print("неудовлетворительно")
    elif mark == 3:
        print("удовлетворительно")
    elif mark == 4:
        print('хорошо')
    elif mark==5:
        print('отлично')

def tryagain():
    tries=input('wanna try again? (y/n) ')
    if tries=='y':
     graderand()
     tryagain()
    else:
        print('goodbye')

if start =='y':
    graderand()
    tryagain()
else:
    print('goodbye')




