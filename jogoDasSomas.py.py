"""
******************************************************************************************
Autor: Naylane do Nascimento Ribeiro
Componente Curricular: Algoritmos I
Concluído em: 14/11/2022
Declaro que este código foi elaborado por mim de forma individual e não contém
nenhum trecho de código de colega ou de outro autor, tais como provindos de livros e
apostilas, e páginas ou documentos eletrônicos da internet. Qualquer trecho de código
de outra autoria que não a minha está destacado com uma citação do autor e a fonte do
código, e estou ciente que estes trechos não serão considerados para fins de avaliação.
******************************************************************************************
"""

from random import shuffle

def gera_numeros(dimensao):
    numeros = []

    # preenchendo a lista de números
    for i in range(1, dimensao + 1):
        numeros.append(i)
    
    # embaralhando os números
    shuffle(numeros)

    return numeros

def gera_tabuleiro_espelho(dimensao):
    tabuleiro_espelho = []

    for i in range(dimensao):
        linha = []
        numero = gera_numeros(dimensao)
        for j in range(dimensao):
            linha.append(numero[j])
        tabuleiro_espelho.append(linha)
    
    return tabuleiro_espelho

def gera_tabuleiro(dimensao):
    tabuleiro = []

    for i in range(dimensao):
        linha = []
        for j in range(dimensao):
            linha.append(0)
        tabuleiro.append(linha)

    return tabuleiro

def imprime_tabuleiro(secao, dimensao, somas_linhas, somas_colunas):
    if dimensao == 4:
        print(f'''
   {somas_linhas[0]} \t [ {secao[0][0]} ] [ {secao[0][1]} ] | [ { secao[1][0]} ] [ {secao[1][1]} ]
   {somas_linhas[1]} \t [ {secao[0][2]} ] [ {secao[0][3]} ] | [ {secao[1][2]} ] [ {secao[1][3]} ]
    \t -------------------------
   {somas_linhas[2]} \t [ { secao[2][0]} ] [ {secao[2][1]} ] | [ {secao[3][0]} ] [ {secao[3][1]} ]
   {somas_linhas[3]} \t [ {secao[2][2]} ] [ {secao[2][3]} ] | [ {secao[3][2]} ] [ {secao[3][3]} ]
           {somas_colunas[0]} \t {somas_colunas[1]} \t {somas_colunas[2]}    {somas_colunas[3]}
    ''')

    elif dimensao == 9:
        print(f'''
    {somas_linhas[0]} \t [ {secao[0][0]} ] [ {secao[0][1]} ] [ {secao[0][2]} ] | [ {secao[1][0]} ] [ {secao[1][1]} ] [ {secao[1][2]} ] | [ {secao[2][0]} ] [ {secao[2][1]} ] [ {secao[2][2]} ]
    {somas_linhas[1]} \t [ {secao[0][3]} ] [ {secao[0][4]} ] [ {secao[0][5]} ] | [ {secao[1][3]} ] [ {secao[1][4]} ] [ {secao[1][5]} ] | [ {secao[2][3]} ] [ {secao[2][4]} ] [ {secao[2][5]} ]
    {somas_linhas[2]} \t [ {secao[0][6]} ] [ {secao[0][7]} ] [ {secao[0][8]} ] | [ {secao[1][6]} ] [ {secao[1][7]} ] [ {secao[1][8]} ] | [ {secao[2][6]} ] [ {secao[2][7]} ] [ {secao[2][8]} ]
    \t ---------------------------------------------------------
    {somas_linhas[3]} \t [ {secao[3][0]} ] [ {secao[3][1]} ] [ {secao[3][2]} ] | [ {secao[4][0]} ] [ {secao[4][1]} ] [ {secao[4][2]} ] | [ {secao[5][0]} ] [ {secao[5][1]} ] [ {secao[5][2]} ]
    {somas_linhas[4]} \t [ {secao[3][3]} ] [ {secao[3][4]} ] [ {secao[3][5]} ] | [ {secao[4][3]} ] [ {secao[4][4]} ] [ {secao[4][5]} ] | [ {secao[5][3]} ] [ {secao[5][4]} ] [ {secao[5][5]} ] 
    {somas_linhas[5]} \t [ {secao[3][6]} ] [ {secao[3][7]} ] [ {secao[3][8]} ] | [ {secao[4][6]} ] [ {secao[4][7]} ] [ {secao[4][8]} ] | [ {secao[5][6]} ] [ {secao[5][7]} ] [ {secao[5][8]} ]
    \t ---------------------------------------------------------
    {somas_linhas[6]} \t [ {secao[6][0]} ] [ {secao[6][1]} ] [ {secao[6][2]} ] | [ {secao[7][0]} ] [ {secao[7][1]} ] [ {secao[7][2]} ] | [ {secao[8][0]} ] [ {secao[8][1]} ] [ {secao[8][2]} ]
    {somas_linhas[7]} \t [ {secao[6][3]} ] [ {secao[6][4]} ] [ {secao[6][5]} ] | [ {secao[7][3]} ] [ {secao[7][4]} ] [ {secao[7][5]} ] | [ {secao[8][3]} ] [ {secao[8][4]} ] [ {secao[8][5]} ]
    {somas_linhas[8]} \t [ {secao[6][6]} ] [ {secao[6][7]} ] [ {secao[6][8]} ] | [ {secao[7][6]} ] [ {secao[7][7]} ] [ {secao[7][8]} ] | [ {secao[8][6]} ] [ {secao[8][7]} ] [ {secao[8][8]} ]
    \t  {somas_colunas[0]}    {somas_colunas[1]}    {somas_colunas[2]}      {somas_colunas[3]}    {somas_colunas[4]}    {somas_colunas[5]}      {somas_colunas[6]}    {somas_colunas[7]}    {somas_colunas[8]}
    ''')

