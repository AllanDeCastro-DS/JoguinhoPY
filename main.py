import os
import random as math


def start():
    os.system("clear")



def jogo1():
        start()
        print(f"Você escolheu o jogo 1\n\n")
        print(f"toda vez que você rodar o sistema ira gerar uma sequencia de 3 numeros de 1 a 7.\n\n se os 3 numeros forem iguais você ganha\n\n")

        num1 = ''
        num2 = ''
        num3 = ''

        devmode = int(input("digite 1 para ativar o modo desenvolvedor: "))
    
        if devmode == 1:
            print("modo desenvolvedor ativado\n\n")
            print("no modo desenvolvedor você escolhe os numeros\n")
            num1 = int(input("digite o valor que deseja para ganhar o jogo: \n"))
            num2 = num1
            num3 = num2
            print(f"""
                Os numeros escolhidos foram:
                {num1}, {num2}, {num3}
                
                """)
        

        

        elif devmode != 1:
            num1 = math.randint(1, 8);
            num2 = math.randint(1, 8);
            num3 = math.randint(1, 8);
            print(f"""
                Os numeros escolhidos foram:
                {num1}, {num2}, {num3}
                
                """)

        


        if num1 == num2 and num1 == num3:
            print("Você Ganhou!")

        else:
            replay = int(input('digite 1 para jogar novamente: '))

            if replay == 1:
                    jogo1()

            else:
                    print('Obrigado por jogar')







def escolha():

    jogoescolha = int(input(f"digite o numero 1 para jogar o jogo da sorte, digite 2 para sair: \n"))

    if jogoescolha == 1:
        jogo1()
    else:
        print('Fechando jogo')


if __name__ == "__main__":
    start()
    escolha()