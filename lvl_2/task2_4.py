# Пункт A.
# Напишите функцию, которая удаляет все восклицательные знаки из заданной строк.
# Например,
# foo("Hi! Hello!") -> "Hi Hello"
# foo("") -> ""
# foo("Oh, no!!!") -> "Oh, no"

def remove_exclamation_marks(s):
    g = s.replace("!","")
    print(g)
    pass
remove_exclamation_marks("Hi! Hello!")


# Пункт B.
# Удалите восклицательный знак из конца строки. 
# remove("Hi!") == "Hi"
# remove("Hi!!!") == "Hi!!"
# remove("!Hi") == "!Hi"

def remove_last_em(s):
    a = s[::-1]
    g = a.replace("!","", 1)
    k = g[::-1]
    print(k)
remove_last_em("!Hi!!!a!!g")       

# Дополнительно

# Пункт С.
# Удалите слова из предложения, если они содержат ровно один восклицательный знак.
# Слова разделены одним пробелом.
# Например,
# remove("Hi!") === ""
# remove("Hi! Hi!") === ""
# remove("Hi! Hi! Hi!") === ""
# remove("Hi Hi! Hi!") === "Hi"
# remove("Hi! !Hi Hi!") === ""
# remove("Hi! Hi!! Hi!") === "Hi!!"
# remove("Hi! !Hi! Hi!") === "!Hi!"

def remove_word_with_one_em(s):
    k = []
    f = s.split(" ")
    for i in f:
        if i.count("!") != 1:
            k.append(i)
    a = " ".join(k)
    print(a)
   
    
remove_word_with_one_em("Hi! Hi!! !Hi Hi! !Hi! Hi! Hi")
