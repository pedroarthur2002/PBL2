import random


def tabuleiro_inicial():
    #Essa função gera o tabuleiro.   
    matriz = [[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]]
    adicionar_numero(matriz)
    adicionar_numero(matriz)    
    return matriz

def adicionar_numero(matriz):
    #Essa função adiciona o número 2 ou 4 numa posição aleatória do tabuleiro.
    vazia = []
    for i in range(4):
        for j in range(4):
            if matriz[i][j] == 0:
                vazia.append((i, j))
    if vazia:
        i, j = random.choice(vazia)        
        matriz[i][j] = random.choice([2, 4])

def imprimir_tabuleiro(matriz):
    #Essa função imprime a matriz num formato de tabuleiro que é mais intuitivo para jogar
    for i in matriz:
        for j in i:
            print(f'{j}',end='   ')
        print('')

def mover_esquerda(matriz):
    #Função que move os números diferentes de zero para a esquerda.
    aux_0 = []
    aux_1 = []
    aux_2 = []
    aux_3 = []
    #Esse trecho faz a soma dos elementos adjacentes de cada linha antes de fazer a movimentação.
    for i in range(3):        
        if matriz[0][i] == matriz [0][i+1]:
            matriz[0][i] += matriz[0][i+1]
            matriz[0][i+1] = 0                   
    #Esse trecho faz a movimentação do números.         
    for j in range(0,4):
        if matriz[0][j] != 0:
            aux_0.append(matriz[0][j])    
    for i in range(4-len(aux_0)):
        aux_0.append(0)
    matriz[0] = aux_0

    for i in range(3):        
        if matriz[1][i] == matriz [1][i+1]:
            matriz[1][i] += matriz[1][i+1]
            matriz[1][i+1] = 0           
            
    for j in range(0,4):
        if matriz[1][j] != 0:
            aux_1.append( matriz[1][j]) 
    for i in range(4-len(aux_1)):
        aux_1.append(0)  
    matriz[1] = aux_1

    for i in range(3):        
        if matriz[2][i] == matriz [2][i+1]:
            matriz[2][i] += matriz[2][i+1]
            matriz[2][i+1] = 0             
              
    for j in range(0,4):
        if matriz[2][j] != 0:
            aux_2.append( matriz[2][j])
    for i in range(4-len(aux_2)):
        aux_2.append(0)
    matriz[2] = aux_2

    for i in range(3):        
        if matriz[3][i] == matriz [3][i+1]:
            matriz[3][i] += matriz[3][i+1]
            matriz[3][i+1] = 0             
           
    for j in range(0,4):
        if matriz[3][j] != 0:
            aux_3.append( matriz[3][j])    
    for i in range(4-len(aux_3)):
        aux_3.append(0) 
    matriz[3] = aux_3
    
    adicionar_numero(matriz)
    adicionar_numero(matriz) 
    print(imprimir_tabuleiro(matriz))

def mover_direita(matriz):
    #Função que move os números diferentes de zero para a direita.
    aux_0 = []
    aux_1 = []
    aux_2 = []
    aux_3 = [] 
    #Esse trecho faz a soma dos elementos adjacentes de cada linha antes de fazer a movimentação.
    for i in range(2,-1,-1):        
        if matriz[0][i] == matriz [0][i+1]:
            matriz[0][i] += matriz[0][i+1]
            matriz[0][i+1] = 0
    #Esse trecho faz a movimentação do números.           
    for j in range(3,-1,-1):
        if matriz[0][j] != 0:
            aux_0.append(matriz[0][j])    
    for i in range(4-len(aux_0)):
        aux_0.append(0)
    matriz[0] = aux_0[::-1]       

    for i in range(2,-1,-1):        
        if matriz[1][i] == matriz [1][i+1]:
            matriz[1][i] += matriz[1][i+1]
            matriz[1][i+1] = 0

    for j in range(3,-1,-1):
        if matriz[1][j] != 0:
            aux_1.append( matriz[1][j]) 
    for i in range(4-len(aux_1)):
        aux_1.append(0) 
    matriz[1] = aux_1[::-1]               

    for i in range(2,-1,-1):        
        if matriz[2][i] == matriz [2][i+1]:
            matriz[2][i] += matriz[2][i+1]
            matriz[2][i+1] = 0

    for j in range(3,-1,-1):
        if matriz[2][j] != 0:
            aux_2.append( matriz[2][j])
    for i in range(4-len(aux_2)):
        aux_2.append(0)
    matriz[2] = aux_2[::-1]                

    for i in range(2,-1,-1):        
        if matriz[3][i] == matriz [3][i+1]:
            matriz[3][i] += matriz[3][i+1]
            matriz[3][i+1] = 0

    for j in range(3,-1,-1):
        if matriz[3][j] != 0:
            aux_3.append( matriz[3][j])    
    for i in range(4-len(aux_3)):
        aux_3.append(0)
    matriz[3] = aux_3[::-1]           

    adicionar_numero(matriz)
    adicionar_numero(matriz) 
    print(imprimir_tabuleiro(matriz))

