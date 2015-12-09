def novo_jogo(jogo,solucao):

  import sudoku, curses, pickle


  menssagem='Deseja iniciar novo jogo? (S/N): '
  curses.cbreak()
  curses.echo()
  windowt = curses.newwin(2,100,15,0)
  windowt.addstr(1,1,menssagem)
  resposta = windowt.getch()
  resposta = chr (resposta)
  windowt.refresh()
		
  
  if resposta in ['S', 's']:
    jogo,solucao = sudoku.inicia_sudoku()
      
  else:
      pass
  return jogo,solucao 