def valida_entradas(dimensao):    
    # pede a seção que o jogador deseja revelar um número até que seja digitada uma entrada válida
    while True:
        try:
            secao_escolhida = int(input('\nDigite a seção que deseja revelar um número: '))
            if secao_escolhida < 1 or secao_escolhida > dimensao:
                print('A seção deve ser entre 1 e %d! Tente novamente.' % dimensao)
            else:
                break
        except:
            print('Tipo de entrada inválido! Tente novamente.')
    
    # pede o número que o jogador deseja revelar até que seja digitada uma entrada válida
    while True:
            try:
                numero = int(input('\nDigite o número a ser revelado: '))
                if numero < 1 or numero > dimensao:
                    print('O número deve ser entre 1 e %d! Tente novamente.' % dimensao)
                else:
                    break
            except:
                print('Tipo de entrada inválido! Tente novamente.')
                
    return secao_escolhida, numero

def calcula_somas(tabuleiro, dimensao):
    somas_linhas = []
    somas_colunas = []

    # adicionando zero nas listas de somas das linhas e colunas para depois alterar para o valor correlato
    for i in range(dimensao):
        somas_linhas.append(0)
        somas_colunas.append(0)

    if dimensao == 4:
        # calcula a soma da diagonal
        soma_diagonal = tabuleiro[0][0] + tabuleiro[0][3] + tabuleiro[3][0] + tabuleiro[3][3]

        for x in range(2):
            # calcula a soma das linhas
            somas_linhas[x] = tabuleiro[0][x*2] + tabuleiro[0][(x*2)+1] + tabuleiro[1][x*2] + tabuleiro[1][(x*2)+1]
            somas_linhas[x+2] = tabuleiro[2][x*2] + tabuleiro[2][(x*2)+1] + tabuleiro[3][x*2] + tabuleiro[3][(x*2)+1]
            # calcula a soma das colunas
            somas_colunas[x] = tabuleiro[0][x] + tabuleiro[0][x+2] + tabuleiro[2][x] + tabuleiro[2][x+2]
            somas_colunas[x+2] = tabuleiro[1][x] + tabuleiro[1][x+2] + tabuleiro[3][x] + tabuleiro[3][x+2]
        
    elif dimensao == 9:
        # calcula a soma da diagonal
        soma_diagonal = tabuleiro[0][0] + tabuleiro[0][4] + tabuleiro[0][8] + tabuleiro[4][0] + tabuleiro[4][4] + tabuleiro[4][8] + tabuleiro[8][0] + tabuleiro[8][4] + tabuleiro[8][8]
        
        for x in range(3):
            # calcula a soma das linhas
            somas_linhas[x] = tabuleiro[0][x*3] + tabuleiro[0][(x*3)+1] + tabuleiro[0][(x*3)+2] + tabuleiro[1][x*3] + tabuleiro[1][(x*3)+1] + tabuleiro[1][(x*3)+2] + tabuleiro[2][x*3] + tabuleiro[2][(x*3)+1] + tabuleiro[2][(x*3)+2]
            somas_linhas[x+3] = tabuleiro[3][x*3] + tabuleiro[3][(x*3)+1] + tabuleiro[3][(x*3)+2] + tabuleiro[4][x*3] + tabuleiro[4][(x*3)+1] + tabuleiro[4][(x*3)+2] + tabuleiro[5][x*3] + tabuleiro[5][(x*3)+1] + tabuleiro[5][(x*3)+2]
            somas_linhas[x+6] = tabuleiro[6][x*3] + tabuleiro[6][(x*3)+1] + tabuleiro[6][(x*3)+2] + tabuleiro[7][x*3] + tabuleiro[7][(x*3)+1] + tabuleiro[7][(x*3)+2] + tabuleiro[8][x*3] + tabuleiro[8][(x*3)+1] + tabuleiro[8][(x*3)+2]
            # calcula a soma das colunas
            somas_colunas[x] = tabuleiro[0][x] + tabuleiro[0][x+3] + tabuleiro[0][x+6] + tabuleiro[3][x] + tabuleiro[3][x+3] + tabuleiro[3][x+6] + tabuleiro[6][x] + tabuleiro[6][x+3] + tabuleiro[6][x+6]
            somas_colunas[x+3] = tabuleiro[1][x] + tabuleiro[1][x+3] + tabuleiro[1][x+6] + tabuleiro[4][x] + tabuleiro[4][x+3] + tabuleiro[4][x+6] + tabuleiro[7][x] + tabuleiro[7][x+3] + tabuleiro[7][x+6]
            somas_colunas[x+6] = tabuleiro[2][x] + tabuleiro[2][x+3] + tabuleiro[2][x+6] + tabuleiro[5][x] + tabuleiro[5][x+3] + tabuleiro[5][x+6] + tabuleiro[8][x] + tabuleiro[8][x+3] + tabuleiro[8][x+6]
    
    return somas_linhas, somas_colunas, soma_diagonal

