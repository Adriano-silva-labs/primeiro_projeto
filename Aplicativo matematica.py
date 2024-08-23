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
            print('Iniciando questionario')
        elif opcao == '2':
            print('Iniciando Raciocínio Rápido...')
        elif opcao == '3':
            print('Voltando ao menu principal...')
            break
        else:
            print('Opção inválida. Tente novamente.')
    
    print('=================')
    
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
