'''
Esta subfunção serve para avaliar a entrada do usuário. Se o usuário
não entrar com os valores pré-selecionados pelo programador nas escolhas
possíveis, o programa volta a mostrar a mensagem de entrada e solicita
novamente a entrada.
'''

# O parámetro 'titulo' é a mensagem a ser exibida para o usuário
# O parámetro 'lista_opcao_validas' será as possibilidades de entradas do usuário
def le_opcao (titulo, lista_opcao_validas):
    
    opcao = ''
    
    while True:
        opcao = input (titulo)
        if opcao in lista_opcao_validas:
            break

    return opcao 
