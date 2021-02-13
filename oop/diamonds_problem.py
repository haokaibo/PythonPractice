class A:
    def __init__(self):
        print("A.__init__")

    def m(self):
        print("m of A called")


class B(A):
    def __init__(self):
        super().__init__()
        print("B.__init__")

    def m(self):
        print("m of B called")
        super().m()


class C(A):
    def __init__(self):
        super().__init__()
        print("C.__init__")

    def m(self):
        print("m of C called")
        super().m()


class D(B, C):
    def __init__(self):
        super().__init__()
        print("D.__init__")

    def m(self):
        print("m of D called")
        super().m()


if __name__ == '__main__':
    d = D()
    d.m()
