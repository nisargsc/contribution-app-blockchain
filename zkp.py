from ast import operator
import random, timeit
from Crypto.Util import number

class zkp:
    def __init__(self, pan_no):
        self.pan = self.getPAN(pan_no)
        self.P = self.genLargePrime(22)
        self.g = self.getGenerator()
        self.r = random.randint(0, self.P - 1)

        self.y = pow(self.g, self.pan, self.P)

        h = pow(self.g, self.r, self.P)
        
        for i in range(3):
            if not self.round(h):
                print("ERRRRROR")
            else:
                print("GG")
        print("VERIFICATION COMPLETE")

    def round(self, h):
        b = random.randint(0,1)
        s = (self.r + b*self.pan) % (self.P - 1)

        LHS = pow(self.g, s, self.P )
        RHS = h * pow(self.y, b, self.P) 
        
        return LHS == RHS

    def __str__(self):
        line = "This is a zkp object created for the PAN number {}, Large Prime: {} and Generator: {}".format(self.pan, self.P, self.g)
        return str(line)

    # def 

    @staticmethod
    def printInfo():
        print("""This is a zkp class object created it will just verify that the user has a password or
something unique like a PAN card in our case which will be hashed and converted to a unique value which
is sent to the server. The original unique value is kept secret and will never reach the server""")

    @staticmethod
    def genLargePrime(n_length = None):
        if not n_length:
            n_length = 1024
        primeNum = number.getPrime(n_length)
        return (primeNum)

    @staticmethod
    def getGenerator(range = 20):
        return random.randint(0, range)

    @staticmethod
    def getPAN(pan):
        ans = 0
        place = 1
        for ch in pan:
            ans += ord(ch)*pow(10,place)
            place+=1
        return ans

    

def __main__():
    start = timeit.default_timer()
    
    obj = zkp("INDHS2918G")
    # print(obj)
    obj.printInfo()
    print('Time: ', timeit.default_timer() - start)  

__main__()