#Exercício 1 

#Algoritmo que leia um valor de um produto e mostre o novo valor atualizado com 25% de desconto.

produto = float(input("Digite o valor do produto: R$ "))

desconto = produto * 0.25

produto_desconto = produto - desconto

print("O valor do produto com desconto é ",produto_desconto);