# Напишите функцию, которая возвращает номер квартал по номеру месяца
# Например: 
# месяц 2 (февраль) является частью первого квартала; 
# месяц 6 (июнь) является частью второго квартала; 
# месяц 11 (ноябрь) является частью четвертого квартала.

def quarter_of(month):
    if month < 1 or month > 12:
        print("Такого месяца нет!")
    elif month > 9:
        print(f"Месяц {month} является частью четвертого квартала")
    elif month > 6:
        print(f"Месяц {month} является частью третьего квартала")
    elif month > 3:
        print(f"Месяц {month} является частью второго квартала")
    else:
        print(f"Месяц {month} является частью первого квартала")

quarter_of(10) #Здесь можно запрашивать число у пользователя, но вроде в условии задачи нужно написать только функцию
    