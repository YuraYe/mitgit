from mit import examples
from mit import console

print('===== START =====')
minn = 0
maxx = 12
while True:
    opt = console.input_int(f'Chose test ({minn}-{maxx}): ', minn, maxx)

    if opt == 0:
        examples.test0()
    elif opt == 1:
        examples.test1()
    elif opt == 2:
        examples.test2()
    elif opt == 3:
        examples.test3()
    elif opt == 4:
        examples.test4()
    elif opt == 5:
        examples.test5()
    elif opt == 6:
        examples.test6()
    elif opt == 7:
        examples.test7()
    elif opt == 8:
        examples.test8()
    elif opt == 9:
        examples.test9()
    elif opt == 10:
        examples.test10()
    elif opt == 11:
        examples.test11()
    elif opt == 12:
        examples.test12()

    fina = input('Press ENTER to restart...')
    if fina != '':
        break

print('====== END ======')
