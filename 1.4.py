n=(int(input('Ввдедите сумму')))
banknotes=[1, 2, 4, 8, 16, 32 ,64]
c = 128
while 1 <= (c := c // 2):
    x, n = divmod(n,c)
    if x > 0:
        print(c, x)
