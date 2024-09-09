import numpy as np
import minhasFuncoes as mf


########################################################################  
#   programa principal - NÃO ALTERE NADA ABAIXO DESTA LINHA!!!!!       #
#   Mas você deve entender o código, para implementar corretamente     #
#   as duas funções                                                    #
########################################################################

# Estrutura da matriz Mega contem em cada linha, números inteiros representando as seguintes informações:
# [Concurso, Dia, Mês, Ano, D1, D2, D3, D4, D5, D6, GSena, RSena,
#  GQuina, RQuina, GQuadra, RQuadra, ValorAcum, EstPremio, AcumMegaVirada]



def mvAcMv(Matriz):
    """Obtem o maior valor na coluna 18 da matriz escolhida"""
    linha, coluna = np.shape(Matriz)
    maior = [Matriz[0][18],0,18]
    for i in range(linha):
        if maior[0] < Matriz[i][18]:
            maior[0] = Matriz[i][18]
            maior[1] = i+1
    return maior[1]

def imprimeInfoConc(Matriz, NConcurso, InfoAdicional = False):
    NConcurso -= 1
    print(f"Concurso {NConcurso+1}. Data do sorteio: {Matriz[NConcurso][1]}/{Matriz[NConcurso][2]}/{Matriz[NConcurso][3]}")
    print('Dezenas sorteadas: ',end=" ")
    for i in range(4,10):
        if i < 9:
            print(f'{Matriz[NConcurso][i]}', end=", ")
        elif i == 9:
            print(f'e {Matriz[NConcurso][i]}')

    if InfoAdicional == True:
        print("Premiação: \n",
            f"6 acertos: {Matriz[NConcurso][10]}," + " "*(7-len(str(Matriz[NConcurso][10]))) + f"R$ {Matriz[NConcurso][11]},00\n",
            f"5 acertos: {Matriz[NConcurso][12]}," + " "*(7-len(str(Matriz[NConcurso][12]))) + f"R$ {Matriz[NConcurso][13]},00\n",
            f"4 acertos: {Matriz[NConcurso][14]}," + " "*(7-len(str(Matriz[NConcurso][14]))) + f"R$ {Matriz[NConcurso][15]},00\n")



print('Este programa analisa os resultados de jogos da Megasena')
print('Por simplificação, nos valores em Reais, os centavos estão sendo omitidos')
# função que faz a leitura do arquivo de dados e gera a matriz e retorna o endereço da matriz gerada (Mega)
# retorna também o número de concursos lidos (numConc)
Mega, numConc = mf.learq()

# imprime algumas informações sobre os concursos, armazenadas na matriz Mega
# Informa o total de concursos registrados na matriz Mega
print('\nO arquivo lido possui resultados de %d concursos!' %numConc)
# Imprime a data do primeiro concurso (informações na primeira linha da matriz Mega)
print('O primeiro sorteio registrado foi em %d/%d/%d.' %(Mega[0][1], Mega[0][2], Mega[0][3]))
# Imprime a data do último concurso (informações na última linha da matriz Mega)
print('O último sorteio registrado foi em %d/%d/%d.' %(Mega[numConc-1][1], Mega[numConc-1][2], Mega[numConc-1][3]))
print()

### chama mvAcMv para obter o número do concurso com o maior valor acumulado para a megasena da virada
conc = mvAcMv(Mega)
print('O maior valor acumulado para a Megasena da Virada foi: %d' %Mega[conc-1][18])

# chama a função para imprimir a informação resumida do concurso retornado pela função
# implementada - não tem o 3o parâmetro que é opcional. NÃO imprimirá as informações de premiação
imprimeInfoConc(Mega, conc)

# permite que o usuário consulte informações detalhadas de qualquer concurso registrado
while True:
    # usa a função leiaInt para obter o número do concurso (1-numConc), 0 termina.
    num = mf.leiaInt('Entre com o número do concurso (ou 0 para terminar): ', 0, numConc, 'Concurso inexistente')
    if num == 0 :
        break
    # chama a função para imprimir a informação detalhada do concurso - especifica o
    # 3o parâmetro, com valor True que obrigará a impressão das informações da premiação 
    imprimeInfoConc(Mega, num, True)
