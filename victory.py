# YoB:
# Dostoevsky - 1821
# Chekhov - 1860
# Gogol - 1809
# Tolstoy - 1828
# Chernyshevsky - 1828

counter = 0
error = 0

dostoevsky_year = int(1821)
chekhov_year = int(1860)
gogol_year = int(1809)
tolstoy_year = int(1828)
chernyshevsky_year = int(1828)


answer = input("Поиграем в викторину? (y/n)")
if answer == 'n':
    print("до свидания!")
else:
    while answer == 'y':
        print('Угадай год рождения пяти великих писателей')
        year = (int(input('Год рождения Достоевского? ')))
        if year == dostoevsky_year:
            counter += 1
        else:
            error += 1
# --------------------------------------------------
        year = (int(input('Год рождения Чехова? ')))
        if year == chekhov_year:
            counter += 1
        else:
            error += 1
# ---------------------------------------------------
        year = (int(input('Год рождения Гоголя? ')))
        if year == gogol_year:
            counter += 1
        else:
            error += 1
# ---------------------------------------------------
        year = (int(input('Год рождения Толстого? ')))
        if year == tolstoy_year:
            counter += 1
        else:
            error += 1
# ---------------------------------------------------
        year = (int(input('Год рождения Чернышевского? ')))
        if year == chernyshevsky_year:
             counter += 1
        else:
             error += 1
# ---------------------------------------------------

        print("Правильных ответов: ", counter)
        print("Неправильных ответов: ", error)
        print("Процент правильных ответов: ", counter * 100/5)
        print("Процент неправильных ответов: ", error * 100/5)
#-----------------------------------------------------
        counter = 0
        error = 0
        answer = input("Сыграем снова? (y/n): ")

print("End of program")