n= int(input("Введите кол-во задач: "))
k= int(input("Введите время пути до вечеринки в минутах: "))
tasks = 0
time= 240 - k
while time > 0:
    tasks+=1
    time-=tasks*5
    if n== tasks:
        break
if time<0:
    tasks-=1
print(tasks)