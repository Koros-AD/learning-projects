mail=input("type email ")
def email(str):
    x=mail.count('@')
    v=mail.count('.')
    if x==1 and v==1:
        print("valid email")
    elif x==0 or v==0:
        print("invalid email")
email(str)
