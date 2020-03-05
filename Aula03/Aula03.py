# Polimorfismo, altera o comportamente de acordo com a entrada.
def somar_2_numeros(n1:int,n2:int) -> int:
    return n1+n2

def somar_3_numeros_ultimo_opcional(n1:int,n2:int,n3=1):
    # if n3.isalnum():
    #     n3 = int(n3)
    # else:
    #     del n3
    #     n3 = 1
    return n1*n2*n3

def concatenar_2_strings(s1:str,s2:str):
    return s1+s2

print(somar_2_numeros("a","b"))
print(somar_3_numeros_ultimo_opcional(1,2))
print(concatenar_2_strings("a","b"))

# a = 1
# while a == 1:
#     try:
#         n1 = int(input('Informe o primeiro número: '))
#         n2 = int(input('Informe o segundo número: '))
#         a = 2
#     except ValueError:
#         print('Você deve digitar apenas valores numéricos.')
# n1 = int(input('Informe o primeiro número: '))
# n2 = int(input('Informe o segundo número: '))
# n3 = input('Informe o terceiro número: ')
# s1 = input('Informe a primeira string: ')
# s2 = input('Informe a segunda string: ')

# print(somar_2_numeros(n1,n2))
# print(f'A soma entre {n1} e {n2} é: {somar_2_numeros(n1,n2)}')
# print(f'A multiplicação dos números informados é: {somar_3_numeros_ultimo_opcional(n1,n2,n3)}')
# print(f'As suas string concatenadas são: {concatenar_2_strings(s1,s2)}')
