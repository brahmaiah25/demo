class Multiplication_Table:
    def __init__(self,n):
        self.n=n
    def multiply(self):
        i=1
        while i <= 10:
            print(self.n,'x',i,'=',self.n*i)
            i += 1
        return    

n1=int(input("Enter Table  : "))
table=Multiplication_Table(n1)
table.multiply()

