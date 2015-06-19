

class PrimeFinder:

    def __init__(self):
       self. primeArr = []
       self.rangeArr = []
       self.largest = -1

    def set_largest(self, val):
        self.largest =  val

    def get_largest(self):
        return self.largest
    
    def set_rangeArr(self):
        for num in range(self.get_largest()):
            self.rangeArr.append(num + 1)
    
    def get_rangeArr(self):
        return self.rangeArr

    def set_primeArr(self):
        for num in self.get_rangeArr():
            if self.check_prime(num):
                self.primeArr.append(num)

    def get_primeArr(self):
        return self.primeArr

    def check_prime(self,num):
        if num > 1:
            if self.check_two(num):
                return False
            elif self.check_three(num):
                return False
            elif self.check_five(num):
                return False
            else:
                return self.check_factorial(num)

    @staticmethod
    def check_two(num):
        if num == 2:
            return False
        elif num % 2 == 0:
            return True
        else: 
            return False
            
    @staticmethod
    def check_three(num):
        if num == 3:
            return False
        elif num % 3 == 0:
            return True
        else: 
            return False
    
    @staticmethod
    def check_five(num):
        if num == 5:
            return False
        elif num % 5 == 0:
            return True
        else:
            return False
    @staticmethod
    def check_factorial(num):
        for n in range(5, int(num ** 0.5) + 1, 6):
            #print(str(num) + "%" + str(n) + "=" + str(num % n))
            #print(str(num) + "%" + str(n+2) + "=" + str(num % (n + 2)))
            if num % n == 0 or num % (n + 2) == 0:
                return False
        return True
    
    def is_palindrome(self):
        #start at largest and work backwards
        i = len(self.get_primeArr())


pf = PrimeFinder()
pf.set_largest(40)
pf.set_rangeArr()
pfr = pf.get_rangeArr()
pf.set_primeArr()
#pfpa = pf.get_primeArr()
#print(pfpa)
#print(pf.is_palindrome())


