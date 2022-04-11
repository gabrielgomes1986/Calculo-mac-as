#As maçãs custam R$ 1,30 cada se forem compradas menos de uma dúzia, e R$ 1,00 se forem compradas pelo menos 12. Escreva um programa que leia o número de maçãs compradas, calcule e escreva o custo total da compra.

print("#"*60)
print("Olá , digite quantas maças deseja comprar : ")
print("#"*60)
n_macas = int(input("Insira a quantiadade : "))
print("#"*60)
if n_macas < 12 :
    calcule = n_macas * 1.30
    print(f"O custo total da compra foi : {calcule}")
elif n_macas >= 12 :
    calcule = n_macas * 1
    print(f"O custo total da compra foi : {calcule}")
else : 
    print("Não foi possivel calcular.")