def calcula_pontos(tabuleiro, dimensao):
    # criando e adicionando valor 0 para as listas que guardam as somas das linhas, colunas e da diagonal a cada rodada
    pontos_linhas, pontos_colunas, ponto_diagonal = [], [], [0]
    for i in range(dimensao):
        pontos_linhas.append(0)
        pontos_colunas.append(0)

    if dimensao == 4:
        # calcula a soma diagonal
        ponto_diagonal = tabuleiro[0][0] + tabuleiro[0][3] + tabuleiro[3][0] + tabuleiro[3][3]

        for x in range(2):
            # calcula a soma das linhas
            pontos_linhas[x] = tabuleiro[0][x*2] + tabuleiro[0][(x*2)+1] + tabuleiro[1][x*2] + tabuleiro[1][(x*2)+1]
            pontos_linhas[x+2] = tabuleiro[2][x*2] + tabuleiro[2][(x*2)+1] + tabuleiro[3][x*2] + tabuleiro[3][(x*2)+1]
            # calcula a soma das colunas
            pontos_colunas[x] = tabuleiro[0][x] + tabuleiro[0][x+2] + tabuleiro[2][x] + tabuleiro[2][x+2]
            pontos_colunas[x+2] = tabuleiro[1][x] + tabuleiro[1][x+2] + tabuleiro[3][x] + tabuleiro[3][x+2]
        
    elif dimensao == 9:
        # calcula a soma diagonal
        ponto_diagonal = tabuleiro[0][0] + tabuleiro[0][4] + tabuleiro[0][8] + tabuleiro[4][0] + tabuleiro[4][4] + tabuleiro[4][8] + tabuleiro[8][0] + tabuleiro[8][4] + tabuleiro[8][8]
        
        for x in range(3):
            # calcula a soma das linhas
            pontos_linhas[x] = tabuleiro[0][x*3] + tabuleiro[0][(x*3)+1] + tabuleiro[0][(x*3)+2] + tabuleiro[1][x*3] + tabuleiro[1][(x*3)+1] + tabuleiro[1][(x*3)+2] + tabuleiro[2][x*3] + tabuleiro[2][(x*3)+1] + tabuleiro[2][(x*3)+2]
            pontos_linhas[x+3] = tabuleiro[3][x*3] + tabuleiro[3][(x*3)+1] + tabuleiro[3][(x*3)+2] + tabuleiro[4][x*3] + tabuleiro[4][(x*3)+1] + tabuleiro[4][(x*3)+2] + tabuleiro[5][x*3] + tabuleiro[5][(x*3)+1] + tabuleiro[5][(x*3)+2]
            pontos_linhas[x+6] = tabuleiro[6][x*3] + tabuleiro[6][(x*3)+1] + tabuleiro[6][(x*3)+2] + tabuleiro[7][x*3] + tabuleiro[7][(x*3)+1] + tabuleiro[7][(x*3)+2] + tabuleiro[8][x*3] + tabuleiro[8][(x*3)+1] + tabuleiro[8][(x*3)+2]
            # calcula a soma das colunas
            pontos_colunas[x] = tabuleiro[0][x] + tabuleiro[0][x+3] + tabuleiro[0][x+6] + tabuleiro[3][x] + tabuleiro[3][x+3] + tabuleiro[3][x+6] + tabuleiro[6][x] + tabuleiro[6][x+3] + tabuleiro[6][x+6]
            pontos_colunas[x+3] = tabuleiro[1][x] + tabuleiro[1][x+3] + tabuleiro[1][x+6] + tabuleiro[4][x] + tabuleiro[4][x+3] + tabuleiro[4][x+6] + tabuleiro[7][x] + tabuleiro[7][x+3] + tabuleiro[7][x+6]
            pontos_colunas[x+6] = tabuleiro[2][x] + tabuleiro[2][x+3] + tabuleiro[2][x+6] + tabuleiro[5][x] + tabuleiro[5][x+3] + tabuleiro[5][x+6] + tabuleiro[8][x] + tabuleiro[8][x+3] + tabuleiro[8][x+6]

    return pontos_linhas, pontos_colunas, ponto_diagonal

