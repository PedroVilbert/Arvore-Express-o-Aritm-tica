import os
os.system('cls')

class No:
    def __init__(self, valor):
        self.valor = valor
        
        self.esq = None
        self.dir = None
        
    def imprime(self): #imprime em ordem
        if self.esq:
            self.esq.imprime()
        print(self.valor, end=' ')
        if self.dir:
            self.dir.imprime()
    
    def calcula(self):
        if self.valor == '+':
            return self.esq.calcula() + self.dir.calcula()
        elif self.valor == '-':
            return self.esq.calcula() - self.dir.calcula()
        elif self.valor == '*':
            return self.esq.calcula() * self.dir.calcula()
        elif self.valor == '/':
            return self.esq.calcula() / self.dir.calcula()
        else:
            return self.valor

raiz = No('+') #nivel zero

#nivel 1
raiz.esq = No('+') 
raiz.dir = No('*')

#nivel 2
raiz.esq.esq = No(5)
raiz.esq.dir = No(2)

raiz.dir.esq = No(4)
raiz.dir.dir = No(3)

raiz.imprime()
print('\nResultado: ', raiz.calcula())