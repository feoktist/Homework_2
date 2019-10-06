# Pushkin: may 26 1799

p_year = 1799
p_day = 26

print(type(p_year))

year = int(input("Год рождения А.С. Пушкина: "))

while year != p_year:
    print("Неверный год рождения")
    print("Try again!")
    year = int(input("Год рождения Солнца Русской Поэзии? "))

print("Верно!")

print('End of program')
