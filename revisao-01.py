# Aprendizagem e revisão da linguagem Python

# Comentário: descreve a intenção do trecho do codigo-fonte
print("olá, Python!")
print("A soma é:", (3 + 5))
print("\n")

# Variáveis e tipos
nome ="Ana"
idade = 17
altura = 1.65
matriculado = True

for valor in [nome, idade, altura, matriculado]: 
    print(valor, type(valor))

print("\n")

# Entrada de dados e conversão
nome = input("Nome: ")
idade = int(input("Idade: "))
print(f"{nome} terá {idade + 1} anos no próximo aniversário!")

print("Tipo do nome:",type(nome))
print("Tipo da idade:",type(idade))
print("\n")

# Operações aritméticas
a, b = 10, 3
print(( a + b), (a - b), (a * b ))
print((a / b), (a // b), (a % b), (a ** b))
print("Par?", 12 % 2 == 0)
print("\n")

idade = 19
autorizado=True
print(idade >= 18 and autorizado)
print(idade < 18 or not autorizado)
print(idade == 19, idade != 19)
print("\n")

#Decisões com if, elif e else
nota = float(input("Nota:  "))
if nota >= 7:
    print("Aprovado, parabéns!")
elif nota >= 5:
    print("Cuidado, Recuperação!")
else:
    print ("Infelizmente foi reprovado")

print("\n")