class ComplexNumber:
    def __init__(self, real_num, imaginary_num):
        self.complex_num = complex(real_num, imaginary_num)

    def __add__(self, other):
        return self.complex_num + other.complex_num

    def __mul__(self, other):
        return self.complex_num * other.complex_num


a = 8 + 8j
b = 9 - 9j
print(a + b)
print(a * b)
c = ComplexNumber(7, 7)
d = ComplexNumber(1, -1)
print(c.complex_num)
print(d.complex_num)
print(c + d)
print(c * d)
