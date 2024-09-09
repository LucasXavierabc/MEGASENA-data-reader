# -*- coding: utf-8 -*-
import numpy as np

# le o arquivo "MegasenaDezenasOrdemCrescente2.csv" e monta a matrizMega, contendo em cada linha valores inteiros
# representando as seguintes informações (13 em cada linha):
# NúmeroDoConcurso, Dia, Mês, Ano, dezena1, dezena2, dezena3, dezena4, dezena5, dezena6, GanhadoresSena, GanhadoresQuina,
# GanhadoresQuadra 
# O número de linhas da matrizMega será determinada pelo tamanho (número de linhas do arquivo de entrada)
# Retorna:
#   endereço da matriz criada (matrizMega) e o seu número de linhas (n)
def learq() :

    def extraiInt(s) :
        return int(s)
##        if s == '0,00' :
##            return 0
##        else :
##            pi, pf = s.split(',')
##            return int(pi)
            
    try:
        arq = open("MegaSenaDezenasOrdemCrescente.csv", encoding="utf8") 
    except:
        print("A abertura do arquivo falhou!")
        quit()
    s = arq.read()
    arq.close()
    cont = 0   # conta o número de linhas totais, incluindo título (texto) e última linha (vazia)
    for s1 in s.split('\n'):
        cont = cont + 1    
    n = cont - 2
    matrizMega = np.empty((n, 19), dtype=int)
    cont = -1
    for s1 in s.split('\n'):
        if cont > -1  : # exclui a primeira linha (texto)
            if s1 != '' : # exclui eventuais linhas em branco (incluindo a última)
                Conc,Data,D1,D2,D3,D4,D5,D6,GSena,RSena,GQuina,RQuina,GQuadra,RQuadra,ValAc,EstPr,AcMegaVir = s1.split(',')
                dia,mes,ano = Data.split('/')
                RSenaI = extraiInt(RSena)
                RQuinaI = extraiInt(RQuina)
                RQuadraI = extraiInt(RQuadra)
                ValAcI = extraiInt(ValAc)
                EstPrI = extraiInt(EstPr)
                AcMegaVirI = extraiInt(AcMegaVir)
                matrizMega[cont] = [Conc,dia,mes,ano,D1,D2,D3,D4,D5,D6,GSena,RSenaI,GQuina,RQuinaI,GQuadra,RQuadraI,ValAcI, EstPrI,AcMegaVirI]
                cont = cont + 1
        else :
            cont = cont + 1      
    return matrizMega, n

# Nome: leiaInt
# Tarefa: Lê um valor inteiro na faixa [linf, lsup] 
# Parâmetros de entrada:
#   msg: mensagem solicitando o valor (string)
#   linf: limite inferior da faixa (inteiro)
#   lsup: limite superior da faixa (inteiro)
#   msgErro: mensagem de erro quando valor fora da faixa (string)
#   exibir: define a exibição (ou não) da mensagem de erro (boolean)
# Retorna:
#   valor lido na faixa [linf, lsup] (inteiro)
def leiaInt(msg, linf, lsup, msgErro, exibir=True) :
        x = int(input(msg))
        while x < linf or x > lsup :
            if exibir :
                print(msgErro)
            x = int(input(msg))
        return x

# encontra o menor valor em um arranjo. Inicia a busca na posição p
# Retorna:
#   a posição (pos) do menor elemento do arranjo
def acha_menor(arranjo, p) :
    menor = arranjo[p]
    pos = p
    for i in range (p, len(arranjo)) :
        if arranjo[i] < menor :
            menor = arranjo[i]
            pos = i
    return pos

# troca de posição os valores dos elementos das posições p1 e p2
# do arranjo
# Não retorna valor
def troca(arranjo, p1, p2):
    temp = arranjo[p1]
    arranjo[p1] = arranjo[p2]
    arranjo[p2] = temp

# ordena um arranjo em ordem crescente (ou não decrescente, em caso de valores repetidos)
# Não retorna valor
def ordenaArranjo(arranjo) :
    # percorrer o arranjo e encontrar o menor valor
    # trocar o menor valor com  o primeiro elemento
    for i in range (0, len(arranjo)-1) :
        pos_menor = acha_menor(arranjo, i)
        troca(arranjo, pos_menor, i)

# verifica se um valor da posição pos, aparece em posições anteriores
# arr: arranjo unidimensional
# pos: posição onde o novo elemento foi inserido
# retorna: True se o novo elemento já existe no arranjo
#          False, caso contrário.
def repetida(arr, pos) :
    if pos == 0 :
        return False
    else :
        rep = False
        for i in range (0, pos) :
            if arr[i] == arr[pos] :
                rep = True
        return rep
            
    
def mvAcMv(Matriz):
    linha, coluna = np.shape(Matriz)
    maior = [Matriz[0][18],0,18]
    for i in range(linha):
        if maior[0] < Matriz[i][18]:
            maior[0] = Matriz[i][18]
            maior[1] = i
    return maior[1]

def imprimeInfoConc(Matriz, NConcurso, InfoAdicional = False):
    if InfoAdicional == False:
        print(f"Concurso {NConcurso}. Data do sorteio: {Matriz[NConcurso][1]}/{Matriz[NConcurso][2]}/{Matriz[NConcurso][3]}")
        print(f"Dezanas sorteadas: {Matriz[NConcurso][4]}, {Matriz[NConcurso][5]}, {Matriz[NConcurso][6]}, {Matriz[NConcurso][7]}, {Matriz[NConcurso][8]}, {Matriz[NConcurso][9]}")
    
    elif InfoAdicional == True:
        print("Premiação: \n",
            f"6 acertos: {Matriz[NConcurso][10]},\t R$ {Matriz[NConcurso][11]}\n",
            f"5 acertos: {Matriz[NConcurso][12]},\t R$ {Matriz[NConcurso][13]}\n",
            f"4 acertos: {Matriz[NConcurso][14]},\t R$ {Matriz[NConcurso][15]}\n")