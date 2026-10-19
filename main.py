
from calculator.operations import add, subtract, multiply, divide
from calculator.history import add_entry, format_history


OPERATIONS = {
    "1": ("+", add),
    "2": ("-", subtract),
    "3": ("*", multiply),
    "4": ("/", divide),
}


def get_number(message):
    while True:
        value = input(message).strip().replace(",", ".")

        try:
            return float(value)
        except ValueError:
            print("Entrada inválida. Digite um número.")


def show_menu():
    print("\n=== PYTHON CALCULATOR ===")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Ver histórico")
    print("0. Sair")


def main():
    history = []

    while True:
        show_menu()
        choice = input("Escolha uma opção: ").strip()

        if choice == "0":
            print("Calculadora encerrada. Até mais!")
            break

        if choice == "5":
            print("\n=== HISTÓRICO ===")
            print(format_history(history))
            continue

        if choice not in OPERATIONS:
            print("Opção inválida. Tente novamente.")
            continue

        a = get_number("Digite o primeiro número: ")
        b = get_number("Digite o segundo número: ")

        symbol, operation = OPERATIONS[choice]

        try:
            result = operation(a, b)
        except ValueError as error:
            print(f"Erro: {error}")
            continue

        print(f"Resultado: {result:g}")
        add_entry(history, symbol, a, b, result)


if __name__ == "__main__":
    main()
