import os
import random
import sys
from time import sleep
cpf = user = pasw = useradm = paswadm = ''
login = True
resp = c = 0
print('\033[30m','=-'*10,'\033[34m','ELITEBET','\033[30m','=-'*10,'\033[m')
print('')
print('BEM-VINDO AO ELITEBET!')
print('JUNTE-SE A ELITE DA SOCIEDADE ATRAVÉS DAS APOSTAS! ')
print('CADASTRE-SE OU FAÇA SEU LOGIN')
print('')
print('\033[30m','=-'*10,'\033[34m','ELITEBET','\033[30m','=-'*10,'\033[m')
print('DESEJA CADASTRAR-SE OU REALIZAR O LOGIN ?')
print('DIGITE [ 0 ] CADASTRE-SE')
print('DIGITE [ 1 ] LOGIN')
print('DIGITE [ 2 ] PARA SAIR !')
resp = int(input('DIGITE : '))
if resp > 2:
    while resp > 2:
        print('\033[30m''=-'*30)
        print('\033[31mOPÇÃO INCORRETA\033[m')
        print('DESEJA CADASTRAR-SE OU REALIZAR O LOGIN ?')
        print('DIGITE [ 0 ] CADASTRE-SE')
        print('DIGITE [ 1 ] LOGIN')
        print('DIGITE [ 2 ] PARA SAIR !')
        resp = int(input('DIGITE : '))
if resp == 0:
    print('FAÇA O CADASTRO')
    cpf = int(input('Informe o CPF(somente numeros): ').strip())
    useradm = str(input('Informe o Usuario: ').strip())
    paswadm = str(input('Informe a senha: ')).strip()
    print('VOCÊ SE CADASTROU !')
    print('PARA REALIZAR O LOGIN DIGITE [ 1 ] ')
    resp = int(input('DIGITE: '))
    if resp != 1:
        while resp != 1:
            print('\033[31mOPÇÃO INVALIDA ! DIGITE NOVAMENTE ! \033[m')
            print('PARA REALIZAR O LOGIN DIGITE [ 1 ] ')
            resp = int(input('DIGITE: '))
