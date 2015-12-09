import curses
def limpa_digito(jogo):

    menssagem = 'Deseja limpar jogo? (S/N): '
        
    curses.cbreak()
    curses.echo()
    windowt = curses.newwin(2,100,15,0)
    windowt.addstr(1,1,menssagem)
    resposta = windowt.getch()
    resposta = chr (resposta)
    windowt.refresh()
    
    if resposta in ['s', 'S']:
        
        for lin_grade in range(3):
            for col_grade in range(3):
                for lin_regiao in range(3):
                    for col_regiao in range(3):
                        if jogo[lin_grade][col_grade][lin_regiao][col_regiao] ['automatico'] == False:
                            jogo[lin_grade][col_grade][lin_regiao][col_regiao]['digito'] = '.'
                        else:
                            pass
    else:
        pass
