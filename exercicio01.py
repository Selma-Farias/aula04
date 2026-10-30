print("Escola Senac\n")
nome = input("Nome:").title()
prova01 = float (input ("prova 01: ").replace(",","."))
prova02 = float (input ("prova 02: ").replace(",","."))
prova03 = float (input ("prova 03: ").replace(",","."))
media = (prova01 + prova02 + prova03)/3
if   media >= 7:
     situacao = "aprovado"
elif media >= 5:
     situacao = "recuperação"
else:
     situacao = "reprovação"     
print("\nResultado:\n")
print(f"Nome:{nome}")
print(f"prova01:{prova01:.1f}".replace(".",","))
print(f"prova02:{prova01:.1f}".replace(".",","))
print(f"prova03:{prova01:.1f}".replace(".",","))
print(f"Média:{media:.1f}".replace(".","."))
print(f"Situação: {situacao.upper()}")