if resp == 1:
    while login == True:
        for c in range(0, 3, +1):
            c += 1
            print('\033[30m', '-' * 52)
            print('\033[34m', 'FAÇA LOGIN EM SUA CONTA', '\033[m')
            print('\033[30m', '-' * 52, '\033[m')
            user = str(input('USUARIO: ').strip())
            pasw = str(input('SENHA: ').strip())
            print('\033[30m', '-' * 52)
            if pasw != paswadm or user != useradm:
                print('\033[31mSENHA OU USUARIO INCORRETOS ! TENTATIVAS {} / 3!\033[m'.format(c))
                if c == 3:
                    print('Conta Suspensa!')
                    sleep(10)
                    print('\033[31mSua conta esta suspensa !\033[m')
                    sleep(5)
                    sys.exit()
            if user == useradm and pasw == paswadm:
                login = True
                print('\033[34m', 'SEJA BEM VINDO AO ELITEBET', '\033[m')
                print('\033[34m', 'PARA ACESSAR O MENU DE JOGOS DIGITE [ 1 ] !', '\033[m')
                menu = int(input('Digite: '))
                if menu == 1:
                    print('\033[34m', '[ MENU DE JOGOS INFORME QUAL DESEJA JOGAR ]', '\033[m')
                    print('\033[30m', '[', '\033[34m', 'JOGOS', '\033[30m', ']', '\033[m')
                    print('\033[30m', '-' * 52, '\033[m')
                    print('[ 0 ] VOCÊ ESTA COM SORTE ?')
                    print('[ 1 ] JO KEN PO !')
                    print('[ 2 ] VIRTUAL FOOTBALL')
                    select = int(input('DIGITE O NUMERO DO JOGO: ').strip())
                    if select != 0 and 1:
                        while select != 0 and select != 1 and select != 2:
                            print('\033[31mOPÇÃO INVALIDA ! DIGITE NOVAMENTE !\033[m')
                            print(' ')
                            print('\033[30m', '[', '\033[34m', 'JOGOS', '\033[30m', ']', '\033[m')
                            print('\033[30m', '-' * 52, '\033[m')
                            print('[ 0 ] VOCÊ ESTA COM SORTE ?')
                            print('[ 1 ] JO KEN PO !')
                            print('[ 2 ] VIRTUAL FOOTBALL')
                            select = int(input('DIGITE O NUMERO DO JOGO: '))
                    #JOGO 0 ESTOU COM SORTE
                    if select == 0:
                        bet = 0
                        x = 0
                        odd = 0
                        print('\033[32m-=\033[m' * 30)
                        print('                 \033[4;32mVOCÊ ESTA COM SORTE ?\033[m')
                        print('\033[32m-=\033[m' * 30)
                        print('\033[1:33mNeste jogo você tem que descobrir em qual numero estou pensando,')
                        print('Quanto maior o seu multiplicador maior a dificuldade !\033[m')
                        print('''\033[1;32m
                        [1]-[JOGAR]\033[m\033[1;31m
                        [2]-[SAIR]\033[m''')
                        print('')
                        print('\033[1:33mINFORME QUAL DESEJA')
                        nv = int(input('DIGITE: \033[m').strip())
                        if nv != 1 and nv != 2:
                            while nv != 1 and nv != 2:
                                print('\033[1;32m[1]-[JOGAR]\033[m')
                                print('\033[1;31m[2]-[SAIR]\033[m')
                                print('')
                                print('\033[1:33mINFORME QUAL DESEJA')
                                nv = int(input('DIGITE: \033[m').strip())
                        if nv == 1:
                            print('\033[32m-=\033[m' * 30)
                            print('                 \033[4;32mVOCÊ ESTA COM SORTE ?\033[m')
                            print('\033[32m-=\033[m' * 30)
                            bet = float(input('\033[1;33mQual o Valor da aposta ?(Minimo R$1.00): '))
                            if bet < 1.0:
                                while bet < 1.0:
                                    print('Valor invalido! Digite um valor acima de R$1.00')
                                    bet = float(input('Digite um valor acima de R$1.00: '))
                            x = float(input('Informe quantos x deseja apostar(Minimo 1.1x): '))
                            if x < 1.1:
                                while x < 1.1:
                                    print('Multiplicador Invalido !')
                                    x = float(input('Digite um multiplicador acima de 1.1x: '))
                            odd = bet * x
                            print('\033[32m-=\033[m' * 30)
                            print('\033[33mVocê apostou R${} em {}x e pode ganhar R${:.2f}'.format(bet, x, odd))
                            print('\033[32m-=\033[m' * 30)
                            print(end='\033[4;33mQual o numero ?')
                            if x >= 1.1 and x <= 1.5:
                                num = random.randint(0, 5)
                                print(' Entre 0 a 5', )
                            elif x > 1.5 and x < 2:
                                num = random.randint(0, 10)
                                print(' Entre 0 a 10')
                            elif x >= 2 and x <= 4:
                                num = random.randint(0, 15)
                                print(' Entre 0 a 15')
                            elif x > 4 and x < 6:
                                num = random.randint(0, 20)
                                print(' Entre 0 a 20')
                            elif x >= 6 and x < 8:
                                num = random.randint(0, 35)
                                print(' Entre 0 a 35')
                            elif x >= 8 and x <= 10:
                                num = random.randint(0, 45)
                                print(' Entre 0 a 45')
                            elif x > 10:
                                num = random.randint(0, 70)
                                print(' Entre 0 a 70')
                            print('\033[m\033[32m-=\033[m' * 30)
                            elite = int(input('\033[m\033[33mQual é o numero? '))
                            if elite == num:
                                print('\033[m\033[32m-=\033[m' * 30)
                                print('\033[33mPARABÉNS VOCÊ ACERTOU O NUMERO É {} !'.format(num))
                                print('\033[m\033[32m-=\033[m' * 30)
                                print('\033[33mVocê recebeu \033[32m+ R${}\033[m \033[33mna sua conta ! '.format(odd))
                            else:
                                print('É uma pena você ERROU !, o numero era {}'.format(num))
                                print('Você perdeu R${} na sua conta !'.format(bet))
                            print('\033[m\033[32m-=\033[m' * 30)
                            menu = int(input('Digite 1 para voltar ao Menu: '))
                            if menu == 1:
                                print('\033[34m', '[ MENU DE JOGOS INFORME QUAL DESEJA JOGAR ]', '\033[m')
                                print('\033[30m', '[', '\033[34m', 'JOGOS', '\033[30m', ']', '\033[m')
                                print('\033[30m', '-' * 52, '\033[m')
                                print('[ 0 ] VOCÊ ESTA COM SORTE ?')
                                print('[ 1 ] JO KEN PO !')
                                select = int(input('DIGITE O NUMERO DO JOGO: ').strip())
                            #FINAL JOGO 0 ESTOU COM SORTE
                            # Fazer o voltar ao inicio
                        if nv == 2:
                            print('EliteBet Saindoo...')
                            sleep(1)
                            print('===== Encerrado =====')
                            sys.exit()
                    #JOGO 1 JOKEN PO
                    if select == 1:
                        print('\033[32m-=\033[m' * 30)
                        print('\033[1:33m                         JO KEN PO\033[m')
                        print('\033[32m-=\033[m' * 30)
                        print('')
                        print('\033[33m[ 0 ] JOGAR !')
                        print('\033[32m[ 1 ] TUTORIAL!')
                        print('\033[31m[ 2 ] SAIR')
                        print('')
                        op = int(input('\033[33mDIGITE :'))
                        if op > 2:
                            while op > 2:
                                print('OPÇÃO INVALIDA')
                                print('')
                                print('\033[33m[ 0 ] JOGAR !')
                                print('\033[32m[ 1 ] TUTORIAL!')
                                print('\033[31m[ 2 ] SAIR')
                                print('')
                                op = int(input('\033[33mDIGITE NOVAMENTE: '))
                        if op == 1:
                            while op != 0:
                                print(
                                    'JO KEN PO NESTE JOGO VOCÊ TEM QUE VENCER O CASSINO \nESCOLHENDO PEDRA PAPEL OU TESOURA..')
                                print('')
                                print('REGRAS DO JOGO:')
                                print('A PEDRA GANHA DA TESOURA E PERDE PARA O PAPEL.')
                                print('A TESOURA GANHA DO PAPEL E PERDE PARA A PEDRA.')
                                print('O PAPEL GANHA DA PEDRA E PERDE PARA A TESOURA.')
                                print('')
                                sleep(1)
                                print('VOCÊ VAI ESCOLHER UM NUMERO SENDO ELE \n[ 0 ] PEDRA  \n[ 1 ] PAPEL  \n[ 2 ] TESOURA')
                                print('E EU VOU ESCOLHER UM TAMBÉM ^^ !')
                                print('')
                                print('ASSIM QUE APARECER JO KEN PO VAMOS SABER QUEM VENCEU !')
                                print('')
                                sleep(1)
                                print('AGORA VAMOS LA !!')
                                op = int(input('\033[33mDIGITE [ 0 ] JOGAR: '))
                        ###APOSTA E MULTIPLICADOR
                        if op == 0:
                            bet = float(input('Qual o valor da aposta ? (Minimo R$1.00) '))
                            if bet < 1:
                                while bet < 1:
                                    print('Valor invalido! Digite um valor acima de R$1.00')
                                    bet = float(input('Qual o valor da aposta ? (Minimo R$1.00) '))
                            print('Quantos X Deseja ? Escolha seu multiplicador: ')
                            print('[1] [ 1.1x ]')
                            print('[2] [ 1.5x ]')
                            print('[3] [ 2.0x ]')
                            print('[4] [ 2.5x ]')
                            print('[5] [ 3.0x ]')
                            print('[6] Para escolher seu multiplicador !')
                            mult = int(input('Informe sua escolha: '))
                            print('\033[32m-=\033[m' * 30, '\033[33m')
                            if mult == 1:
                                x = 1.1
                                print('[Opção 1]')
                                print('Seu multiplicador escolhido foi [ 1.1x ]')
                            elif mult == 2:
                                x = 1.5
                                print('[Opção 2]')
                                print('Seu multiplicador escolhido foi [ 1.5x ]')
                            elif mult == 3:
                                x = 2.0
                                print('[Opção 3]')
                                print('Seu multiplicador escolhido foi [ 2.0x ]')
                            elif mult == 4:
                                x = 2.5
                                print('[Opção 4]')
                                print('Seu multiplicador escolhido foi [ 2.5x ]')
                            elif mult == 5:
                                x = 3.0
                                print('[Opção 5]')
                                print('Seu multiplicador escolhido foi [ 3.0x ]')
                            elif mult == 6:
                                print('[Opção 6]')
                                x = float(input('Quantos X Deseja ? Escolha seu multiplicador: '))
                                print('Seu multiplicador escolhido foi [ {}x ]'.format(x))
                            elif mult > 6:
                                while mult != 6 and mult != 1 and mult != 2 and mult != 3 and mult != 4 and mult != 5:
                                    print('Opção Invalida !')
                                    print('Quantos X Deseja ? Escolha seu multiplicador: ')
                                    print('[1] [ 1.1x ]')
                                    print('[2] [ 1.5x ]')
                                    print('[3] [ 2.0x ]')
                                    print('[4] [ 2.5x ]')
                                    print('[5] [ 3.0x ]')
                                    print('[6] Para escolher seu multiplicador !')
                                    mult = int(input('Informe sua escolha: '))
                            odd = bet * x
                            print('\033[32m-=\033[m' * 30)
                            print('\033[33mVocê apostou R${} em {}x e pode ganhar R${:.2f}'.format(bet, x, odd))
                            print('\033[32m-=\033[m' * 30)
                            #####FINAL APOSTA E MULTIPLICADOR
                            print('\033[1:33m                         JO KEN PO\033[m')
                            print('\033[32m-=\033[m' * 30)
                            obj = ('Pedra', 'Papel', 'Tesoura')
                            casa = random.randint(0, 2)
                            print('\033[33mSuas Opções:')
                            sleep(0.1)
                            print('\033[34m[ 0 ] PEDRA')
                            sleep(0.5)
                            print('[ 1 ] PAPEL')
                            sleep(0.6)
                            print('[ 2 ] TESOURA\033[m')
                            sleep(0.3)
                            opp = int(input('\033[33mQual vai ser sua jogada ?').strip())
                            print('\033[32m-=\033[m' * 30)
                            while opp != 0 and opp != 1 and opp != 2:
                                print('Não Existe essa opção', '\033[31m', 'Tente Novamente !', '\033[m')
                                print('\033[33mSuas Opções:')
                                print('\033[34m[ 0 ] PEDRA')
                                print('[ 1 ] PAPEL')
                                print('[ 2 ] TESOURA\033[m')
                                opp = int(input('\033[33mQual vai ser sua jogada ?').strip())
                                print('\033[32m-=\033[m' * 30)
                            if opp <= 2:
                                sleep(0.5)
                                print('\033[:33m', 'JO', '\033[m')
                                sleep(0.5)
                                print('\033[:33m', '  KEN', '\033[m')
                                sleep(0.5)
                                print('\033[:33m', '     PO !', '\033[m')
                                print('\033[32m-=\033[m' * 30)
                                print('\033[33mEliteBet Jogou {}'.format(obj[casa]))
                                print('Você Jogou {}'.format(obj[opp]))
                                print('\033[m\033[32m-=\033[m' * 30)
                                if obj[casa] == 'Pedra' and obj[opp] == 'Tesoura' or obj[casa] == 'Tesoura' and obj[
                                    opp] == 'Papel' or \
                                        obj[casa] == 'Papel' and obj[opp] == 'Pedra':
                                    print('\033[31m', 'EliteBet Venceu', '\033[m')
                                elif obj[casa] == obj[opp]:
                                    print('\033[33m', 'EMPATE', '\033[m')
                                else:
                                    print('\033[32m', 'Você Venceu !!', '\033[m')
                            print('\033[32m-=\033[m' * 30)
                            menu = int(input('\033[33mDigite [ 1 ] para retornar ao Menu: '))
                            if menu == 1:
                                print('\033[34m', '[ MENU DE JOGOS INFORME QUAL DESEJA JOGAR ]', '\033[m')
                                print('\033[30m', '[', '\033[34m', 'JOGOS', '\033[30m', ']', '\033[m')
                                print('\033[30m', '-' * 52, '\033[m')
                                print('[ 0 ] VOCÊ ESTA COM SORTE ?')
                                print('[ 1 ] JO KEN PO !')
                                select = int(input('DIGITE O NUMERO DO JOGO: ').strip())
                            #FINAL JOGO 1 JOKENPO
                    #JOGO 2 FUTVIRTUAL
                    if select == 2:
                        # FutVirtual
                        # inicio
                        print('\033[1;37m=-=' * 20)
                        print('\033[33m                        FUT VIRTUAL')
                        print('\033[37m=-=' * 20)
                        # Neste jogo vamos ter 2 times por partidas onde vai ser escolhido times aleatorios nas partidas onde eles vão se enfrentar e o usuario vai poder apostar qual vai ganhar ou quantos gols vão ser feitos na partida ao todo ou por cada time.
                        times_brasileirao = ['Athletico-MG', 'Atlético-GO', 'Bahia', 'Botafogo', 'Bragantino',
                                             'Corinthians', 'Criciúma', 'Cruzeiro', 'Cuiabá', 'Flamengo', 'Fluminense',
                                             'Fortaleza', 'Grêmio', 'Internacional', 'Juventude', 'Palmeiras',
                                             'São Paulo', 'Vasco', 'Vitória']
                        multiplicado = [1.05, 1.10, 1.15, 1.29, 1.5, 1.76, 2.0, 2.23, 2.47, 2.5, 3.0, 3.5, 4.0, 4.5,
                                        5.0, 5.5, 6.0, 6.5, 7.0]
                        multiempate = [1.05, 1.10, 1.15, 1.29, 1.5, 1.76, 2.0]
                        mult = random.choice(multiplicado)
                        multe = random.choice(multiempate)
                        timea = random.choice(times_brasileirao)
                        timeb = random.choice(times_brasileirao)
                        gols_timea = random.randint(0, 7)
                        gols_timeb = random.randint(0, 7)
                        if timea == timeb:
                            while timea == timeb:
                                timea = random.choice(times_brasileirao)
                                timeb = random.choice(times_brasileirao)
                        print('\033[33m                        BRASILEIRÃO')
                        print('\033[37m=-='*20)
                        print('\033[33m               {}      x      {}'.format(timea.upper(), timeb.upper()))
                        print('\033[37m=-='*20)
                        #MENU DE APOSTAS
                        print('\033[33mMENU DE APOSTAS')
                        print('\033[33m[ 1 ]\033[37m PLACAR')
                        print('\033[33m[ 2 ]\033[37m GOLS')
                        print('\033[33m[ 3 ]\033[37m VITORIA OU EMPATE')
                        while True:
                            menu = input('Digite: ')
                            if menu.isdigit():  
                                menu = int(menu)
                                if menu < 1 or menu > 3:
                                    print('\033[1;31mPor favor, digite uma opção válida\033[m')  
                                if menu in [1, 2, 3]:
                                    break
                            else:
                                print('\033[1;31mPor favor, digite uma opção válida\033[m')  
                        # ENQUANTO VALOR DIGITADO FOR INCORRETO VAI SE REPETIR O MENU ATÉ DIGITAR UM NUMERO VALIDO
                        print('\033[37m=-=\033[m' * 20)
                        os.system('cls')
                        #USUARIO ESCOLHER A OPÇÃO 1 APOSTAR NO PLACAR
                        if menu == 1:
                            print('\033[1;33mPLACAR')
                            print('\033[37mA ODD do PLACAR esta em \033[1;33m[{}]'.format(mult))
                            #VALOR QUE O USUARIO DESEJA APOSTAR
                            print('\033[1;37mDeseja apostar quantos R$ no placar ? ')
                            #IDENTIFICADOR SE O NUMERO É VALIDO OU É STR ENQUANTO O USUARIO NÃO DIGITA UM NUMERO VALIDO VAI SER REPETIDO A SOLICITAÇÃO 
                            while True:
                                odd = input('Digite: ')
                                if odd.replace('.','').isdigit():
                                    numb = float(odd)
                                    break
                                else:
                                    print('\033[31mPor favor, digite um número válido\033[m')
                            print('Informe quanto vai ser o placar do jogo entre \n\033[1;33m{} x {}'.format(timea, timeb))
                            print('\033[1;37mQuantos gols do \033[1;33m{} ?\033[1;37m'.format(timea))
                            #QUANTIDADE DE GOLS DO TIME 1
                            #IDENTIFICADOR SE O NUMERO É VALIDO INTEIRO OU É STR ENQUANTO O USUARIO NÃO DIGITA UM NUMERO VALIDO VAI SER REPETIDO A SOLICITAÇÃO 
                            while True:
                                placartimea = input('Digite: ')
                                if placartimea.isdigit():
                                    resulta = int(placartimea)
                                    break
                                else:
                                    print('\033[1;31mPor favor, digite um número válido\033[m')
                            print('Quantos gols do \033[1;33m{} ?\033[1;37m'.format(timeb))
                            #QUANTIDADE DE GOLS DO TIME 2
                            while True:
                                placartimeb = input('Digite: ')
                                if placartimeb.isdigit():
                                    resultb = int(placartimeb)
                                    break
                                else:
                                    print('\033[1;31mPor favor, digite um número válido\033[m')
                            forra = numb * mult
                            print('Você apostou R${} no placar \033[1;33m{} {} x {} {} \033[1;37mpodendo ganhar R${}, Boa Sorte !!'.format(odd, timea, resulta, resultb, timeb, forra))
                            #FORMAS DE MOSTRAR O RESULTADO DA PARTIDA
                            print('\033[1;33m[ 1 ] \033[1;37mResultado mostrando Gols')
                            print('\033[1;33m[ 2 ] \033[1;37mResultado direto')
                            #ENQUANTO VALOR DIGITADO FOR INCORRETO VAI SE REPETIR O MENU ATÉ DIGITAR UM NUMERO VALIDO
                            while True:
                                select = input('Digite: ')
                                if select.isdigit():  
                                    select = int(select)
                                    if select < 1 or select > 2:
                                        print('\033[1;31mPor favor, digite uma opção válida\033[m')  
                                    if select in [1, 2]:
                                        break
                                else:
                                    print('\033[1;31mPor favor, digite uma opção válida\033[m')
                            print('\033[37m=-=\033[m'*20)
                            #SE O USUARIO DESEJAR VER OS GOLS DA PARTIDA
                            if select == 1:
                                #MOSTRAS OS GOLS FEITOS PELO TIME 1
                                for x in range(gols_timea):
                                    print('Goool do {}'.format(timea))
                                    sleep(1)
                                #MOSTRA OS GOLS FEITOS PELO TIME 2
                                for x in range(gols_timeb):
                                    print('Goool do {}'.format(timeb))
                                    sleep(1)
                                print('\033[35m=-=' * 20)
                                print('{} {} x {} {}'.format(timea, gols_timea, gols_timeb, timeb))
                            #SE O USUARIO ESCOLHER O RESULTADO DIRETO SO MOSTRA O PLACAR FINAL
                            if select == 2:
                                print('\033[1;33mPALPITE\033[m')
                                print('\033[1;33m{} \033[1;37m{} \033[1;33mx \033[1;37m{} \033[1;33m{} \033[1;37m'.format(timea, resulta, resultb, timeb))
                                print('\033[37m=-=\033[m' * 20)
                                #COMPARADOR DE PLACAR SE FOR IGUAL AO RESULTADO PALPITE CERTO SE NAO PALPITE ERRADO
                                if resulta == gols_timea and resultb == gols_timeb:
                                    print('\033[1;37mQue Belo Palpite você acertou foram depositados na sua conta \033[1;32m+ R${}'.format(forra))
                                else:
                                    print('\033[1;37mNão foi dessa vez, você errou o palpite e perdeu \033[31mR${}'.format(odd))
                        #MENU DE GOLS
                        if menu == 2:
                            print('\033[1;33mMENU DE GOLS\033[m')
                            print('\033[1;37mDeseja apostar em qual ?')
                            print('\033[1;33m[ 1 ] \033[1;37mPalpite de gols do \033[1;33m{}'.format(timea))
                            print('\033[1;33m[ 2 ] \033[1;37mPalpite de gols do \033[1;33m{}'.format(timeb))
                            print('\033[1;33m[ 3 ] \033[1;37mPalpite de quantos GOLS vão sair na partida entre \033[1;33m{} x {}\033[1;37m'.format(timea, timeb))

                            while True:
                                select = input('Digite: ')
                                if select.isdigit():  
                                    select = int(select)
                                    #ENQUANTO VALOR DIGITADO FOR INCORRETO VAI SE REPETIR A SOLICITAÇÃO DE UM NUMERO VALIDO
                                    if select < 1 or select > 3:
                                        print('\033[1;31mPor favor, digite uma opção válida\033[m')  
                                    if select in [1, 2, 3]:
                                        break
                                else:
                                    print('\033[1;31mPor favor, digite uma opção válida\033[m')  
                            #SE O USUARIO ESCOLHER A OPÇÃO 1
                            if select == 1:
                                print('A ODD de palpite de GOLS do \033[1;33m{}\033[1;37m esta em \033[1;33m[{}]'.format(timea, mult))
                                print('\033[1;37mDeseja apostar quantos \033[1;33mR$ \033[1;37mneste palpite ? ')
                                #IDENTIFICA SE É UM NUMERO DIGITA OU STR 
                                while True:
                                    odd = input('Digite: ')
                                    if odd.replace('.','').isdigit():
                                        odd = float(odd)
                                        break
                                    else:
                                        print('\033[31mPor favor, digite um número válido\033[m')
                                forra = mult * odd
                                print('Qual é seu palpite ? Quantos GOLS o \033[1;33m{}\033[1;37m vai fazer ?'.format(timea))
                                #IDENTIFICA SE É UM NUMERO INTEIRO OU STR
                                while True:
                                    palpite = input('Digite: ')
                                    if palpite.isdigit():
                                        palpite = int(palpite)
                                        break
                                    else:
                                        print('\033[1;31mPor favor, digite um número válido\033[m')
                                print('Você apostou \033[1;33mR${} \033[1;37mque o \033[1;33m{} \033[1;37mvai fazer \033[1;33m{} \033[1;37mGOLS e pode receber \033[1;33mR${:.2f} \033[1;37mpelo palpite \033[1;33mBoa Sorte !'.format(odd, timea, palpite, forra))
                                sleep(5)
                                if palpite == gols_timea:
                                    print('\033[1;37mQue Belo Palpite você acertou ! \nForam depositados na sua conta \033[322m+ R${}\033[1;37m'.format(forra))
                                else:
                                    print('\033[37m=-=\033[m' * 20)
                                    print('Não foi dessa vez, você errou o palpite e perdeu \033[1;31mR${}'.format(odd))
                            #SE O USUARIO ESCOLHER A OPÇÃO 2
                            if select == 2:
                                print('A ODD de palpite de GOLS do \033[1;33m{} \033[1;37mesta em \033[1;33m[{}]'.format(timeb, mult))
                                print('Deseja apostar quantos \033[1;33mR$ \033[1;37mneste palpite ? ')

                                #IDENTIFICA SE É UM NUMERO DIGITA OU STR 
                                while True:
                                    odd = input('Digite: ')
                                    if odd.replace('.','').isdigit():
                                        odd = float(odd)
                                        break
                                    else:
                                        print('\033[31mPor favor, digite um número válido\033[m')
                                forra = mult * odd
                                print('Qual é seu palpite ? Quantos GOLS o \033[1;33m{}\033[1;37m vai fazer ?'.format(timeb))

                                #IDENTIFICA SE É UM NUMERO INTEIRO OU STR
                                while True:
                                    palpite = input('Digite: ')
                                    if palpite.isdigit():
                                        palpite = int(palpite)
                                        break
                                    else:
                                        print('\033[1;31mPor favor, digite um número válido\033[m')
                                print('Você apostou \033[1;33mR${}\033[1;37m que o \033[1;33m{}\033[1;37m vai fazer \033[1;33m{}\033[1;37m GOLS e pode receber \033[1;33mR${} \033[1;37mpelo palpite \033[1;33mBoa Sorte !\033[1;37m'.format(odd, timeb, palpite, forra))
                                sleep(5)
                                if palpite == gols_timeb:
                                    print('Que Belo Palpite você acertou ! \nForam depositados na sua conta \033[1;32m+ R${:.2f}'.format(forra))
                                else:
                                    print('Não foi dessa vez, você errou o palpite e perdeu \033[1;31mR${}\033[1;37m'.format(odd))
                            #SE O USUARIO ESCOLHER A OPÇÃO 3
                            if select == 3:
                                print('A ODD de quantos GOLS vão sair entre \033[1;33m{} x {} \033[1;37mesta em \033[1;33m[{}]\033[1;37m'.format(timea, timeb, mult))
                                print('Deseja apostar quantos \033[1;33mR$\033[1;37m neste palpite ? ')
                            
                                #IDENTIFICA SE É UM NUMERO DIGITA OU STR 
                                while True:
                                        odd = input('Digite: ')
                                        if odd.replace('.','').isdigit():
                                            odd = float(odd)
                                            break
                                        else:
                                            print('\033[31mPor favor, digite um número válido\033[m')
                                forra = mult * odd
                                print('Qual é seu palpite ? Informe quantos Gols vão sair entre \033[1;33m{} x {}\033[1;37m'.format(timea, timeb))
                                palpite = int(input('Digite: '))
                                #IDENTIFICA SE É UM NUMERO INTEIRO OU STR
                                while True:
                                    palpite = input('Digite: ')
                                    if palpite.isdigit():
                                        palpite = int(palpite)
                                        break
                                    else:
                                        print('\033[1;31mPor favor, digite um número válido\033[m')
                                print('Você apostou \033[1;33mR${} \033[1;37mque no jogo entre \033[1;33m{} x {} \033[1;37mvai ser feito \033[1;33m{} \033[1;37mGOLS. Podendo receber neste palpite \033[1;33mR${}\033[1;37m'.format(odd, timea, timeb, palpite, forra))
                                print('\033[1;37m=-=' * 20)
                                sleep(5)
                                result = gols_timea + gols_timeb
                                if palpite == result:
                                    print('Que Belo Palpite você acertou ! \nForam depositados na sua conta \033[1;32m+ R${}\033[1;37m'.format(forra))
                                else:
                                    print('\033[1;37mNão foi dessa vez, você errou o palpite e perdeu \033[1;31mR${}'.format(odd))
                        #MENU DE VITORIA OU EMPATE
                        if menu == 3:
                            print('\033[1;33mMENU VITORIA OU EMPATE\033[1;37m')
                            print('''Deseja apostar em qual dos times 
                        \033[1;33m[ 1 ]\033[1;37m {} 
                        \033[1;33m[ 2 ] \033[1;37m{}
                        \033[1;33m[ 3 ] \033[1;37mEMPATE'''.format(timea, timeb))
                            
                            while True:
                                time = input('Digite: ')
                                if time.isdigit():  
                                    time = int(time)
                                    #ENQUANTO VALOR DIGITADO FOR INCORRETO VAI SE REPETIR A SOLICITAÇÃO DE UM NUMERO VALIDO
                                    if time < 1 or time > 3:
                                        print('\033[1;31mPor favor, digite uma opção válida\033[m')  
                                    if time in [1, 2, 3]:
                                        break
                                else:
                                    print('\033[1;31mPor favor, digite uma opção válida\033[m')  
                            print('\033[1;37m=-=\033[m' * 20)
                            # OPÇÃO 1 VITORIA DO TIME 1 ou VITORIA E EMPATE
                            if time == 1:
                                print('\033[1;33m[ 1 ] \033[1;37mVitoria do \033[1;33m{}\033[1;37m ODD em \033[1;33m[{}]\033[1;37m'.format(timea, mult))
                                print('\033[1;33m[ 2 ] \033[1;37mVitoria do \033[1;33m{} \033[1;37mou Empate ODD em \033[1;33m[{}]\033[1;37m'.format(timea, multe))

                                while True:
                                    palpite = input('Digite: ')
                                    if palpite.isdigit():  
                                        palpite = int(palpite)
                                        #ENQUANTO VALOR DIGITADO FOR INCORRETO VAI SE REPETIR A SOLICITAÇÃO DE UM NUMERO VALIDO
                                        if palpite < 1 or palpite > 2:
                                            print('\033[1;31mPor favor, digite uma opção válida\033[m')  
                                        if palpite in [1, 2]:
                                            break
                                    else:
                                        print('\033[1;31mPor favor, digite uma opção válida\033[m')  
                                print('\033[1;37m=-=\033[m' * 20)
                                #VALOR A APOSTAR SEGUIDO DE RESULTADO DO PALPITE NAS CORES VERDE E VERMELHA
                                if palpite == 1:
                                    print('\033[1;37mDeseja apostar quantos \033[1;33mR$ \033[1;37mneste palpite ? ')
                                    #IDENTIFICA SE É UM NUMERO DIGITA OU STR 
                                    while True:
                                        odd = input('Digite: ')
                                        if odd.replace('.','').isdigit():
                                            odd = float(odd)
                                            break
                                        else:
                                            print('\033[31mPor favor, digite um número válido\033[m')
                                    forra = mult * odd
                                    #SE O USUARIO ACERTAR O PALPITE DA VITORIA DO TIME 1
                                    if gols_timea > gols_timeb:
                                        print('\033[1;37mVitoria do \033[1;33m{}\033[1;37m'.format(timea))
                                        print('Você apostou na Vitoria do \033[1;33m{} \033[1;37mACERTOU o Palpite e foram depositados na sua conta \033[1;32mR${}\033[1;37m'.format(timea, forra))
                                    #SE O USUARIO ERRAR O PALPITE DA VITORIA DO TIME 1
                                    else:
                                        print('\033[1;37mDerrota do \033[1;33m{}'.format(timea))
                                        print('Você apostou na Vitoria do \033[1;33m{} \033[1;37me ERROU o palpite perdendo o valor depositado \033[1;31mR${}'.format(timea, odd))
                                #VALOR A APOSTAR SEGUIDO DE VITORIA OU VITORIA E EMPATE DO TIME ESCOLHIDO
                                if palpite == 2:
                                    print('\033[1;37mDeseja apostar quantos \033[1;33mR$\033[1;37m neste palpite ? ')

                                    while True:
                                        odd = input('Digite: ')
                                        if odd.replace('.','').isdigit():
                                            odd = float(odd)
                                            break
                                        else:
                                            print('\033[31mPor favor, digite um número válido\033[m')
                                    print('\033[1;37m=-=\033[m' * 20)
                                    forra = multe * odd
                                    #VITORIA OU EMPATE DO TIME 1
                                    if gols_timea > gols_timeb or gols_timea == gols_timeb:
                                        #SE O TIME 1 VENCER
                                        if gols_timea > gols_timeb:
                                            print('\033[1;37mVitoria\033[m do \033[1;33m{}\033[1;37m'.format(timea))
                                            print('Você apostou na Vitoria do \033[1;33m{} \033[1;37mou EMPATE. ACERTOU o Palpite e foram depositados na sua conta \033[1;32mR${}'.format(timea, forra))
                                        #SE O TIME 1 VENCER OU EMPATAR
                                        if gols_timea == gols_timeb:
                                            print('\033[33mEMPATE\033[m entre \033[1;33m{} x {}\033[1;37m'.format(timea, timeb))
                                            print('Você apostou na Vitoria do \033[1;33m{} \033[1;37mou EMPATE. ACERTOU o Palpite e foram depositados na sua conta \033[1;32mR${}'.format(timea, forra))
                                    #SE O USUARIO ERRAR O PALPITE
                                    else:
                                        print('\033[1;37mDerrota do \033[1;33m{}\033[1;37m'.format(timea))
                                        print('Você apostou na Vitoria do \033[1;33m{} \033[1;37mou EMPATE.  ERROU o palpite perdendo o valor depositado \033[1;31mR${}\033[1;37m'.format(timea,odd))
                            #SE O USUARIO ESCOLHER A OPÇÃO 2 VITORIA DO TIME 2 OU VITORIA E EMPATE
                            if time == 2:
                                print('\033[1;33m[ 1 ] \033[1;37mVitoria do \033[1;33m{} \033[1;37mODD em \033[1;33m[{}]\033[1;37m'.format(timeb, mult))
                                print('\033[1;33m[ 2 ] \033[1;37mVitoria do \033[1;33m{} \033[1;37mou Empate ODD em \033[1;33m[{}]\033[1;37m'.format(timeb, multe))

                                while True:
                                    palpite = input('Digite: ')
                                    if palpite.isdigit():  
                                        palpite = int(palpite)
                                        #ENQUANTO VALOR DIGITADO FOR INCORRETO VAI SE REPETIR A SOLICITAÇÃO DE UM NUMERO VALIDO
                                        if palpite < 1 or palpite > 2:
                                            print('\033[1;31mPor favor, digite uma opção válida\033[m')  
                                        if palpite in [1, 2]:
                                            break
                                    else:
                                        print('\033[1;31mPor favor, digite uma opção válida\033[m')  

                                if palpite == 1:
                                    print('Deseja apostar quantos \033[1;33mR$ \033[1;37mneste palpite ? ')
                                    #IDENTIFICA SE É UM NUMERO DIGITA OU STR 
                                    while True:
                                        odd = input('Digite: ')
                                        if odd.replace('.','').isdigit():
                                            odd = float(odd)
                                            break
                                        else:
                                            print('\033[31mPor favor, digite um número válido\033[m')
                                    print('\033[1;37m=-=\033[m' * 20)
                                    forra = mult * odd
                                    #SE O USUARIO ACERTAR O PALPITE DA VITORIA
                                    if gols_timeb > gols_timea:
                                        print('\033[1;37mVitoria do \033[1;33m{}\033[1;37m'.format(timeb))
                                        print('Você apostou na Vitoria do \033[1;33m{} \033[1;37mACERTOU o Palpite e foram depositados na sua conta \033[1;32mR${}\033[1;37m'.format(timeb, forra))
                                    #SE O USUARIO ERRAR O PALPITE
                                    else:
                                        print('\033[1;37mDerrota do \033[1;33m{}\033[1;37m'.format(timeb))
                                        print('Você apostou na Vitoria do \033[1;33m{} \033[1;37me ERROU o palpite perdendo o valor depositado \033[1;31mR${}'.format(timeb,odd))
                                # VALOR A APOSTAR SEGUIDO DE VITORIA OU VITORIA E EMPATE DO TIME ESCOLHIDO
                                if palpite == 2:
                                    print('Deseja apostar quantos \033[1;33mR$ neste \033[1;37mpalpite ? ')
                                    #IDENTIFICA SE É UM NUMERO DIGITA OU STR 
                                    while True:
                                        odd = input('Digite: ')
                                        if odd.replace('.','').isdigit():
                                            odd = float(odd)
                                            break
                                        else:
                                            print('\033[31mPor favor, digite um número válido\033[m')
                                    print('\033[1;37m=-=\033[m' * 20)
                                    forra = multe * odd
                                    if gols_timeb > gols_timea or gols_timeb == gols_timea:
                                        #CASO O USUARIO ACERTE A VITORIA
                                        if gols_timeb > gols_timea:
                                            print('\033[1;37mVitoria do \033[1;33m{}\033[1;37m'.format(timeb))
                                            print('Você apostou na Vitoria do \033[1;33m{} \033[1;37mou EMPATE. ACERTOU o Palpite e foram depositados na sua conta \033[1;32mR${}'.format(timeb, forra))
                                        #CASO O USUARIO ACERTE O EMPATE
                                        if gols_timeb == gols_timea:
                                            print('\033[1;37mEMPATE entre \033[1;33m{} x {}\033[1;37m'.format(timeb, timea))
                                            print('Você apostou na Vitoria do \033[1;33m{} \033[1;37mou EMPATE. ACERTOU o Palpite e foram depositados na sua conta \033[1;32mR${}\033[1;37m'.format(timeb, forra))
                                    #CASO O USUARIO ERRE O PALPITE
                                    else:
                                        print('\033[1;37mDerrota do \033[1;33m{}\033[1;37m'.format(timeb))
                                        print(
                                            'Você apostou na Vitoria do \033[1;33m{} \033[1;37mou EMPATE.  ERROU o palpite perdendo o valor depositado \033[1;31mR${}\033[1;37m'.format(
                                                timeb, odd))
                            #SE O USUARIO ESCOLHER A OPÇÃO 3 EMPATE
                            if time == 3:
                                print('\033[1;33mEMPATE \033[1;37mODD \033[1;33m[{}]\033[1;37m'.format(mult))
                                print('Deseja apostar quantos \033[1;33mR$ \033[1;37mneste palpite ? ')
                                #IDENTIFICA SE É UM NUMERO DIGITA OU STR 
                                while True:
                                    odd = input('Digite: ')
                                    if odd.replace('.','').isdigit():
                                        odd = float(odd)
                                        break
                                    else:
                                        print('\033[31mPor favor, digite um número válido\033[m')
                                print('\033[1;37m=-=\033[m' * 20)
                                forra = mult * odd
                                #MOSTRA SE O USUARIO ACERTAR O EMPATE
                                if gols_timea == gols_timeb:
                                    print('\033[1;37mEMPATE entre \033[1;33m{} x {}\033[1;37m'.format(timeb, timea))
                                    print('Você apostou no EMPATE. ACERTOU o Palpite e foram depositados na sua conta \033[1;32mR${}\033[1;37m'.format(forra))
                                #MOSTRA QUEM VENCEU CASO O USUARIO ERRE O PALPITE
                                else:
                                    if gols_timea > gols_timeb:
                                        print('\033[1;33m{} \033[1;37mVenceu '.format(timea))
                                        print('Você apostou no EMPATE e acabou perdendo o valor depositado \033[1;31mR${}\033[1;37m'.format(odd))
                                    if gols_timeb > gols_timea:
                                        print('\033[1;33m{} \033[1;37mVenceu '.format(timeb))
                                        print('Você apostou no EMPATE e acabou perdendo o valor depositado \033[1;31mR${}\033[1;37m'.format(odd))
                        # RESULTADO DO JOGO FINAL
                        print('\033[1;37m=-=\033[m' * 20)
                        print('\033[1;33mRESULTADO DO JOGO \033[m')
                        if gols_timea > gols_timeb:
                            print(
                                '\033[1;33m{} \033[1;37m{} \n\033[1;33m{} \033[1;37m{}'.format(timea, gols_timea, timeb,
                                                                                               gols_timeb))
                        if gols_timeb > gols_timea:
                            print(
                                '\033[1;33m{} \033[1;37m{} \n\033[1;33m{} \033[1;37m{}'.format(timeb, gols_timeb, timea,
                                                                                               gols_timea))
                        if gols_timea == gols_timeb:
                            print(
                                '\033[1;33m{} \033[1;37m{} \n\033[1;33m{} \033[1;37m{}'.format(timea, gols_timea, timeb,
                                                                                               gols_timeb))
                        print('\033[1;37m=-=\033[m' * 20)
    if resp >= 3:
        print('\033[31mNumero incorreto !')
        resp = int(input('Digite novamente: \033[m'))
else:
    print('EliteBet Saindoo...')
    sleep(1)
    print('===== Encerrado =====')
    sys.exit()