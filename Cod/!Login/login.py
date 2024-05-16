import random
import sys
from time import sleep
cpf = ''
user = ''
pasw = ''
useradm = ''
paswadm = ''
login = True
resp = 0
c = 0
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
    paswadm = input('Informe a senha: ').strip()
    print('VOCÊ SE CADASTROU !')
    print('PARA REALIZAR O LOGIN DIGITE [ 1 ] ')
    resp = int(input('DIGITE: '))
if resp == 1:
    while login == True:
        for c in range(3, 0, -1):
            c -= 1
            print('\033[30m', '-' * 52)
            print('\033[34m', 'FAÇA LOGIN EM SUA CONTA', '\033[m')
            print('\033[30m', '-' * 52, '\033[m')
            user = str(input('USUARIO: ').strip())
            pasw = str(input('SENHA: ').strip())
            if user == useradm and pasw == paswadm:
                login = True
                print('\033[34m', 'SEJA BEM VINDO AO ELITEBET', '\033[m')
                print('\033[34m', 'INFORME QUAL JOGO DESEJA JOGAR !', '\033[m')
                print('\033[30m', '[', '\033[34m', 'JOGOS', '\033[30m', ']', '\033[m')
                print('\033[30m', '-' * 52, '\033[m')
                print('[ 0 ] VOCÊ ESTA COM SORTE ?')
                print('[ 1 ] JO KEN PO !')
                select = int(input('DIGITE O NUMERO DO JOGO: ').strip())
            elif pasw != paswadm:
                print(c)
                print('\033[31mSENHA INCORRETA VOCÊ TEM MAIS {} TENTATIVAS !\033[m'.format(c))
                if c == 0:
                    print('Conta Suspensa!')
                    sleep(10)
                    print('\033[31mSua conta esta suspensa durante 5s !\033[m')
                    sleep(5)
                    sys.exit()
            else:
                print('\033[31mUSUARIO OU SENHA ESTÃO INCORRETOS !\033[m')
    if resp >= 3:
        print('\033[31mNumero incorreto !')
        resp = int(input('Digite novamente: \033[m'))


else:
    print('EliteBet Saindoo...')
    sleep(1)
    print('===== Encerrado =====')
    sys.exit()