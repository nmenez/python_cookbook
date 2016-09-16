def Chapter3_1():
    print('3.1 Rounding Numerical Values')
    print('round(1.23, 1) >>>', round(1.23, 1))
    print('round(1.25361, 3) >>>', round(1.25361, 3))
    print('using format')
    x = 1.23456
    print('x = 1.23456')
    print('''format(x, '0.2f') >>>''', format(x, '0.2f')  )
    print(''''value is {:0.3f}'.format(x) >>>''', '{:0.3f}'.format(x))

def Chapter3_2():
    print('3.2 Performing Accurate Decimal Calculations')
    from decimal import Decimal
    print('using Decimal modules sacrifices speed for precision')
    a = Decimal('4.2')
    b = Decimal('2.1')
    print('a + b = ', a+b)
    print('''Decimal('6.3') ==  a+b >>>''', Decimal('6.3') ==  a+b)

def Chapter3_3():
    print('3.3 formatting for output')
    x = 1234.56789
    print('x =', x)
    print('right justified')
    print("format(x, '>10.1f') => ", format(x, '>10.1f'))
    print("format(x, '>9.1f') => ", format(x, '>9.1f'))
    print("format(x, '>8.1f') => ", format(x, '>8.1f'))
    print('left justified')
    print("format(x, '<10.1f') => ", format(x, '<10.1f'))
    print("format(x, '<9.1f') => ", format(x, '<9.1f'))
    print("format(x, '<8.1f') => ", format(x, '<8.1f'))
    print('centered')
    print("format(x, '^10.1f') => ", format(x, '^10.1f'))
    print('inclusion of thousand separator')
    print("format(x, '0,.1f') => ", format(x, '0,.1f'))

def Chapter3_4():
    print('3.4 working with decimal and octal')
    x = 8
    print('x = ', x)
    print('bin(x) =>', bin(x))
    print('oct(x) =>', oct(x))

def Chapter3_5():
    pass

def Chapter3_6():
    print('3.6 Complex Numbers')
    a = complex(3, 4)
    print('a=complex(2,4) =>', a)
    b = 3 - 5j
    print('b= 3- 5j =>', b)
    print('a.real =>', a.real)
    print('a.imag =>', a.imag)
    print('a + b = >', a+b)
    print('a * b = >', a*b)
    print('a / b = >',  a/b)
    print('abs(a) =>', abs(a))

    print(' to do more additional complex-valued functions as sines, cosines, or square roots, use cmath')
    import cmath
    print('cmath.sin(a) =>' , cmath.sin(a))
    print('cmath.cos(a) =>' , cmath.cos(a))
    print('cmath.exp(a) =>', cmath.exp(a))


if __name__ == "__main__":
   #Chapter3_1()
   #Chapter3_2()
   #Chapter3_3()
   #Chapter3_4()
   #Chapter3_5()
   Chapter3_6()