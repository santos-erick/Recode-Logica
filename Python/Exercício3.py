#Exercício3

"""
Uma agência bancária possui dois tipos de investimentos, conforme o quadro abaixo. Faça um algoritmo que receba o tipo do investimento 
e o valor do investimento, calcule e mostre o valor corrigido de acordo com o tipo de investimento.
Tipo - 1 Poupança - 5%
Tipo - 2 Fundo de renda fixa - 10%
"""

investimento = float(input("Digite o valor do investimento que será aplicado: "))

tipo_investimento = int(input("Digite 1 para Poupança(que rende 5%) ou 2 para fundo de renda fixa(que rende 10%): "))



if tipo_investimento == 1:
    print("Você escolheu investir o valor de", investimento, "com rendimento de 5% da Poupança")
    print("O rendimento de 5% de ", investimento, "equivale a: ", investimento * 0.05)
    print("Valor final com rendimento: ", investimento + investimento* 0.05)
    
elif tipo_investimento == 2:
    print("Você escolheu investir o valor de", investimento, "com rendimento de 10% do Fundo de Renda Fixa")
    print("O rendimento de 10% de ", investimento, "equivale a: ", investimento * 0.1)
    print("Valor final com rendimento: ", investimento + investimento* 0.1)
        
else:
    print("Opção inválida!")
    print("Digite 1 para Poupança e 2 para Fundo de Renda Fixa.")
        