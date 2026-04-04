def tong_hai_so(a, b):
    return a + b

def tong_cac_so(*args):
    return sum(args)


def kiem_tra_so_nguyen_to(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def tim_so_nguyen_to(a, b):
    return [x for x in range(a, b + 1) if kiem_tra_so_nguyen_to(x)]


def kiem_tra_so_hoan_hao(n):
    return n == sum(i for i in range(1, n) if n % i == 0)


def tim_so_hoan_hao(a, b):
    return [x for x in range(a, b + 1) if kiem_tra_so_hoan_hao(x)]


def menu():
    while True:
        print('\nMenu:')
        print('1. Tính tổng 2 số')
        print('2. Tính tổng các số')
        print('3. Kiểm tra số nguyên tố')
        print('4. Tìm số nguyên tố trong khoảng')
        print('5. Kiểm tra số hoàn hảo')
        print('6. Tìm số hoàn hảo trong khoảng')
        print('0. Thoát')
        choice = input('Chọn chức năng: ')

        if choice == '1':
            a = int(input('Nhập số thứ nhất: '))
            b = int(input('Nhập số thứ hai: '))
            print('Tổng:', tong_hai_so(a, b))
        elif choice == '2':
            nums = list(map(int, input('Nhập các số cách nhau bởi dấu phẩy: ').split(',')))
            print('Tổng:', tong_cac_so(*nums))
        elif choice == '3':
            n = int(input('Nhập số cần kiểm tra: '))
            print('Số nguyên tố' if kiem_tra_so_nguyen_to(n) else 'Không phải số nguyên tố')
        elif choice == '4':
            a = int(input('Nhập a: '))
            b = int(input('Nhập b: '))
            print('Các số nguyên tố trong khoảng:', tim_so_nguyen_to(a, b))
        elif choice == '5':
            n = int(input('Nhập số cần kiểm tra: '))
            print('Số hoàn hảo' if kiem_tra_so_hoan_hao(n) else 'Không phải số hoàn hảo')
        elif choice == '6':
            a = int(input('Nhập a: '))
            b = int(input('Nhập b: '))
            print('Các số hoàn hảo trong khoảng:', tim_so_hoan_hao(a, b))
        elif choice == '0':
            break
        else:
            print('Lựa chọn không hợp lệ!')

menu()