#Criando um aplicativo de matemática fácil e intuitivo


def mostrar_menu():
    print('====MENU====')
    print('1. calculadora')
    print('2. Tabuada')
    print('3. Jogos')
    print('4. Sair ')
    
    #Segundo menu da aplicação
    
def mostrar_submenu_jogos():
    while True:
        print('====MENU DE JOGOS====')
        print('1. Questões')
        print('2. Raciocínio Rápido')
        print('3. Voltar ao menu principal')
        print('========================')
        
        opcao = input('ESCOLHA UMA OPÇÃO:')
        
        if opcao == '1':
            Questões() # Chama a função Questões
        elif opcao == '2':
            print('Iniciando Raciocínio Rápido...')
        elif opcao == '3':
            print('Voltando ao menu principal...')
            break
        else:
            print('Opção inválida. Tente novamente.')
    
    print('=================')
    
def Questões():
    perguntas = [
        ("Maria tinha 15 balas. Ela deu 5 para seu amigo e depois ganhou mais 8. Quantas balas Maria tem agora?", "18"),
        ("João tem 5 pacotes de cartões. Cada pacote contém 12 cartões. Quantos cartões João tem no total?", "60"),
        ("Um livro custa R$ 45,00. Se você tem um desconto de 20%, quanto você vai pagar pelo livro?", "36"),
        ("Em uma corrida, Maria correu 3 quilômetros no primeiro dia e 5 quilômetros no segundo dia. Se ela aumentar a distância corrida em 2 quilômetros a cada dia, quantos quilômetros ela terá corrido ao final do quarto dia?", "20"),
        ("Um restaurante oferece uma promoção onde você paga R$ 50,00 por uma refeição e ganha um desconto de 10% na próxima refeição. Quanto você pagará pela próxima refeição após aplicar o desconto?", "45"),
        ("Você tem R$ 200,00 e quer comprar um item que custa R$ 125,00. Quanto dinheiro você terá restante após a compra?", "75"),
        ("Uma loja oferece um desconto de 20% em um produto que custa R$ 250,00. Qual é o valor do desconto e qual é o preço final do produto?", "50, 200"),
        ("Se um carro viaja a uma velocidade constante de 90 km/h, quanto tempo levará para percorrer uma distância de 270 km?", "3 horas"),
        ("Você participa de um concurso em que deve responder 12 perguntas. Se cada pergunta vale 10 pontos e você acertou 9 perguntas, qual é a sua pontuação total?", "90"),
        ("Um tanque de água tem capacidade para 500 litros. Se você já preencheu 320 litros, qual é a quantidade de água que ainda pode ser adicionada ao tanque?", "180"),
        ("Se um livro custa R$ 48,00 e você paga com uma nota de R$ 100,00, quanto de troco você deve receber?", "52"),
        ("Em um terreno retangular de 25 metros de comprimento e 10 metros de largura, qual é a área total do terreno?", "250"),
        ("Você compra 3 caixas de frutas, cada uma contendo 8 maçãs. Quantas maçãs você tem no total?", "24"),
        ("Uma receita pede 4 xícaras de farinha para fazer um bolo. Se você quer fazer metade da receita, quantas xícaras de farinha você precisará?", "2"),
        ("Você e dois amigos decidiram dividir uma conta de restaurante de R$ 135,00 igualmente entre vocês. Quanto cada um deve pagar?", "45"),
        ("Uma fábrica produz 1200 peças em 8 horas. Qual é a taxa de produção por hora?", "150 peças por hora"),
        ("Se você investe R$ 200,00 em um fundo que rende 5% ao ano, quanto você terá ao final de um ano, considerando o rendimento simples?", "210"),
        ("Qual é o valor de 15% de R$ 80,00?", "12"),
        ("Você compra um celular por R$ 999,00 e paga em 12 parcelas iguais. Qual é o valor de cada parcela?", "83,25"),
        ("Uma piscina retangular tem 8 metros de comprimento e 6 metros de largura. Se a profundidade da piscina é de 1,5 metros, qual é o volume de água necessário para preenchê-la?", "72"),
        ("Você tem um orçamento de R$ 500,00 para gastar em roupas. Se você comprar uma camisa por R$ 89,00 e um par de calças por R$ 129,00, quanto dinheiro restará?", "282"),
        ("Qual é a diferença entre o quadrado de 15 e o quadrado de 10?", "125"),
        ("Se um ônibus sai de uma cidade A às 14:00 e chega à cidade B às 18:00, qual é a duração total da viagem?", "4 horas"),
        ("Um pacote de 500 gramas de arroz custa R$ 12,00. Qual é o custo por grama de arroz?", "0,024"),
        ("Você tem uma peça de roupa que custa R$ 120,00 e está com um desconto de 30%. Qual é o preço com o desconto aplicado?", "84"),
        ("Se um aluno tem uma nota de 75 em um teste e a nota máxima é 100, qual é a porcentagem de acertos do aluno?", "75%"),
        ("Você comprou 5 pares de sapatos, cada um custando R$ 120,00. Se você pagou com um desconto total de 15%, quanto você pagou no total?", "510"),
        ("Um jardim possui uma forma triangular com uma base de 10 metros e uma altura de 12 metros. Qual é a área do jardim?", "60"),
        ("Você tem uma receita que rende 20 porções e quer ajustar a receita para render 5 porções. Se a receita original usa 2 xícaras de açúcar, quantas xícaras de açúcar você usará na receita ajustada?", "0,5"),
        ("Se você gastar R$ 75,00 em um mês e economizar 20% desse valor, quanto você economizou?", "15"),
        ("Um carro consome 8 litros de combustível para percorrer 100 km. Quantos litros serão necessários para percorrer 450 km?", "36"),
        ("Você tem um saldo de R$ 350,00 e faz uma compra de R$ 127,00. Qual é o saldo restante?", "223"),
        ("Se uma receita pede 3 colheres de sopa de óleo e você tem apenas colheres de chá (1 colher de sopa = 3 colheres de chá), quantas colheres de chá você deve usar?", "9"),
        ("Você investiu R$ 800,00 e obteve um retorno de 12%. Qual foi o valor do retorno?", "96"),
        ("Se você participa de uma corrida e corre 8 km no primeiro dia e aumenta a distância em 1 km a cada dia subsequente, qual será a distância total percorrida ao final de 5 dias?", "40"),
        ("Um livro custa R$ 85,00 e está com um desconto de 10%. Qual é o valor com o desconto aplicado?", "76,50"),
        ("Se você comprar 4 itens que custam R$ 37,00 cada, quanto você gastou no total?", "148"),
        ("Qual é a área de um círculo com raio de 7 metros? (Use π ≈ 3,14)", "153,86"),
        ("Se você tem um retângulo com comprimento de 15 metros e largura de 4 metros, qual é o perímetro do retângulo?", "38")
    ]

    for pergunta, resposta_correta in perguntas:
            while True:
                print(pergunta)
                resposta = input(" Sua resposta: ").strip()
                
                if resposta == resposta_correta:
                    print("Resposta correta!")
                    break
                else:
                    print("Resposta incorreta. Tente novamente.")
            continuar = input('Deseja continuar para a próxima pergunta? (s/n):').strip().lower()
            if continuar != 's':
                print('Voltando ao menu principal...')
                break

