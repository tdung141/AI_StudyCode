from math import gcd

class PhanSo:
    def __init__(self, tu, mau):
        if mau == 0:
            raise ValueError("Mẫu số không được bằng 0")
        self.tu = tu
        self.mau = mau
        self.rut_gon()

    def rut_gon(self):
        ucln = gcd(self.tu, self.mau)
        self.tu //= ucln
        self.mau //= ucln
        if self.mau < 0:
            self.tu *= -1
            self.mau *= -1

    def __add__(self, other):
        return PhanSo(self.tu * other.mau + other.tu * self.mau, self.mau * other.mau)

    def __sub__(self, other):
        return PhanSo(self.tu * other.mau - other.tu * self.mau, self.mau * other.mau)

    def __mul__(self, other):
        return PhanSo(self.tu * other.tu, self.mau * other.mau)

    def __truediv__(self, other):
        if other.tu == 0:
            raise ValueError("Không thể chia cho phân số có tử = 0")
        return PhanSo(self.tu * other.mau, self.mau * other.tu)

    def __str__(self):
        return f"{self.tu}/{self.mau}"
