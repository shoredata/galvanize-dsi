class LinearPolynomial:
    def __init__(self,m,b):
        self.mym = m
        self.myb = b

    def __str__(self):
        if self.myb> 0:
            return str(self.mym) + 'x+' + str(self.myb)
        else:
            return str(self.mym) + 'x' + str(self.myb)

    def evaluate(self,x):
        return self.mym * x + self.myb

    def __add__(self, other):
        return LinearPolynomial(self.mym + other.mym, self.myb + other.myb)

    def __sub__(self, other):
        return LinearPolynomial(self.mym - other.mym, self.myb - other.myb)
