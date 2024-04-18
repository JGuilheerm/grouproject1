from models.tabela import Tabela
from models.pergunta import Pergunta

def main():
  print(f'''
                      ========================================================   
                        VOCÊ FOI SELECIONADO PARA FAZER PARTE DESTA PESQUISA!
                      ========================================================
''')
  print(f'''
                  ===============================================================      
                  |   Por favor, responda às perguntas a seguir considerando:   |
                  |                                                             |      
                  |                  1 - Sim                                    |
                  |                                                             |
                  |                  2 - Não                                    |  
                  |                                                             |
                  |                  3 - Não sei responder                      |     
                  |                                                             |
                  ===============================================================\n      
        ''')
  respostas = Pergunta.coletar_respostas()  
  Tabela.escrever_csv(respostas)  
  print(f'''\n******Obrigado por participar da pesquisa!******''')
      
if __name__ == "__main__":
    main()