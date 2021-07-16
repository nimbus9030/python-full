class CalcClass:
    def AddNumbers(self, i, j): #addition
        return i + j
    
    def SubNumbers(self, i, j): #subtraction
        return i - j        

    def MulNumbers(self, i, j): #Multiplication 
        return i * j

    def DivNumbers(self, i, j): #division 
        return i / j

calc = CalcClass()
print( calc.AddNumbers(1, 2) )