def calculadora():
    while True:
        print("Escolha uma operação:")
        print("1. Adição (+)")
        print("2. Subtração (-)")
        print("3. Multiplicação (*)")
        print("4. Divisão (/)")

        operacao = input("Digite a operação desejada (+, -, *, /): ")

        if operacao in ('+', '-', '*', '/'):
            try:
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))

                if operacao == '+':
                    resultado = num1 + num2
                elif operacao == '-':
                    resultado = num1 - num2
                elif operacao == '*':
                    resultado = num1 * num2
                elif operacao == '/':
                    if num2 != 0:
                        resultado = num1 / num2
                    else:
                        print("Erro: Divisão por zero não é permitida.")
                        continue  # Volta ao início do loop para tentar novamente

                print(f"O resultado é: {resultado}")

            except ValueError:
                print("Erro: Entrada inválida. Por favor, insira números válidos.")
        
        else:
            print("Erro: Operação inválida.")

        # Pergunta ao usuário se deseja continuar
        continuar = input('Deseja realizar outra operação? (s/n): ').strip().lower()
        if continuar != 's':
            print('Voltando ao menu principal...')
            break

def tabuada():
    while True:
        N3 = int(input('DIGITE UM Nº PARA TER A SUA TABUADA: '))

        V1 = N3*1
        V2 = N3*2
        V3 = N3*3
        V4 = N3*4
        V5 = N3*5
        V6 = N3*6
        V7 = N3*7
        V8 = N3*8
        V9 = N3*9
        V10 = N3*10

        print(N3,'X 1 =',V1)
        print(N3,'X 2 =',V2)
        print(N3,'X 3 =',V3)
        print(N3,'X 4 =',V4)
        print(N3,'X 5 =',V5)
        print(N3,'X 6 =',V6)
        print(N3,'X 7 =',V7)
        print(N3,'X 8 =',V8)
        print(N3,'X 9 =',V9)
        print(N3,'X 10 =',V10)

# Pergunta ao usuário se deseja continuar
        continuar = input('Deseja realizar outra consulta ? (s/n): ').strip().lower()
        if continuar != 's':
            print('Voltando ao menu principal...')
            break
    
def main():
    while True:  #vou iniciar um loop 
        mostrar_menu() # vai exibir o menu 
        
        try:
            escolha = int(input('Escolha uma opção de (1-4): '))
        except ValueError:
            print('Entrada inválida. Por favor, insira um número.')
            continue
        
        if escolha == 1:
            calculadora()
        elif escolha == 2:
            tabuada()
        elif escolha == 3:
            mostrar_submenu_jogos()
        elif escolha == 4:
            print('Saindo...')
            break
        else:
            print('Escolha inválida, tente novamente.')
            
if __name__ == "__main__":
    main()
