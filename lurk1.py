text=("""
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо -- песнь заводит,
Налево -- сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух... там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
""")
def onesyllable(str):
    sep = {'\n', '!', ':', ',', '-','.', ';', ' '}
    vowels = {'а', 'е','я', 'ё', 'э','ю', 'у', 'о', 'и', 'ы'}
    vowelnumber = 0
    words1 = ''
    words2 = set()
    for char in str:
        lowercase= char.lower()
        if lowercase in sep:
            if len(words1) > 0:
                if vowelnumber == 1:
                    words2.add(words1)
                vowelnumber = 0
                words1 = ''
        else:
            if lowercase in vowels:
                vowelnumber += 1
            words1 += lowercase
    return words2
print(onesyllable(text))



