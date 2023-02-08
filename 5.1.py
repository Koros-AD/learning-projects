def find():
   word=input("введите слово ")
   word_s=word.lower()
   char=input("введите букву ")
   charx=char.lower()
   x=word_s.count(charx)
   print(f'Буква {char} встречается в слове {x} раз')
find()