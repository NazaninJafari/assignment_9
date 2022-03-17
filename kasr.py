class kasr:
    def __init__(self, s, m):
        self.soorat = s
        self.makhraj = m

    def sum(self, mehman):
        result = kasr(None, None)
        result.soorat = (self.soorat * mehman.makhraj) + (mehman.soorat * self.makhraj)
        result.makhraj = self.makhraj * mehman.makhraj
        return result

    def sub(self , mehman):
        result = kasr(None, None)
        result.soorat = (self.soorat * mehman.makhraj) - (mehman.soorat * self.makhraj)
        result.makhraj = self.makhraj * mehman.makhraj
        return result

    def mul(self, mehman):
        result = kasr(None, None)
        result.soorat = self.soorat * mehman.soorat
        result.makhraj = self.makhraj * mehman.makhraj
        return result

    def div(self , mehman):    
        result = kasr(0 , 0)
        result.soorat = self.soorat * mehman.makhraj
        result.makhraj = self.makhraj * mehman.soorat
        return result

    def show(self):
        print(self.soorat ,'/',self.makhraj)

a = kasr(3,5)
b = kasr(4,3)

c = a.mul(b)
c.show()

d = a.sum(b)
d.show()

e = a.sub(b)
e.show()

f = a.div(b)
f.show()