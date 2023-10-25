# Cabeçalho da tabela verdade
print("Tabela Verdade do Operador AND")
print("-" * 49)
print("| Entrada (A) | Entrada (B) | Saída (A AND B) |")
print("-" * 49)

# Loop através de todas as combinações possíveis de entradas (True e False)
for entrada_a in [True, False]:
    for entrada_b in [True, False]:
        # Calcula a saída usando o operador AND
        saida = entrada_a and entrada_b

        # Imprime a linha da tabela verdade
        print(f"| {entrada_a:^12} | {entrada_b:^12} | {saida:^15} |")

# Rodapé da tabela verdade
print("-" * 49)