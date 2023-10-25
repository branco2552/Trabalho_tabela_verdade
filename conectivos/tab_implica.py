# Cabeçalho da tabela verdade
print("Tabela Verdade do Operador Implicação")
print("-" * 44)
print("| Entrada (A) | Entrada (B) | Saída (A => B) |")
print("-" * 44)

# Loop através de todas as combinações possíveis de entradas (True e False)
for entrada_a in [True, False]:
    for entrada_b in [True, False]:
        # Calcula a saída usando o operador de implicação
        saida = not entrada_a or entrada_b

        # Imprime a linha da tabela verdade
        print(f"| {entrada_a:^12} | {entrada_b:^12} | {saida:^14} |")

# Rodapé da tabela verdade
print("-" * 44)
