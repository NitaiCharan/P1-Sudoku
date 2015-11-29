'''
Biblioteca para criação da grade do tabuleiro.
'''


def mapa ():

    from sudoku0 import inicia_sudoku

    grade, solucao = inicia_sudoku()
    for lin_grade in range (3):
        for col_grade in range(3):
            junta_linha = ''
            for lin_regiao in range (3):
                junta_celulas = ''
                for col_regiao in range (3):
                    junta_celulas += grade [lin_grade] [col_grade] [lin_regiao] [col_regiao] ['digito'] + ' '
                junta_linha += junta_celulas + '| '
            print(junta_linha)
            if (col_grade + 1) % 3 == 0:
                print ('-----------------------')
    return grade, solucao