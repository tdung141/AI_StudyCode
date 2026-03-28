def kiem_tra_chia_het():
    so = int(input('Nhap mot so nguyen duong: '))
    if so <= 0:
        return 'Vui long nhap so nguyen duong!'
    if so % 2 == 0:
        print(f'{so} chia het cho 2')
    if so % 3 == 0:
        print(f'{so} chia het cho 3')
    if so % 2 != 0 and so % 3 != 0:
        print(f'{so} khong chia het cho 2 hay 3')

kiem_tra_chia_het()

import math

def giai_phuong_trinh_bac_2():
    a = float(input('Nhap a: '))
    b = float(input('Nhap b: '))
    c = float(input('Nhap c: '))
    if a == 0:
        return 'a phai khac 0!'
    delta = b**2 - 4*a*c
    if delta < 0:
        return 'Phuong trinh vo nghiem'
    elif delta == 0:
        x = -b / (2*a)
        print(f'Phuong trinh co nghiem kep: x = {x}')
    else:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        print(f'Phuong trinh co 2 nghiem: x1 = {x1}, x2 = {x2}')

giai_phuong_trinh_bac_2()