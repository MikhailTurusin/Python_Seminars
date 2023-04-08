# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы
# расплачивались за проезд и получали билет с номером. Счастливым
# билетом называют такой билет с шестизначным номером, где сумма
# первых трех цифр равна сумме последних трех. Т.е. билет с номером
# 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать
# программу, которая проверяет счастливость билета.

# 385916 -> yes
# 123456 -> no

number = int(input("Введите номер билета: "))

if number < 100000 or number > 999999:
    print("Номер билета должен быть шестизначный")
else : 
    number=str(number)
    number1=(int(number[0])+int(number[1])+int(number[2]))
    number2=(int(number[3])+int(number[4])+int(number[5]))
    if number1==number2 : print(f"Билет {number} счастливый -> YES")
    else : print (f"Билет {number} несчастливый -> NO")