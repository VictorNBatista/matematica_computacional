def calcular_salario(salario_fixo, comissao_fixa_por_carro, num_carros_vendidos, valor_total_vendas):
    # Comissão de 5% sobre o total de vendas
    percentual_comissao = 0.05  
    bonus_adicional = 0.10  # Bônus adicional para mais de 10 carros vendidos
    
    # Calcula salário base
    salario_final = salario_fixo
    
    if num_carros_vendidos > 0:
        # Adiciona a comissão fixa por carro e percentual sobre vendas
        salario_final += comissao_fixa_por_carro * num_carros_vendidos
        salario_final += percentual_comissao * valor_total_vendas
        
        # Adiciona bônus adicional se vender mais de 10 carros
        if num_carros_vendidos > 10:
            salario_final += bonus_adicional * valor_total_vendas
            
    return salario_final

# Solicita ao usuário os valores
salario_fixo = float(input("Digite o salário fixo do vendedor: "))
comissao_fixa_por_carro = float(input("Digite a comissão fixa por carro vendido: "))
num_carros_vendidos = int(input("Digite o número de carros vendidos: "))
valor_total_vendas = float(input("Digite o valor total das vendas: "))

# Calcula o salário final
salario_final = calcular_salario(salario_fixo, comissao_fixa_por_carro, num_carros_vendidos, valor_total_vendas)
print(f"O salário final do vendedor é: R$ {salario_final:.2f}")
