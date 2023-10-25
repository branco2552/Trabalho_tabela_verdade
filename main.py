def menu():
    print("Escolha uma operação lógica:")
    print("1. NOT")
    print("2. AND")
    print("3. OR")
    print("4. XOR")
    print("5. Implicação")
    print("6. Bicondicional")
    print("0. Sair")

def not_table():
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


def and_table():
        # Cabeçalho da tabela verdade
        print("Tabela Verdade do Operador AND")
        print("-" * 39)
        print("| Entrada (A) | Entrada (B) | Saída (A AND B) |")
        print("-" * 39)

        # Loop através de todas as combinações possíveis de entradas (True e False)
        for entrada_a in [True, False]:
            for entrada_b in [True, False]:
                # Calcula a saída usando o operador AND
                saida = entrada_a and entrada_b

                # Imprime a linha da tabela verdade
                print(f"| {entrada_a:^12} | {entrada_b:^12} | {saida:^15} |")

        # Rodapé da tabela verdade
        print("-" * 39)

def or_table():
# Cabeçalho da tabela verdade
        print("Tabela Verdade do Operador OR")
        print("-" * 38)
        print("| Entrada (A) | Entrada (B) | Saída (A OR B) |")
        print("-" * 38)

        # Loop através de todas as combinações possíveis de entradas (True e False)
        for entrada_a in [True, False]:
            for entrada_b in [True, False]:
                # Calcula a saída usando o operador OR
                saida = entrada_a or entrada_b

                # Imprime a linha da tabela verdade
                print(f"| {entrada_a:^12} | {entrada_b:^12} | {saida:^14} |")

        # Rodapé da tabela verdade
        print("-" * 38)


def xor_table():
        # Cabeçalho da tabela verdade
        print("Tabela Verdade do Operador XOR")
        print("-" * 39)
        print("| Entrada (A) | Entrada (B) | Saída (A XOR B) |")
        print("-" * 39)

        # Loop através de todas as combinações possíveis de entradas (True e False)
        for entrada_a in [True, False]:
            for entrada_b in [True, False]:
                # Calcula a saída usando o operador XOR
                saida = entrada_a != entrada_b

                # Imprime a linha da tabela verdade
                print(f"| {entrada_a:^12} | {entrada_b:^12} | {saida:^15} |")

        # Rodapé da tabela verdade
        print("-" * 39)


def implication_table():
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


def biconditional_table():
        # Cabeçalho da tabela verdade
        print("Tabela Verdade do Operador Bicondicional (Equivalência)")
        print("-" * 59)
        print("| Entrada (A) | Entrada (B) | Saída (A <=> B) |")
        print("-" * 59)

        # Loop através de todas as combinações possíveis de entradas (True e False)
        for entrada_a in [True, False]:
            for entrada_b in [True, False]:
                # Calcula a saída usando o operador Bicondicional
                saida = entrada_a == entrada_b

                # Imprime a linha da tabela verdade
                print(f"| {entrada_a:^12} | {entrada_b:^12} | {saida:^16} |")

        # Rodapé da tabela verdade
        print("-" * 59)


if __name__ == "__main__":
    while True:
        menu()
        escolha = input("Digite o número da operação desejada (ou 0 para sair): ")

        if escolha == "1":
            not_table()
        elif escolha == "2":
            and_table()
        elif escolha == "3":
            or_table()
        elif escolha == "4":
            xor_table()
        elif escolha == "5":
            implication_table()
        elif escolha == "6":
            biconditional_table()
        elif escolha == "0":
            print("Saindo...")
            break
        else:
            print("Escolha inválida. Por favor, escolha uma opção válida.")
