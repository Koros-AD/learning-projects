import random
l=[]
n=(int(input("Введите размер списка ")))
def fillin():
  for i in range (n):
   x=random.randint(1,20)
   l.append(x)
fillin()
print(l)

def writein():
    plr1=(input("Player 1 name:"))
    plr2=(input("Player 2 name: "))
    return plr1,plr2
