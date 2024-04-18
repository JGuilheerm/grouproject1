from datetime import datetime
from models.dados import Dados

class Pergunta:
    def coletar_respostas():
        respostas = []
        while True:
            try:
                idade = int(input("\nInforme sua idade (digite 00 para encerrar):\n "))
                if idade < 0:
                    print("Idade não pode ser negativa. Por favor, tente novamente.")
                    continue
                elif idade == 00:
                    break
                
                while True:
                        genero = input("\nInforme seu gênero (M/F):\n ").upper()
                        if genero not in ['M', 'F']:
                            print("Gênero deve ser 'M' para masculino ou 'F' para feminino. Por favor, tente novamente.")
                        else:
                            break
