#Ler o ano atual e o ano de nascimento de uma pessoa. Escrever uma mensagem que diga se ela poderá ou não votar este ano (não é necessário considerar o mês em que a pessoa nasceu)

print("#"*70)
ano_atual = int(input("Insira o ano atual : "))
ano_nascimento = int(input("Insira o ano de nascimento : "))
print("#"*70)
calculo = ano_atual - ano_nascimento
if calculo < 16 : 
    print ("Você não pode votar  ")
else:
    print ("Você Pode votar !! ")
    
print("#"*70)