def fecha_jogo ():
    
    import curses
    
    menssagem = 'Deseja realmente sair do jogo? (S/N): '
    #################################################
    #Para utilização de confirmação de usuário sera necessário a cópia deste
    #conteudo
    #Lembre-se de colocar a mensagem antes de chamar essa função
    
    curses.cbreak()
    curses.echo()
    windowt = curses.newwin(2,100,15,0)
    windowt.addstr(1,1,menssagem)
    resposta = windowt.getch()
    resposta = chr (resposta)
    windowt.refresh()
    
    ###################################################
    if resposta in ['S', 's']:
        return resposta
    else:
        pass