def mover_cima(matriz):
    #Função que move os números diferentes de zero para cima.
    aux_0 = []
    aux_1 = []
    aux_2 = []
    aux_3 = []
    #Esse trecho soma os números iguais adjascentes nas colunas.
    for i in range(3):        
        if matriz[i][0] == matriz [i+1][0]:
            matriz[i][0] += matriz[i+1][0]
            matriz[i+1][0] = 0
    #Esse trecho faz a movimentação do números.                  
    for i in range(0,4):
        if matriz[i][0] != 0:
            aux_0.append(matriz[i][0])    
    for i in range(4-len(aux_0)):
        aux_0.append(0)      
    matriz[0][0] = aux_0[0]
    matriz[1][0] = aux_0[1]
    matriz[2][0] = aux_0[2]
    matriz[3][0] = aux_0[3]        

    for i in range(3):        
        if matriz[i][1] == matriz [i+1][1]:
            matriz[i][1] += matriz[i+1][1]
            matriz[i+1][1] = 0

    for i in range(0,4):
        if matriz[i][1] != 0:
            aux_1.append(matriz[i][1]) 
    for i in range(4-len(aux_1)):
        aux_1.append(0)    
    matriz[0][1] = aux_1[0]
    matriz[1][1] = aux_1[1]  
    matriz[2][1] = aux_1[2]   
    matriz[3][1] = aux_1[3]          

    for i in range(3):        
        if matriz[i][2] == matriz [i+1][2]:
            matriz[i][2] += matriz[i+1][2]
            matriz[i+1][2] = 0

    for i in range(0,4):
        if matriz[i][2] != 0:
            aux_2.append(matriz[i][2])
    for i in range(4-len(aux_2)):
        aux_2.append(0)   
    matriz[0][2] = aux_2[0]
    matriz[1][2] = aux_2[1]   
    matriz[2][2] = aux_2[2]   
    matriz[3][2] = aux_2[3]
    #Esse trecho soma os números iguais adjacentes nas colunas.
    for i in range(3):        
        if matriz[i][3] == matriz [i+1][3]:
            matriz[i][3] += matriz[i+1][3]
            matriz[i+1][3] = 0            
    #Esse trecho faz a movimentação do números.      
    for i in range(0,4):
        if matriz[i][3] != 0:
            aux_3.append(matriz[i][3])    
    for i in range(4-len(aux_3)):
        aux_3.append(0)    
    matriz[0][3] = aux_3[0]
    matriz[1][3] = aux_3[1]   
    matriz[2][3] = aux_3[2]   
    matriz[3][3] = aux_3[3]

    adicionar_numero(matriz)
    adicionar_numero(matriz)           
    print(imprimir_tabuleiro(matriz)) 

