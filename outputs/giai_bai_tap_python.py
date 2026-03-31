def bai_1():
    product = 1
    for i in range(1, 11):
        product *= i
    print('Tích của 10 số tự nhiên đầu tiên là:', product)


def bai_2():
    n = int(input('Nhập vào số nguyên dương n: '))
    if n < 0:
        print('Vui lòng nhập số nguyên dương!')
        return
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    print(f'{n}! =', factorial)


def bai_3():
    n = int(input('Nhập vào số nguyên dương n: '))
    if n < 2:
        print('Không phải số nguyên tố.')
        return
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            print('Không phải số nguyên tố.')
            return
    print('Đây là số nguyên tố.')


def bai_4():
    n = int(input('Nhập vào số nguyên n: '))
    total = sum(i for i in range(n) if i % 2 == 0)
    print('Tổng các số chẵn nhỏ hơn', n, 'là:', total)


bai_1()
bai_2()
bai_3()
bai_4()