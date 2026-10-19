
def add_entry(history, operation, a, b, result):
    entry = {
        "operation": operation,
        "first_number": a,
        "second_number": b,
        "result": result
    }

    history.append(entry)


def format_history(history):
    if not history:
        return "Nenhum cálculo realizado ainda."

    lines = []

    for index, entry in enumerate(history, start=1):
        lines.append(
            f"{index}. {entry['first_number']:g} "
            f"{entry['operation']} "
            f"{entry['second_number']:g} = "
            f"{entry['result']:g}"
        )

    return "\n".join(lines)
