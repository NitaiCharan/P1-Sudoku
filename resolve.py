import novo_jogo
import curses
def resolve(jogo, solucao):
    errou = False
    if errou == False:
        for lin_grade in range(3):
            if errou == False:
                for col_grade in range(3):
                    if errou == False:
                        for lin_regiao in range(3):
                            if errou == False:
                                for col_regiao in range(3):
                                    if jogo[lin_grade] [col_grade] [lin_regiao] [col_regiao] ["digito"] == solucao [lin_grade] [col_grade] [lin_regiao] [col_regiao] ["digito"]:
                                        pass
                                    else:
                                        errou = True
                                        menssagem = 'Jogo esta errado. Continue tentando que você chega lá!'
                                        curses.cbreak()
                                        curses.noecho()
                                        windowt = curses.newwin(2,100,15,0)
                                        windowt.addstr(1,1,menssagem)
                                        windowt.refresh()
                                        break
                            else:
                                break
                    else:
                        break
            else:
                break
    else:
        pass
    
    if errou == False:
        menssagem = 'Parabéns, você acertou. Aproveite e joge novamente. Precione qualquer tecla'
        curses.cbreak()
        curses.echo()
        windowt = curses.newwin(2,100,15,0)
        windowt.addstr(1,1,menssagem)
        resposta = windowt.getch()
        resposta = chr (resposta)
        windowt.refresh()
        jogo, solucao = novo_jogo.novo_jogo(jogo, solucao)
    return jogo, solucao
