'''
Por Nitai Charan | Clovison G | Fabiano Antero
Arquivo principal
'''

from mapa import mapa
from naobug import le_opcao

sair = False


while not sair:


    # Requisito 7
    if mapa() == 'f':
        # O retorno da sub-função 'mapa' deve retornará
        confir = le_opcao ('Deseja realmente sair do jogo?(S/N): ', ['S', 'N'])
        # A variável 'confir' entra com os parámetros necessários mas sai com o retorno do le_opcao
        if confir == 'S':
            sair = True
        else:
            pass
