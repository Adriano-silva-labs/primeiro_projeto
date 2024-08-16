#Criando um aplicativo de matemática fácil e intuitivo

def mostrar_menu():
    print('====MENU====')
    print('1. Dobro, Triplo, Raiz Quadrada')
    print('2. Tabuada')
    print('3. Sair ')
    print('=================')
    
def dobro_triplo_raiz():
    n2 = int(input('DIGITE UM NÚMERO, VAMOS DESCOBRIR O DOBRO TRIPLO E RAIZ QUADRADA'))
    dobro = n2*2
    triplo = n2*3
    raiz_quadrada = n2**0.5

    print ('RESULTADO')
    print('DOBRO: {}\nTRIPLO: {}\nRAIZ QUADRADA: {}'.format(dobro, triplo, raiz_quadrada))
    

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

# Exemplo de uso das funções 
mostrar_menu()
escolha = int(input("Escolha uma opção (1-3) :"))
if escolha == 1:
    dobro_triplo_raiz()
if escolha == 2:
    tabuada()
elif escolha == 3:
    print('Saindo...')
else:
    print('Escolha inválida, tentee novamente. ')
    
