i=int(input("enter time "))
h=i//3600
x=i-3600*h
m=x//60
s=i-(3600*h+60*m)
print(h,"hours",m,"minitues",s,"sec")



