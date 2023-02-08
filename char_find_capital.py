char="a"
def find_a(a):
    count=a.count(char)
    return count
x=input("ВВЕДИТЕ ТЕКСТ ")
x=x.lower()
res=find_a(x)
print(res)
def check():
 if res<=4:
    print("Bad str")
 else:
    print('good str')
check()