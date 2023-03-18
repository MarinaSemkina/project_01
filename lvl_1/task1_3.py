# Задача 1.3.

# Напишите скрипт, который принимает от пользователя номер месяца, 
# а возвращает количество дней в нем.
# Результат проверки вывести на консоль
# Допущение: в феврале 28 дней
# Если номер месяца некорректен - сообщить об этом
mounth = [["Январь" , 31], ["Февраль" , 28], ["Март" , 31], ["Апрель" , 30], 
          ["Май" , 31], ["Июнь" , 30], ["Июль" , 31], ["Август" , 31], 
          ["Сентябрь" , 30], ["Октябрь" , 31], ["Ноябрь" , 30], ["Декабрь" , 31]]

m = int(input("Введите номер месяца: ")) - 1
if m > 12 or m < 0:
    print("Такого месяца нет!")
else:
    print(f"Вы ввели {mounth[m][0]}. {mounth[m][1]}  дней ")


# Например,
    # Введите номер месяца: 3
    # Вы ввели март. 31 дней

    # Введите номер месяца: 2
    # Вы ввели февраль. 28 дней

    # Введите номер месяца: 15
    # Такого месяца нет!
    