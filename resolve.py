errou = False
import curses
def resolve(jogo, solucao):
    for lin_grade in range(3):
            for col_grade in range(3):
                    for lin_regiao in range(3):
                            for col_regiao in range(3):
                                if jogo[lin_grade] [col_grade] [lin_regiao] [col_regiao] ["digito"] == solucao [lin_grade] [col_grade] [lin_regiao] [col_regiao] ["digito"]:
                                    pass
                                
                                else:
                                    errou == True

                                    menssagem = 'Você é um burro'


                                    
                                    curses.cbreak()
                                    curses.echo()
                                    windowt = curses.newwin(2,100,15,0)
                                    windowt.addstr(1,1,menssagem)
                                    resposta = windowt.getch()
                                    resposta = chr (resposta)
                                    windowt.refresh()
                                    break
                                                                    
    if errou == False:
        
        menssagem = 'Você acertou'

        curses.cbreak()
        curses.echo()
        windowt = curses.newwin(2,100,15,0)
        windowt.addstr(1,1,menssagem)
        resposta = windowt.getch()
        resposta = chr (resposta)
        windowt.refresh()
