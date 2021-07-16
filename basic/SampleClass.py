##############################
#1 simple class 
##############################
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



##############################
#2 constructor and destructor sample 1
##############################
# class CalcClass:
#     def __init__(self):
#         print( "called constructor.." )
#         self.i = 100
#         self.j = 1

#     def __del__(self):
#         print( "called destructor.." )

#     def AddNumbers(self): #addition
#         return self.i + self.j


# calc = CalcClass()
# print( calc.AddNumbers() )


##############################
#3 constructor and destructor sample 2
##############################
# class CalcClass:
#     def __init__(self, i, j):
#         print( "called constructor.." )
#         self.i = i
#         self.j = j

#     def __del__(self):
#         print( "called destructor.." )

#     def AddNumbers(self): #addition
#         return self.i + self.j

#     def SubNumbers(self): #subtraction
#         return self.i - self.j        

#     def MulNumbers(self): #Multiplication 
#         return self.i * self.j

#     def DivNumbers(self): #division 
#         return self.i / self.j

# calc = CalcClass(10, 5)
# print( calc.AddNumbers() )
# print( calc.SubNumbers() )
# print( calc.MulNumbers() )
# print( calc.DivNumbers() )

# print("---------")

# calc2 = CalcClass(12, 3)
# print( calc2.AddNumbers() )
# print( calc2.SubNumbers() )
# print( calc2.MulNumbers() )
# print( calc2.DivNumbers() )

