import sudoku, curses, pickle

try:
    arquivo = open ('save.sv', 'rb+')
    jogo = pickle.load(arquivo)
    arquivo.close()
    
    arquivo = open ('solucao.sv', 'rb+')
    solucao = pickle.load(arquivo)
    arquivo.close()

    
except:
    jogo, solucao = sudoku.inicia_sudoku()
    arquivo = open('save.sv', 'wb+')
    pickle.dump(jogo, arquivo)
    arquivo.close()
    arquivo = open('solucao.sv', 'wb+')
    pickle.dump(solucao, arquivo)
    arquivo.close()

'''
Esta biblioteca trata da aparencia da grade do tabuleiro.
'''

def desenha_sudoku(window, grade, selecao):
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    for lin_grade in range(3):
        for col_grade in range(3):
            regiao = grade[lin_grade][col_grade]
            for lin_regiao in range(3):
                for col_regiao in range(3):
                    posicao = (lin_grade*27)+(col_grade*3)+(lin_regiao*9)+col_regiao+1



                    #Formatação na aparencia da grade

                    final1 = 1 #Para formatação rápida da da grade
                    final2 = 2
                    final3 = 0

                    celula = regiao[lin_regiao][col_regiao]

                    a = celula[sudoku.DIGITO]
                    y = 4*(col_grade+1)-4+col_regiao + final1
                    x = 4*(lin_grade+1)-4+lin_regiao + final1




                    if posicao == selecao :
                        
                        window.addstr(x, y, a, curses.color_pair(1))
                        window.refresh()

                        lg = lin_grade
                        lr = lin_regiao
                        cg = col_grade
                        cr = col_regiao


                    if a == grade [lin_grade] [col_grade] [lin_regiao] [col_regiao]['digito'] and grade [lin_grade] [col_grade] [lin_regiao] [col_regiao] ['automatico'] == False and grade [lin_grade] [col_grade] [lin_regiao] [col_regiao] ['digito'] != '.':

                        if posicao == selecao:
                            window.addstr(x, y, a, curses.color_pair(1))
                            window.refresh()
                        else:

                            curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_BLACK)
                            window.addstr(x, y, a, curses.color_pair(2))
                            window.refresh()



                    else:
                        if posicao == selecao:
                            curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
                            window.addstr(x, y, a, curses.color_pair(1))
                            window.refresh()
                        else:
                            window.addstr(x, y, a)
                            window.refresh()


                    if col_regiao == 0:
                        y = 4*(col_grade+1)-4+col_regiao + final3
                        x = 4*(lin_grade+1)-4+lin_regiao + final1
                        b = '|'
                        window.addstr(x, y, b)
                        window.refresh()
                    if col_grade == 2 and col_regiao ==2 :
                        y = 4*(col_grade+1)-4+col_regiao + final2
                        x = 4*(lin_grade+1)-4+lin_regiao + final1
                        b = '|'
                        window.addstr(x, y, b)
                        window.refresh()


                    if lin_regiao == 0:
                        y = 4*(col_grade+1)-4+col_regiao + final3
                        x = 4*(lin_grade+1)-4+lin_regiao + final3
                        b = '--'
                        window.addstr(x, y, b)
                        window.refresh()



                        if lin_regiao == 0 and col_regiao == 0 :
                            y = 4*(col_grade+1)-4+col_regiao + final3
                            x = 4*(lin_grade+1)-4+lin_regiao + final3
                            b = '+'
                            window.addstr(x, y, b)
                            window.refresh()
                        if col_grade == 2 and lin_regiao == 0 and col_regiao == 2 :
                            y = 4*(col_grade+1)-4+col_regiao +final2
                            x = 4*(lin_grade+1)-4+lin_regiao + final3
                            b = '+'
                            window.addstr(x, y, b)
                            window.refresh()
                        #ultima linha
                        if lin_grade == 2:
                            y = 4*(col_grade+1)-4+col_regiao + final3
                            x = 4*(lin_grade+1)-4+lin_regiao + final3 +4
                            b = '--'
                            window.addstr(x, y, b)
                            window.refresh()
                            if lin_grade == 2 and col_grade == 0 and lin_regiao == 0 and col_regiao == 0 :
                                y = 4*(col_grade+1)-4+col_regiao + final3
                                x = 4*(lin_grade+1)-4+lin_regiao + final3 +4
                                b = '+'
                                window.addstr(x, y, b)
                                window.refresh()

                            if lin_grade == 2 and col_grade == 2 and lin_regiao == 0 and col_regiao == 2 :
                                y = 4*(col_grade+1)-4+col_regiao +final2
                                x = 4*(lin_grade+1)-4+lin_regiao + final3 +4
                                b = '+'
                                window.addstr(x, y, b)
                                window.refresh()


    return lg,  lr, cg, cr



#Tratador da lista
def tratador(jogo,key, lg,  lr, cg, cr):
    if jogo [lg][cg][lr][cr]['automatico']== True:
        pass
    elif jogo [lg][cg][lr][cr]['automatico']== False:
        if key == '0':
            key = '.'
        jogo [lg][cg][lr][cr]['digito'] = key
    return jogo


#Primeira rodada do mapa
tela= curses.initscr()

curses.start_color()
curses.noecho()
curses.cbreak()
curses.curs_set(False)

tela.clear()

selecao = 1



window3 = curses.newwin(20,30,0,45)
instrucao = 'Comandos:\n   w \n a   d move o cursor\n   s\n  1-9  entra com um dígito\n  0 . limpa o dígito\n   n   novo jogo\n   z   salva o jogo\n   f   fecha o jogo\n   x   resolve'
window3.addstr(1,1,instrucao)
window3.refresh()

window2 = curses.newwin(30,30,0,0)
instrucao = 'Regras:\n Preencha a grade de forma \n que cada coluna, linha e \n região contenha todos os \n dígitos de 1 a 9.'
window2.addstr(3,1,instrucao)
window2.refresh()

window1 = curses.newwin(14, 13, 0, 30)
desenha_sudoku(window1, jogo, selecao)
window3.refresh()

#Futura rodadas

key = ord ('t')#window1.getch()

while key != 10:

    key = chr(key)

    if key == 'w':
        if (selecao - 9) >= 1:
            selecao -= 9
    elif key == 's':
        if (selecao + 9) <= 81:
            selecao += 9
    elif key == 'a':
        if (selecao - 1) >= 1:
            selecao -= 1
    elif key == 'd':
        if (selecao + 1) <= 81:
            selecao += 1
    elif key in ['0','1','2','3','4','5','6','7','8','9','.']:
        jogo = tratador(jogo,key, lg,  lr, cg, cr)
    elif key == 'n':
        from novo_jogo import novo_jogo
        jogo,solucao = novo_jogo(jogo,solucao)
        
    elif key == 'z':
        from salva_jogo import salva_jogo
        salva_jogo(jogo, solucao)
        
    elif key == 'f':
        from fecha_jogo import fecha_jogo
        resposta = fecha_jogo()
        if resposta in ['s', 'S']:
            break
    elif key == 'x':
        from resolve import resolve
        jogo, solucao = resolve(jogo, solucao)

    lg,  lr, cg, cr = desenha_sudoku(window1, jogo, selecao)
    key = window1.getch()

curses.endwin()
