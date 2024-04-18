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
                
                perguntas = [
                    "\n1 - Você possui algum tipo de seguro atualmente?\n ",
                    "\n2 - Você está ciente das diversas modalidades de seguros disponíveis no mercado?\n ",
                    "\n3 - Você considera o seguro um investimento importante?\n ",
                    "\n4 - Você acredita que um seguro oferece um bom custo-benefício?\n ",
                    "\n5 - Você está familiarizado com o conceito de apólice de seguros?\n ",
                    "\n6- Você gostaria de receber informações sobre seguros?\n "
                ]
                
                respostas_perguntas = []
                for pergunta in perguntas:
                    while True:
                        try:
                            resposta = int(input(pergunta))
                            if resposta in [1, 2, 3]:
                                respostas_perguntas.append(resposta)
                                break
                            else:
                                print("Resposta inválida. Por favor, insira 1 para Sim, 2 para Não ou 3 para Não sei.")
                        except ValueError:
                            print("Entrada inválida. Por favor, insira um número.")
                
                data_e_hora= datetime.now()
                data = data_e_hora.strftime("%d/%m/%Y %H:%M")
                resposta = Dados(idade, genero, respostas_perguntas, data)
                respostas.append(resposta)
                
            except ValueError:
                print("Entrada inválida. Por favor, insira um número para a idade.")
                continue

        return respostas