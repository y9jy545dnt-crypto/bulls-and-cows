from random import randint


def startingGame():
    pass

def creatingNumber(computerNumber= ''):
    while len(computerNumber) != 4:
        f = True
        r = str(randint(0, 9))
        for i in computerNumber:
            if r == i:
                f = False
                break
        if f:
            computerNumber += r
    return computerNumber


def calculationBullsAndCows(guessedNumber, computerNumber):
    bulls = 0
    cows = 0
    for i in range(len(guessedNumber)):
        if guessedNumber[i] == computerNumber[i]:
            bulls += 1
        elif guessedNumber[i] in computerNumber and guessedNumber[i] != computerNumber[i]:
            cows += 1
    return bulls, cows

newGameFlag = False

computerNumber = creatingNumber()
print('Найди число, задуманное компьютером! Введи четыре различные цифры')
while True:
    guessedNumber = input()
    if len(guessedNumber) == 4 and len(set(guessedNumber.split(''))) == 4:
        bulls, cows = calculationBullsAndCows(guessedNumber, computerNumber)
        if bulls == 4:
            print('Поздравляю, вы угадали!', 'Хотите сыграть еще?', sep='\n')
        else:
            print(f'Быков: {bulls}, Коров: {cows}', 'Попробуй еще раз! Введи четыре различные цифры', sep='\n')
    else:
        print('Вы ввели  некорректный набор цифр')
