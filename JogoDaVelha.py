#criando um jogo da velha
import os
os.system('cls')

matriz = [["-","-","-"],
          ["-","-","-"],
          ["-","-","-"]]

#Função para imprimir a matriz
def imprimir_matriz(matriz):
    for linha in matriz:
        print(" ".join(linha))

#Loop principal do jogo

jogador = "X"
jogadas = 0

while True:
    #Imprime a matriz atual
    imprimir_matriz(matriz)

    #Lê a jogada do usuário
    jogada = input("Jogador "+jogador+" ,faça a sua jogada (linha,coluna): ")
    linha, coluna = jogada.split(",")
    linha = int(linha.strip())
    coluna = int(coluna.strip())
    
    #verifica se a jogada é válida
    if matriz[linha][coluna] != "-":
        print("Essa jogada não é valida. Tente novamente")
        continue

    #Faz a jogada
    matriz[linha][coluna] = jogador
    jogadas = jogadas+1

    #Verifica se o jogo acabou
    vitoria = False

    #verifica se alguma linha está completa
    for linha in matriz:
        if linha[0]==linha[1]==linha[2]!="-":
            vitoria = True
            break
    
    #Verificar se alguma coluna está completa
    for j in range(3):
        if matriz[0][j]==matriz[1][j]==matriz[2][j]!="-":
            vitoria=True
            break

    #Verificar se alguma diagonal está completa
    if matriz[0][0]==matriz[1][1]==matriz[2][2]!="-" or matriz[0][2]==matriz[1][1]==matriz[2][0]!="-":
        vitoria = True
    if vitoria:
        imprimir_matriz(matriz)
        print("Parabéns jogador " + jogador + " , você ganhou")
        break
    elif jogadas == 9:
        imprimir_matriz(matriz)
        print("Empate")
        break

    #Passa a vez para o próximo jogador
    if jogador =="X":
        jogador = "O"
    else:
        jogador = "X"