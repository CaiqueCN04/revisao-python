def soma_divisores(numero):
   numero = abs(numero)
   soma = 0
   for i in range(1, numero + 1):
       if numero % i == 0:
           soma += i

   return soma

try:
   num = int(input("Digite um número inteiro: "))
   resultado = soma_divisores(num)
   print(f"A soma de todos os divisores de {num} é: {resultado}")
except ValueError:
   print("Entrada inválida. Certifique-se de inserir um número inteiro.")

 