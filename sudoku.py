import random

class Sudoku:
    def __init__(self,n):
        self.n = n
        self.tabuleiro = []
        self.preenchidos = 0
        self.feitos = []

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

    def valoresCelula(self, celula):
        aux = [x for x in range(1, self.n **2 + 1)]
        for x in range(1, self.n ** 2 + 1):
            if self.valorLinhaColuna(celula, x) or self.valorBloco(celula, x):
                aux.remove(x)
        return aux

    def proximaCelula(self):
        menorValor = self.n ** 2
        listaMenores = []
        for i in range(self.n ** 2):
            for j in range(self.n ** 2):
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
        aux = random.randint(0, len(listaMenores) -1)
        return listaMenores[aux]
