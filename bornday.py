# Pushkin: may 26 1799

p_year = 1799
p_day = 26

print(type(p_year))

year = int(input("Год рождения А.С. Пушкина: "))

if year != p_year:
    print("Неверный год рождения")
else:
    day = int(input("День рождения А.С. Пушкина: "))
    if day == p_day:
        print("Верно!")
    else:
        print("Неверный день рождения")


print('End of program')
