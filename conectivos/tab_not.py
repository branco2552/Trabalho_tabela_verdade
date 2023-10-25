# Cabeçalho da tabela verdade
print("Tabela Verdade do Operador NOT")
print("-" * 31)
print("| Entrada (A) | Saída (NOT A) |")
print("-" * 31)

# Loop através de todas as entradas possíveis (True e False)
for entrada in [True, False]:
    # Calcula a saída usando o operador NOT
    saida = not entrada

    # Imprime a linha da tabela verdade
    print(f"| {entrada:^12} | {saida:^14} |")

# Rodapé da tabela verdade
print("-" * 31)