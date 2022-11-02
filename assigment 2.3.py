
+class Complex:
    def __init__(self,real,img):
        self.real = real
        self.img = img
    def __add__(self,other):
        real=self.real+other.real
        img = self.img+other.img
        return Complex(real,img)
    def __sub__(self,other):
        real=self.real-other.real
        img = self.img-other.img
        return Complex(real,img)
    def __mul__(self,other):
        real=(self.real*other.real)+(self.img*other.img)
        img = (self.img*other.real)-(self.real*other.img)
        return Complex(real,img)
    def __eq__(self , other):
        return self.real == other.real and self.img == other.img
    def __str__(self):
        sign ="+"
        if self.img<0:
            sign=""
        return str(self.real)+sign+str(self.img)+"i"

com1 = Complex(1,7)
com2 = Complex(1,7)
com3 = com1+com2
com4 = com1-com2
com5 = com1*com2
print(com3)
print(com4)
print(com5)
print(com1==com2)