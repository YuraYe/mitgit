from mit import examples
from mit import console

print('===== START =====')
minn = 0
maxx = 11
while True:
    opt = console.input_int('Chose test (0-11): ', 0, 11)

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

    fina = input('Press ENTER to restart...')
    if fina != '':
        break

print('====== END ======')
