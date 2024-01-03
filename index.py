# Calculando valor da area:
pi = 3.14159

raio = float (input("digite o raio da circunferência: "))

area = (raio * 2) * pi 

print(f"Área = {area:.4f}")

#Problema 1005:
primeira_nota = float(input())
segunda_nota = float(input())

media = ((primeira_nota * 3.5) + (segunda_nota * 7.5)) / 11

print(f"MEDIA = {media:.5f}")

#problema 1006:
frist_note = float(input())
second_note = float(input())
tree_note = float(input())

media = (
    (frist_note * 2) + (second_note * 3) + (tree_note * 5) 
    ) / 10

print(f"MEDIA = {media:.1f}")

#problema 1007:
primeiro_valor = int(input())
segundo_valor = int(input())
terceiro_valor = int(input())
quarto_valor = int(input())

calculo_diferenca = (primeiro_valor * segundo_valor) - (terceiro_valor * quarto_valor)

print(f"DIFERENÇA = {calculo_diferenca}")

# Problema 1008:
numero_de_funcionario = int(input())
numero_de_horas_trabalhadas = int(input())
valor_recebido_por_hora = float(input())

salario_funcionario = numero_de_horas_trabalhadas * valor_recebido_por_hora

print(f"NUMBER = {numero_de_funcionario}")
print(f"SALARY = R$ {salario_funcionario:.2f}")

# problema 1009:
nome_de_funcionario = (input())
valor_de_vendas_mes = float(input())
salario_fixo_mes = float(input())

valor_de_comicao = valor_de_vendas_mes * 0.15

salario_final = salario_fixo_mes + valor_de_comicao

print(f"SALARIO FINAL = R$ {salario_final}")

# Problema 1010:
numero_de_peca_um, quantidade_de_peca_um, valor_peca_um = map(float, input().split())
numero_de_peca_dois, quantidade_de_peca_dois, valor_peca_dois = map(float, input().split() )  

valor_total_de_pecas = (quantidade_de_peca_um * valor_peca_um) + (quantidade_de_peca_dois * valor_peca_dois)

print(f"VALOR A PAGAR: R$ {valor_total_de_pecas:.2f}")

#problema 1011:
valor_raio = float(input())
valor_de_pi = 3.14159

calculo_do_volume = ((4/3) * valor_de_pi) * (valor_raio ** 3)

print(f"VOLUME = {calculo_do_volume:.3f}")

# Problema 1012:
valor_a = float(input())
valor_b = float(input())
valor_c = float(input())

area_triangulo_rentangulo = (valor_a * valor_c) / 2
area_do_circulo = 3.14159 * (valor_c ** 2)
area_do_trapezio = ((valor_a + valor_b) * valor_c) / 2
area_do_quadrado = valor_b ** 2
area_do_retangulo = valor_a * valor_b

print(f"TRIANGULO: {area_triangulo_rentangulo:.3f}")
print(f"CIRCULO: {area_do_circulo:.3f}")
print(f"TRAPEZIO: {area_do_trapezio:.3f}")
print(f"QUADRADO: {area_do_quadrado:.3f}")
print(f"RETANGULO: {area_do_retangulo:.3f}")

# Problema 1013:
valor_a = int(input())
valor_b = int(input())
valor_c = int(input())

if valor_a > valor_b and valor_a + valor_c:
    print(f"{valor_a} eh o maior")
elif valor_b > valor_a and valor_b > valor_c:
    print (f"{valor_b} eh o maior")
else:
    print(f'{valor_c} eh o maior')
# Outra solução pro problema 1013:
a = int(input())
b = int(input())
c = int(input())


maior_entre_a_e_b = (a + b + abs(a-b)) / 2
maior_entre_a_b_e_c = (maior_entre_a_e_b + c + abs(maior_entre_a_e_b - c)) / 2

print(f"{maior_entre_a_b_e_c} eh o maior !")



# Problema 01 letcode - "twosum":
    
def TwoSum(self, nums: list[int], target: int):
        
        dicionario_de_numeros = {}

        for indice, numeros in enumerate(nums):

            complemento = target - numeros

            if complemento in dicionario_de_numeros:
                return [dicionario_de_numeros[complemento], indice]
            
            dicionario_de_numeros[numeros] = indice
        
        return []
# Outra implementação:
def TwoSum(target: int, numeros: list[int]):
    
    tamanho_da_lista = len(numeros)

    for i in range(tamanho_da_lista):
         for j in range(i + 1, tamanho_da_lista):
              if numeros[j] == target - numeros[i]:
                   return [i, j]