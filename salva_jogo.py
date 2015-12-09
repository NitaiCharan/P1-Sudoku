import curses
import pickle
def salva_jogo(jogo, solucao):
    menssagem = 'Você deseja salvar o jogo? (S/N) '
    curses.cbreak()
    curses.echo()
    windowt = curses.newwin(2,100,15,0)
    windowt.addstr(1,1,menssagem)
    resposta = windowt.getch()
    resposta = chr (resposta)
    windowt.refresh()

    if resposta in ['s', 'S']:
        arquivo = open ('save.sv', 'wb+')
        pickle.dump(jogo, arquivo)
        arquivo.close()

        arquivo = open ('solucao.sv', 'wb+')
        pickle.dump(solucao, arquivo)
        arquivo.close()
    else:
        pass