def mover_baixo(matriz):
    #Função que move os números diferentes de zero para baixo.
    aux_0 = []
    aux_1 = []
    aux_2 = []
    aux_3 = []
    #Esse trecho soma os números iguais adjacentes nas colunas.
    for i in range(2,-1,-1):        
        if matriz[i][0] == matriz [i+1][0]:
            matriz[i][0] += matriz[i+1][0]
            matriz[i+1][0] = 0
    #Esse trecho faz a movimentação do números.
    for i in range(3,-1,-1):
        if matriz[i][0] != 0:
            aux_0.append(matriz[i][0])    
    for i in range(4-len(aux_0)):
        aux_0.append(0)
    matriz[i][0] = aux_0[::-1] 
    matriz[0][0] = aux_0[3]
    matriz[1][0] = aux_0[2]
    matriz[2][0] = aux_0[1]
    matriz[3][0] = aux_0[0]
            
    for i in range(2,-1,-1):        
        if matriz[i][1] == matriz [i+1][1]:
            matriz[i][1] += matriz[i+1][1]
            matriz[i+1][1] = 0

    for i in range(3,-1,-1):
        if matriz[i][1] != 0:
            aux_1.append(matriz[i][1]) 
    for i in range(4-len(aux_1)):
        aux_1.append(0)            
    matriz[0][1] = aux_1[3]
    matriz[1][1] = aux_1[2]  
    matriz[2][1] = aux_1[1]   
    matriz[3][1] = aux_1[0]

    for i in range(2,-1,-1):        
        if matriz[i][2] == matriz [i+1][2]:
            matriz[i][2] += matriz[i+1][2]
            matriz[i+1][2] = 0

    for i in range(3,-1,-1):
        if matriz[i][2] != 0:
            aux_2.append(matriz[i][2])
    for i in range(4-len(aux_2)):
        aux_2.append(0)           
    matriz[0][2] = aux_2[3]
    matriz[1][2] = aux_2[2]  
    matriz[2][2] = aux_2[1]   
    matriz[3][2] = aux_2[0]

    for i in range(2,-1,-1):        
        if matriz[i][3] == matriz [i+1][3]:
            matriz[i][3] += matriz[i+1][3]
            matriz[i+1][3] = 0

    for i in range(3,-1,-1):
        if matriz[i][3] != 0:
            aux_3.append(matriz[i][3])    
    for i in range(4-len(aux_3)):
        aux_3.append(0)                
    matriz[0][3] = aux_3[3]
    matriz[1][3] = aux_3[2]  
    matriz[2][3] = aux_3[1]   
    matriz[3][3] = aux_3[0]

    adicionar_numero(matriz)
    adicionar_numero(matriz) 
    print(imprimir_tabuleiro(matriz))

def vitoria(matriz):
    #Função que verifica se o usuário ganhou o jogo.
    for i in range(0,4):
        for j in range(0,4):
            if matriz[i][j] == 2048:
                print('Parabéns, você ganhou! Reiniciando o jogo...')
                break

def derrota(matriz):
    #Função que verifica se o usuário perdeu o jogo.
    for i in range(4):
        for j in range(4):
            if matriz[i][j] == 0:
                return False
            
            if j < 3 and matriz[i][j] == matriz[i][j + 1]:
                return False
            if i < 3 and matriz[i][j] == matriz[i + 1][j]:
                return False
    
    return True

cont_jogadas = 0    
while True:
    opçao = int(input('\n[1] Iniciar partida\n[2]Quantidade de jogadas\n[3] Sair do jogo\nOpção:'))
    if opçao == 3:
        print('Você escolheu sair do jogo!')
        break
    if opçao == 2:
        if cont_jogadas != 0:
            print(f'Você jogou {cont_jogadas} vezes')
        elif cont_jogadas == 0:
            print('Você não fez jogadas ainda!')
                
    if opçao == 1:
        while True:
            if cont_jogadas == 0:
                tabuleiro = tabuleiro_inicial()
                imprimir_tabuleiro(tabuleiro)
            direçao = input('\n[w] cima\n[a] esquerda\n[d] direita\n[s] baixo\nDigite uma direção: ').lower().strip()
            direçao_valida = direçao.lower().strip()            
            if direçao_valida in ['w','a','s','d']:
                cont_jogadas += 1
                if direçao_valida == 'a':
                    a = mover_esquerda(tabuleiro)
                    vitoria(tabuleiro)
                    if derrota(tabuleiro):
                        print('Você perdeu! Reiniciando o jogo...')
                        break
                                     
                if direçao_valida == 'd':
                    d = mover_direita(tabuleiro)
                    vitoria(tabuleiro)
                    if derrota(tabuleiro):
                        print('Você perdeu! Reiniciando o jogo...')
                        break
                    
                if direçao_valida == 'w':
                    w = mover_cima(tabuleiro)
                    vitoria(tabuleiro)
                    if derrota(tabuleiro):
                        print('Você perdeu! Reiniciando o jogo...')
                        break
                     
                if direçao_valida == 's':
                    s = mover_baixo(tabuleiro)
                    vitoria(tabuleiro)
                    if derrota(tabuleiro):
                        print('Você perdeu! Reiniciando o jogo...')
                        break
                  
            else:
                print('Você errou o dado de entrada, tente novamente!')
            
    elif opçao != 1 and opçao != 2 and opçao != 3:
        print('Você errou o dado de entrada, tente novamente!')