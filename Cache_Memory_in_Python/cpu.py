from memory import Memory

class Cpu:
    def __init__(self,L1):
        self.R1=0
        self.R2=0
        self.L1 = L1
    def plus(self, operand1, operand2):
        self.R1, time1 = self.L1.get(operand1)
        self.R2, time2 = self.L1.get(operand2)
        print("(access time) ", round(time1, 2), " , (access time) ", round(time2, 2))
        self.R1 += self.R2
        #print("(register 1) ", self.R1, " + (register 2) ", self.R2, " = (result) ", self.R1 + self.R2)
        return self.R1