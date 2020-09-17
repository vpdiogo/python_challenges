num = int(input("Digite um número: "))
tam = len(str(num))

soma = 0

while tam > 0:
	d = num % 10
	soma = soma + d
	num = num // 10
	tam = tam - 1 

print("A soma dos dígitos desse número é: ", soma)
