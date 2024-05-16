import random
from time import sleep
print('\033[32m-=\033[m'*30)
print('\033[1:33m                         JO KEN PO\033[m')
print('\033[32m-=\033[m'*30)
bet = 0
odd = 0
x = 0
select = int(input('Digite 1:'))
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
            print('JO KEN PO NESTE JOGO VOCÊ TEM QUE VENCER O CASSINO \nESCOLHENDO PEDRA PAPEL OU TESOURA..')
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
        print('\033[32m-=\033[m' * 30,'\033[33m')
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
            if obj[casa] == 'Pedra' and obj[opp] == 'Tesoura' or obj[casa] == 'Tesoura' and obj[opp] == 'Papel' or \
                obj[casa] == 'Papel' and obj[opp] == 'Pedra':
                print('\033[31m', 'EliteBet Venceu', '\033[m')
            elif obj[casa] == obj[opp]:
                print('\033[33m', 'EMPATE', '\033[m')
            else:
                print('\033[32m', 'Você Venceu !!', '\033[m')
        print('\033[32m-=\033[m' * 30)