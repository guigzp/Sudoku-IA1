from sudoku import *

def resolveSudoku(sudoku, celula = None):   
    if sudoku.preenchidos == sudoku.n ** 4:
        return True
    if celula == None:
        celula = sudoku.proximaCelula()
    valoresCelula = sudoku.valoresCelula(celula)
    for x in valoresCelula:
        sudoku.tabuleiro[celula[0]][celula[1]] = x
        sudoku.preenchidos += 1
        if sudoku.preenchidos == sudoku.n ** 4:
            return True
        proximaCelula = sudoku.proximaCelula()
        if proximaCelula != False:
            if(resolveSudoku(sudoku, proximaCelula)):
                return True
        sudoku.tabuleiro[celula[0]][celula[1]] = 0
        sudoku.preenchidos -= 1
    return False


def geraSudoku(sudoku):
    indice = random.randint(0, 2365)
    arquivo = open("tabuleiros.txt", "r")
    linhas = arquivo.readlines()
    linha = linhas[indice].rstrip("\n\r")
    aux = []
    cont = 0
    for i in linha:
        cont += 1
        if i == '.':
            aux.append(0)
        else:
            aux.append(int(i))
            sudoku.preenchidos += 1
        if cont == 9:
            cont = 0
            sudoku.tabuleiro.append(aux.copy())
            aux.clear()
    for i in range(sudoku.n **2):
        for j in range(sudoku.n **2):
            if sudoku.tabuleiro[i][j] != 0:
                sudoku.feitos.append((i,j))
        
def geraSaidaHtml(sudoku):
        linha = 0
        saida = open("sudoku.html", "w")
        saida.write('<style>table { border-collapse: collapse; margin: auto; font-family: Calibri, sans-serif; } colgroup, tbody { border: solid medium; } td { border: solid thin; height: 1.4em; width: 1.4em; text-align: center; padding: 0;  } .cinza {background-color: #d3d3d3 }</style>')
        saida.write('<table>')
        for i in range(sudoku.n):
            saida.write('<colgroup>')
            for j in range(sudoku.n):
                saida.write('<col>')
        for i in range(sudoku.n):
            saida.write('<tbody>')
            for j in range(sudoku.n):
                saida.write('<tr>')
                for x in range(sudoku.n **2):
                    if (linha, x ) in sudoku.feitos:
                        saida.write('<td class="cinza">' + str(sudoku.tabuleiro[linha][x]))
                    else:
                        saida.write('<td>' + str(sudoku.tabuleiro[linha][x]))
                linha += 1

        saida.write('</table>')
        saida.close()

sdk = Sudoku(3)
geraSudoku(sdk)
resolveSudoku(sdk)
geraSaidaHtml(sdk)