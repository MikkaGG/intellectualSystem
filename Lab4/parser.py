def create_table(grammar, first, follow):
    table = {nt: {} for nt in grammar}
    for nt, rules in grammar.items():
        for rule in rules:
            first_set = set()
            for symbol in rule:
                if symbol in grammar:
                    first_set.update(first[symbol] - {"EMPTY"})
                    if "EMPTY" not in first[symbol]:
                        break
                else:
                    first_set.add(symbol)
                    break
            else:
                first_set.add("EMPTY")
            for terminal in first_set - {"EMPTY"}:
                table[nt][terminal] = rule
            if "EMPTY" in first_set:
                for terminal in follow[nt]:
                    table[nt][terminal] = rule
    return table

def parse(tokens, grammar, table):
    stack = ["commands"]
    i = 0
    while stack:
        top = stack.pop()
        token_type, token_value = tokens[i]
        if top == token_type:
            i += 1
        elif top in grammar:
            rule = table[top].get(token_type)
            if not rule:
                raise ValueError(f"Unexpected token {token_type} at position {i}")
            stack.extend(reversed(rule))
        elif top == "EMPTY":
            continue
        else:
            raise ValueError(f"Unexpected token {token_type}")
    if i < len(tokens) - 1:
        raise ValueError("Input not fully consumed")
