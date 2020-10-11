import sys

def block_restart():
    print('\nперезапустить программу? (если нет, программа закроетеся)')
    ans = input('[д/н] >')
    if ans == 'д':
        print(' ')
    elif ans == 'н':
        sys.exit()
    else:
        print('пожалуйста ответьте - да (д) или нет (н) ')
        block_restart()
  
def block_vivod():
    numbers = []
    while True:
        vod = input('\nвведите число в десятичной системе счисления:')
        if not vod.isnumeric():
            print('\nвы ввели текст вместо числа')
        else:
            break
    while int(vod) > 0:
        print('\n' + str(vod) + '/' + str(syst))
        vod, a = divmod(int(vod), int(syst))
        baza = [ 0 , 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        a = baza[a]
        print(a)
        numbers = [a] + numbers
    print('\nчисло сконвертировано:')
    print(numbers)
    block_restart()

while True:
    syst = input('\nвведите систему счисления в которую вы хотите перевести ваше число:')
    if not syst.isnumeric():
        print('\nвы ввели текст вместо числа')
    elif int(syst) == 1:
        print('\nизвините но поддерживается минимум двоичная система счисления')
    elif int(syst) > 36:
        print('\nизвините но поддерживается максимум тридцатишестиричная система счиления')
    else:
        block_vivod()
