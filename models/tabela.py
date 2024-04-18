import csv

class Tabela:
    def escrever_csv(respostas):
      try:
        with open('respostas.csv', 'w', newline='', encoding='utf-8') as file:
          gravar = csv.writer(file, dialect='excel')
          gravar.writerow(['Data e Hora', 'Idade', 'Genero', 'Pergunta 1', 'Pergunta 2', 'Pergunta 3', 'Pergunta 4', 'Pergunta 5', 'Pergunta 6'])
          for resposta in respostas:
             gravar.writerow([resposta.data, resposta.idade, resposta.genero] + resposta.respostas)
      except csv.Error as e:
         print(f'Ocorreu um erro ao escrever no arquivo CSV: {str(e)}')
     