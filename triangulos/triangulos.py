# Função para verificar semelhança pelo critério Lado-Ângulo-Lado (LAL)
def verificar_lal(lados1, angulo1, lados2, angulo2):
    # Lados são proporcionais e o ângulo entre eles é congruente
    if (lados1[0] / lados2[0] == lados1[1] / lados2[1]) and (angulo1 == angulo2):
        return True
    return False

# Função para verificar semelhança pelo critério Ângulo-Ângulo (AA)
def verificar_aa(angulos1, angulos2):
    # Dois ângulos são congruentes
    if (angulos1[0] == angulos2[0] and angulos1[1] == angulos2[1]) or \
       (angulos1[0] == angulos2[1] and angulos1[1] == angulos2[0]):
        return True
    return False

# Função para verificar semelhança pelo critério Lado-Lado-Lado (LLL)
def verificar_lll(lados1, lados2):
    # Todos os lados são proporcionais
    if (lados1[0] / lados2[0] == lados1[1] / lados2[1] == lados1[2] / lados2[2]):
        return True
    return False

# Função principal para verificar a semelhança dos triângulos com base nos critérios
def verificar_seme1hanca(triangulo1, triangulo2):
    # Verificação pelo critério LAL
    if 'lados' in triangulo1 and 'angulo' in triangulo1:
        if verificar_lal(triangulo1['lados'], triangulo1['angulo'], triangulo2['lados'], triangulo2['angulo']):
            return "Os triângulos são semelhantes pelo critério LAL."
    
    # Verificação pelo critério AA
    if 'angulos' in triangulo1 and 'angulos' in triangulo2:
        if verificar_aa(triangulo1['angulos'], triangulo2['angulos']):
            return "Os triângulos são semelhantes pelo critério AA."
    
    # Verificação pelo critério LLL
    if 'lados' in triangulo1 and 'lados' in triangulo2:
        if verificar_lll(triangulo1['lados'], triangulo2['lados']):
            return "Os triângulos são semelhantes pelo critério LLL."
    
    return "Os triângulos não são semelhantes."

# Solicitando dados do usuário para cada critério
print("Digite as informações dos triângulos para verificar semelhança.")
tipo_criterio = input("Escolha o critério de semelhança (LAL, AA, LLL): ").strip().upper()

if tipo_criterio == "LAL":
    # Dados para LAL
    lados1 = list(map(float, input("Digite os dois lados do primeiro triângulo separados por espaço: ").split()))
    angulo1 = float(input("Digite o ângulo entre os lados do primeiro triângulo: "))
    lados2 = list(map(float, input("Digite os dois lados do segundo triângulo separados por espaço: ").split()))
    angulo2 = float(input("Digite o ângulo entre os lados do segundo triângulo: "))
    
    triangulo1 = {'lados': lados1, 'angulo': angulo1}
    triangulo2 = {'lados': lados2, 'angulo': angulo2}
    
elif tipo_criterio == "AA":
    # Dados para AA
    angulos1 = list(map(float, input("Digite os dois ângulos do primeiro triângulo separados por espaço: ").split()))
    angulos2 = list(map(float, input("Digite os dois ângulos do segundo triângulo separados por espaço: ").split()))
    
    triangulo1 = {'angulos': angulos1}
    triangulo2 = {'angulos': angulos2}
    
elif tipo_criterio == "LLL":
    # Dados para LLL
    lados1 = list(map(float, input("Digite os três lados do primeiro triângulo separados por espaço: ").split()))
    lados2 = list(map(float, input("Digite os três lados do segundo triângulo separados por espaço: ").split()))
    
    triangulo1 = {'lados': lados1}
    triangulo2 = {'lados': lados2}
    
else:
    resultado = "Critério inválido. Escolha entre LAL, AA ou LLL."
    triangulo1, triangulo2 = {}, {}

# Verificação e exibição do resultado
if triangulo1 and triangulo2:
    resultado = verificar_seme1hanca(triangulo1, triangulo2)

print(resultado)
