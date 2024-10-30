def bissetriz_interna_ratio(ab, ac, bc):
    # Verifica se os lados formam um triângulo válido
    if ab + ac <= bc or ab + bc <= ac or ac + bc <= ab:
        return "Os valores fornecidos não formam um triângulo."
    
    # Cálculo da divisão pela bissetriz interna
    bd = (ab * bc) / (ab + ac)
    dc = bc - bd
    ratio = bd / dc
    return bd, dc, ratio

# Entrada de dados do usuário
try:
    ab = float(input("Digite o comprimento do lado AB: "))
    ac = float(input("Digite o comprimento do lado AC: "))
    bc = float(input("Digite o comprimento do lado BC: "))

    # Cálculo da bissetriz interna
    interna_result = bissetriz_interna_ratio(ab, ac, bc)
    if isinstance(interna_result, str):
        print(interna_result)
    else:
        bd, dc, ratio = interna_result
        print(f"Bissetriz Interna - BD: {bd:.2f}, DC: {dc:.2f}, Razão BD/DC: {ratio:.2f}")
except ValueError:
    print("Por favor, insira valores numéricos válidos.")
