"""
 Coury Richards
 CodeEval
 For some fun
 22JUN2015
"""
class PrimeFinder:

    def __init__(self):
       self. primeArr = []
       self.rangeArr = []
       self.largest = -1
    
    #Start Getters/Setters
    
    def get_num(self, i):
        return primeArr[i]

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
    
    #End Getters/Setters

    def check_prime(self,num):
        #0 and 1 are not prime
        if num > 1:
            #Check all the other exceptions
            if self.check_two(num):
                return False
            elif self.check_three(num):
                return False
            elif self.check_five(num):
                return False
            #Check all the numbers ractorials
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
        #Checks the range of factorial for this number
        #If divisible by one then not prime
        for n in range(5, int(num ** 0.5) + 1, 6):
            #These are for troubleshooting
            #print(str(num) + "%" + str(n) + "=" + str(num % n))
            #print(str(num) + "%" + str(n+2) + "=" + str(num % (n + 2)))
            if num % n == 0 or num % (n + 2) == 0:
                return False
        return True
    
class Palindrom:

    def __init__(self, palArr):
        self.palArr = palArr

    def set_palArr(self, palArr):
        self.palArr = palArr

    def get_palArr(self):
        return self.palArr

    def is_palindrome(self):
        #Will check all conditions
        for item in self.palArr: 
            if not type(item) == 'string':
                item = str(item)
            #Incase it is not a string
            fP = 0
            eP = len(item)-1
            for c in item:
                if not fP == eP:
                    if not item[fP] == item[eP]:
                        return False
                    else:
                        fP += 1
                        eP -= 1
                else:
                    return False
            return True
                

"""
pf = PrimeFinder()
pf.set_largest(40)
pf.set_rangeArr()
pfr = pf.get_rangeArr()
pf.set_primeArr()
pfpa = pf.get_primeArr()
print(pfpa)
print(pf.is_palindrome())
"""

a = [1041]

p = Palindrom(a)
print(p.is_palindrome())

