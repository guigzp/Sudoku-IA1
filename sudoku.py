import random

class Sudoku:
    def __init__(self,n):
        self.n = n
        self.tabuleiro = []
        self.preenchidos = 0
        self.feitos = []

    def teste(self):
        '''
        self.tabuleiro.append([5,3,0,0,7,0,0,0,0])
        self.tabuleiro.append([6,0,0,1,9,5,0,0,0])
        self.tabuleiro.append([0,9,8,0,0,0,0,6,0])
        self.tabuleiro.append([8,0,0,0,6,0,0,0,3])
        self.tabuleiro.append([4,0,0,8,0,3,0,0,1])
        self.tabuleiro.append([7,0,0,0,2,0,0,0,6])
        self.tabuleiro.append([0,6,0,0,0,0,2,8,0])
        self.tabuleiro.append([0,0,0,4,1,9,0,0,5])
        self.tabuleiro.append([0,0,0,0,8,0,0,7,9])
        ''' 
        self.tabuleiro.append([0,2,0,0,0,5,0,0,0])
        self.tabuleiro.append([0,1,5,0,0,0,0,0,0])
        self.tabuleiro.append([0,0,0,0,0,8,7,0,3])
        self.tabuleiro.append([0,5,1,0,0,0,0,0,0])
        self.tabuleiro.append([0,0,9,7,0,0,0,1,0])
        self.tabuleiro.append([0,0,0,3,0,0,0,4,6])
        self.tabuleiro.append([0,0,0,0,8,0,0,0,1])
        self.tabuleiro.append([7,0,0,9,3,0,0,6,0])
        self.tabuleiro.append([0,0,0,0,0,0,4,0,8])
        for i in range(9):
            for j in range(9):
                if self.tabuleiro[i][j] != 0:
                    self.preenchidos += 1

    def valorLinhaColuna(self, celula, valor):
        for x in self.tabuleiro[celula[0]]:
            if x == valor:
                return True
        for x in range(self.n ** 2):
            if self.tabuleiro[x][celula[1]] == valor:
                return True
        return False

    def valorBloco(self, celula, valor):
        linhaInicial = celula[0] - (celula[0] % self.n)
        colunaInicial = celula[1] - (celula[1] % self.n)
        for i in range(linhaInicial, linhaInicial + self.n):
            for j in range(colunaInicial, colunaInicial + self.n):
                if self.tabuleiro[i][j] == valor:
                    return True
        return False

    def podeInserir(self, celula, valor):
        if(self.valorLinhaColuna(celula,valor) or self.valorBloco(celula,valor)):
            return False
        return True

    def valoresCelula(self, celula):
        aux = [1,2,3,4,5,6,7,8,9]
        for x in range(1,10):
            if self.valorLinhaColuna(celula, x) or self.valorBloco(celula, x):
                aux.remove(x)
        return aux

    def proximaCelula(self):
        menorValor = 9
        listaMenores = []
        for i in range(9):
            for j in range(9):
                if self.tabuleiro[i][j] == 0:
                    qtd = len(self.valoresCelula((i,j)))
                    if qtd == 0:
                        return False
                    if qtd < menorValor:
                        menorValor = qtd
                        listaMenores.clear()
                        listaMenores.append((i,j))
                    elif qtd == menorValor:
                        listaMenores.append((i,j))
        if len(listaMenores) == 0:
            return False
        aux = random.randint(0, len(listaMenores) -1)
        return listaMenores[aux]
