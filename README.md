# Pesquisa sobre o Mercado Segurador

É um programa em Python que realiza uma pesquisa digital sobre o Mercado Segurador. Os dados dos entrevistados são coletados e armazenados em arquivo .csv, onde serão visualizados em uma planilha.

### Funcionalidade

- Deve ser informado os dados dos entrevistados, como idade e gênero.
- Serão 6 perguntas, podendo ser respondias com 1-Sim, 2-Não ou 3-Não sei responder.
- O armazenamento dos dados são coletados para o arquivo .csv para análises futuras pelo Excel.

### Como usar

- Verifique se tem o Python instalado em sua máquina. Você pode baixá-lo em [python.org](https://www.python.org/)
- Baixe o projeto em sua máquina e o inicie
- Execute o script no arquivo index.py
- Siga as instruções no terminal para inserir os dados da pesquisa
- Para encerrar, digite '00' quando solicitado a idade
- Confira os dados digitados na planilha

### Squad

- Pessoa Co-facilitadora: Wash
- Pessoa Gestora de Conhecimento: Eloise
- Pessoa Gestora de Gente e Engajamento: Gabriela
- Pessoa Colaboradora I: Isadora
- Pessoa Colaboradora II: João Guilherme

## Detalhes do Projeto

Sua equipe recebeu uma nova solicitação de projeto! Dessa vez para desenvolver uma pesquisa digital com a população de várias cidades do Brasil. Para isso, será necessário armazenar os dados dessa pesquisa em um arquivo .csv para utilização em análises futuras. A pesquisa será feita a partir de um levantamento ativo, realizado pelos funcionários da empresa que irão sair com o projeto nas ruas para coletar as respostas.

Você e seu squad devem desenvolver um projeto capaz de armazenar dados recolhidos na pesquisa em um documento csv.
As perguntas para essa pesquisa (assim como o tema dela) devem ser definidas pelo grupo.

Como fazer: 

- A pesquisa que será realizada deve conter 4 perguntas (o grupo pode decidir o tema e formular as questões) que podem ser respondidas com Sim (1), Não (2), Não sei responder (3).
- Para iniciar o questionário, será solicitado ao usuário que informe a sua idade e gênero. Cada linha do nosso arquivo .csv deve conter: idade, gênero, resposta_1, resposta_2, resposta_3, resposta_4, data e hora da resposta.
- O projeto deve ficar solicitando respostas em um laço de repetição que fica inserindo as respostas informadas nas linhas do .csv até que a idade de 00 seja informada; então, podemos ficar inserindo novas respostas por quanto tempo for necessário (quando a idade 00 é informada o projeto para de executar).
- Com os dados preenchidos no .csv, o grupo deve realizar uma exibição simples dos resultados utilizando o Excel (com uma simulação de 10 respostas no questionário para gerar os dados). Na apresentação, deverão ser demonstrados o funcionamento do questionário e o exemplo dos dados coletados.