def partida(dimensao):
    print('\nIniciando partida...')
    print('-=' * 50)
    
    # faz chamada das funções necessárias
    tabuleiro_espelho = gera_tabuleiro_espelho(dimensao)
    tabuleiro = gera_tabuleiro(dimensao)
    somas_linhas, somas_colunas, soma_diagonal = calcula_somas(tabuleiro_espelho, dimensao)
    imprime_tabuleiro(tabuleiro, dimensao, somas_linhas, somas_colunas)
    
    linhas_reveladas = {}
    colunas_reveladas = {}
    diagonal_revelada = False

    jogadores = {
        'jogador 1': 0,
        'jogador 2': 0
    }
    jogador_da_partida = 'jogador 2'
    
    partida_continua = True
    while partida_continua:
        # alterna a partida entre os jogadores 1 e 2:
        if jogador_da_partida == 'jogador 1':
            jogador_da_partida = 'jogador 2'
        elif jogador_da_partida == 'jogador 2':
            jogador_da_partida = 'jogador 1'
        
        print('-=' * 50)
        print('Rodada do %s:' % jogador_da_partida)

        secao_escolhida, numero = valida_entradas(dimensao)

        # revelando números
        for secao in range(dimensao):
            if secao == secao_escolhida - 1:
                # loop que percorre dentro das seções:
                for elemento in range(len(tabuleiro[secao])):
                    if tabuleiro_espelho[secao][elemento] == numero:
                        # verifica se o número já foi revelado
                        if tabuleiro[secao][elemento] == 0:
                            tabuleiro[secao][elemento] = numero
                        else:    
                            print('\nO número %d já foi revelado nessa seção!' % numero)
                            print('O %s perdeu a vez!' % jogador_da_partida)

        imprime_tabuleiro(tabuleiro, dimensao, somas_linhas, somas_colunas)
        pontos_linhas, pontos_colunas, ponto_diagonal = calcula_pontos(tabuleiro, dimensao)

        # atribui pontuação aos jogadores
        for i in range(dimensao):
            chave = 'posicao_' + str(i+1)

            if pontos_linhas[i] == somas_linhas[i]:
                # verifica se a linha já foi revelada
                if linhas_reveladas.get(chave) == None:
                    print('-> A %dª linha foi revelada! O %s recebe %d pontos.' % ((i+1), jogador_da_partida, pontos_linhas[i]))
                    # soma o valor da linha a pontuação do jogador
                    jogadores[jogador_da_partida] += pontos_linhas[i]
                    # adiciona a linha no dicionário de linhas reveladas
                    linhas_reveladas[chave] = True
                    
            if pontos_colunas[i] == somas_colunas[i]:
                # verifica se a coluna já foi revelada
                if colunas_reveladas.get(chave) == None:
                    print('-> A %dª coluna foi revelada! O %s recebe %d pontos.' % ((i+1), jogador_da_partida, pontos_colunas[i]))
                    # soma o valor da coluna a pontuação do jogador
                    jogadores[jogador_da_partida] += pontos_colunas[i]
                    # adiciona a coluna no dicionário de colunas reveladas
                    colunas_reveladas[chave] = True

        if ponto_diagonal == soma_diagonal:
            # verifica se a diagonal já foi revelada
            if diagonal_revelada == False:
                print('-> A diagonal principal foi revelada! O %s recebe %d pontos.' % (jogador_da_partida, (ponto_diagonal*2)))
                # soma o valor da diagonal a pontuação do jogador
                jogadores[jogador_da_partida] += (ponto_diagonal*2)
                # altera o valor booleano para verdadeiro
                diagonal_revelada = True

        print('\nPontuação =', jogadores[jogador_da_partida])

        # verifica se todo o tabuleiro foi revelado
        for secao in range(len(tabuleiro_espelho)):
            if tabuleiro == tabuleiro_espelho:
                partida_continua = False
    
    print('-=' * 50)
    if jogadores['jogador 1'] > jogadores['jogador 2']:
        print('O jogador 1 ganhou a partida com %d pontos!' % jogadores['jogador 1'])
    elif jogadores['jogador 2'] > jogadores['jogador 1']:
        print('O jogador 2 ganhou a partida com %d pontos!' % jogadores['jogador 2'])
    elif jogadores['jogador 1'] == jogadores['jogador 2']:
        print('A partida empatou!')
    print('Fim de jogo!')

