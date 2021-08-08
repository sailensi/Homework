
while True:
    s = input("Введите число на английском от 1 до 10 (например SIX): ")

    try:
        if s == str('one') or s == str('One') or s == str('ONE'):
            print(1)
        if s == str('two') or s == str('TWO') or s == str('TWO'):
            print (2)
        if s == str('three') or s == str('Three') or s == str('THREE'):
            print(3)
        if s == str('four') or s == str('Four') or s == str('FOUR'):
            print(4)
        if s == str('five') or s == str('Five') or s == str('Five'):
            print(5)
        if s == str('six') or s == str('Six') or s == str('SIX'):
            print(6)
        if s == str('seven') or s == str('Seven') or s == str('SEVEN'):
            print(7)
        if s == str('eight') or s == str('Eight') or s == str('EIGHT'):
            print(8)
        if s == str('nine') or s == str('Nine') or s == str('NINE'):
            print(9)
        if s == str('ten') or s == str('Ten') or s == str('TEN'):
            print(10)
            break
        else:
            print('None')
            break






    except ValueError:
           print('none')
           break

