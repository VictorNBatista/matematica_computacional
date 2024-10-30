import itertools

# Funções lógicas
def implies(p, q):
    return not p or q

def evaluate(P, Q, M):
    # Calculando cada condicional
    cond1 = implies(P, Q)
    cond2 = implies(P or Q, True)
    cond3 = implies(not P, implies(M, True))
    # Calculando o resultado final
    R = cond1 and cond2 and cond3
    return R, cond1, cond2, cond3

# Definindo as combinações de valores para P, Q e M
values = [True, False]
combinations = list(itertools.product(values, repeat=3))

# Exibindo a tabela verdade
print(f"{'P':^5} {'Q':^5} {'M':^5} {'R':^5} {'P->Q':^7} {'P∨Q→R':^10} {'¬P→(M→R)':^12}")
for P, Q, M in combinations:
    R, cond1, cond2, cond3 = evaluate(P, Q, M)
    print(f"{P:^5} {Q:^5} {M:^5} {R:^5} {cond1:^7} {cond2:^10} {cond3:^12}")
