def bissetriz_externa_ratio(ab, ac, bc):
    # Verifica se os lados formam um triângulo válido
    if ab + ac <= bc or ab + bc <= ac or ac + bc <= ab:
        return "Os valores fornecidos não formam um triângulo."
    
    # Verifica se a condição para a bissetriz externa é válida
    if ab == ac:
        return "A bissetriz externa não pode ser aplicada com AB igual a AC."

    # Cálculo da divisão pela bissetriz externa
    be = (ab * bc) / (ab - ac)
    ec = be - bc
    ratio = be / ec
    return be, ec, ratio

# Entrada de dados do usuário
try:
    ab = float(input("Digite o comprimento do lado AB: "))
    ac = float(input("Digite o comprimento do lado AC: "))
    bc = float(input("Digite o comprimento do lado BC: "))

    # Cálculo da bissetriz externa
    externa_result = bissetriz_externa_ratio(ab, ac, bc)
    if isinstance(externa_result, str):
        print(externa_result)
    else:
        be, ec, ratio = externa_result
        print(f"Bissetriz Externa - BE: {be:.2f}, EC: {ec:.2f}, Razão BE/EC: {ratio:.2f}")
except ValueError:
    print("Por favor, insira valores numéricos válidos.")
