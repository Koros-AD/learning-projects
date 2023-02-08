a =int(input("Enter two numbers  "))
b =int(input())
if b==0:
    print("One of the numbers equals zero")
else:
    c1 = a / b
    c2 = a // b
    c3 = a % b
    print(f"""division results:
          {a} / {b} = {c1}
          {a} // {b} = {c2} 
          {a} % {b} = {c3}""")
