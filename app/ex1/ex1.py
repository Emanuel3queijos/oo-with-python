coddigo = 10
salario = 1500.9
nome = "jose"
situiacao = True

print("codigo:", coddigo, "salario:", salario, "Nome:", nome)
# mesma coisa praticamente
print("codigo: " + str(coddigo) + " salario: " + str(salario) + " Nome: " + str(nome))


print("codigo: %d " % coddigo)

# defininr o tipo de variavl que a gente quer receber no imput

fruta = input("digite o nome de uma fruta: ")
print(fruta)

qtdFruta = int(input("digite quantas frutas voce quer: "))
print("tome aqui suas " + str (qtdFruta) + fruta+"s")


