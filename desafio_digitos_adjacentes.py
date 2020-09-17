num = int(input("Digite um número: "))
tam = len(str(num))

num_rep = 0

while tam > 0:
	if num != 0:
		d = num % 10
		num = num // 10
		ds = num % 10
		if d == ds:
			num_rep = num_rep + 1
	tam = tam - 1 

if num_rep != 0:
	print("Existem algarismos repetidos")
else:
	print("Não existem algarismos repetidos")
