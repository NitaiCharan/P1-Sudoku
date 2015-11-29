'''
Por Nitai Charan | Clovison G | Fabiano Antero
Arquivo principal
'''

from mapa import mapa
from naobug import le_opcao


sair = False


while not sair:
    #variavel para tratamento da escolha desejada do usuário

    grade, solucao = mapa()



    escolha = input ('Escolha: ')

    #Requisito 6
    if escolha == 'z':
        confir = le_opcao ('Deseja realmente salvar o jogo?(S/N): ', ['S', 'N'])
        if confir == 'S':
            arquivo.opon ('gamesave.sex', 'wb')
            arquivo.write (grade)
            arquivo.close()

    # Requisito 7
    if escolha == 'f':
        confir = le_opcao ('Deseja realmente sair do jogo?(S/N): ', ['S', 'N'])
        # A variável 'confir' entra com os parámetros necessários mas sai com o retorno do le_opcao
        if confir == 'S':
            sair = True
        else:
            pass
