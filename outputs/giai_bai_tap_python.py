def bai_1():
    a = int(input('Nhap so nguyen a: '))
    b = int(input('Nhap so nguyen b: '))
    tong = a + b
    print('Tong hai so:', tong)


def bai_2():
    chuoi = input('Nhap chuoi ky tu: ')
    print('Chuoi ky tu:', chuoi)


def bai_3():
    a = int(input('Nhap so nguyen a: '))
    b = int(input('Nhap so nguyen b: '))
    c = int(input('Nhap so nguyen c: '))
    tong = a + b + c
    tich = a * b * c
    print('Tong:', tong)
    print('Tich:', tich)
    hieu_ab = a - b
    hieu_ac = a - c
    hieu_bc = b - c
    print('Hieu a-b:', hieu_ab)
    print('Hieu a-c:', hieu_ac)
    print('Hieu b-c:', hieu_bc)
    if b != 0:
        chia_ab = a // b
        chia_ac = a // c
        chia_bc = b // c
        print('Chia a/b:', chia_ab)
        print('Chia a/c:', chia_ac)
        print('Chia b/c:', chia_bc)
    else:
        print('Khong the chia cho 0')


def bai_4():
    chuoi1 = input('Nhap chuoi 1: ')
    chuoi2 = input('Nhap chuoi 2: ')
    chuoi3 = input('Nhap chuoi 3: ')
    ket_qua = chuoi1 + ' ' + chuoi2 + ' ' + chuoi3
    print('Ket qua:', ket_qua)


def bai_5():
    import math
    R = float(input('Nhap ban kinh R: '))
    CV = 2 * R * math.pi
    DT = math.pi * R * R
    print('Chu vi:', CV)
    print('Dien tich:', DT)


if __name__ == '__main__':
    bai_1()
    bai_2()
    bai_3()
    bai_4()
    bai_5()