# main
menu = True
while menu:
    print('-=' * 50)
    print('''    _                           _                                                  ___        __  
   (_)  ___   __ _   ___     __| |  __ _   ___    ___  ___   _ __    __ _   ___   |_  )      /  \ 
   | | / _ \ / _` | / _ \   / _` | / _` | (_-<   (_-< / _ \ | '  \  / _` | (_-<    / /   _  | () |
  _/ | \___/ \__, | \___/   \__,_| \__,_| /__/   /__/ \___/ |_|_|_| \__,_| /__/   /___| (_)  \__/ 
 |__/        |___/                                                                                ''')

    print('\nOs níveis disponíveis são:')
    print('Nível 1 - tabuleiro 4 x 4')
    print('Nível 2 - tabuleiro 9 x 9')

    # pede o nível que o usuário deseja jogar até que seja digitada uma entrada válida
    while True:
        try:
            nivel = int(input('\nDigite o nível que deseja jogar: '))
            if nivel != 1 and nivel != 2:
                print('Por favor, escolha entre nível 1 ou nível 2.')
            else:
                break
        except:
            print('Entrada inválida! Por favor, tente novamente.')

    if nivel == 1:
        dimensao = 4
    elif nivel == 2:
        dimensao = 9
    
    # inicia uma nova partida
    partida(dimensao)
    
    # após o termino da anterior, pergunta se o usuário deseja iniciar uma nova partida
    print('\nDeseja iniciar uma nova partida?')
    escolha = input('Digite s ou n: ')

    while escolha.lower() != 's' and escolha.lower() != 'n':
        escolha = input('Por favor, digite s ou n:')

    if escolha.lower() == 's':
        pass
    elif escolha.lower() == 'n':
        menu = False
        print('\nPrograma encerrado.')