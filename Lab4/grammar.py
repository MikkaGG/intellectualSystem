def compute_first(grammar):
    first = {nt: set() for nt in grammar}
    for nt, rules in grammar.items():
        for rule in rules:
            if rule[0] not in grammar:  # Терминал
                first[nt].add(rule[0])
    changed = True
    while changed:
        changed = False
        for nt, rules in grammar.items():
            for rule in rules:
                before = len(first[nt])
                for symbol in rule:
                    if symbol in grammar:  # Нетерминал
                        first[nt].update(first[symbol] - {"EMPTY"})
                        if "EMPTY" not in first[symbol]:
                            break
                    else:  # Терминал
                        first[nt].add(symbol)
                        break
                else:
                    first[nt].add("EMPTY")
                changed |= len(first[nt]) > before
    return first

def compute_follow(grammar, first):
    follow = {nt: set() for nt in grammar}
    follow["commands"].add("EOF")
    changed = True
    while changed:
        changed = False
        for nt, rules in grammar.items():
            for rule in rules:
                for i, symbol in enumerate(rule):
                    if symbol in grammar:
                        next_symbols = rule[i + 1:]
                        before = len(follow[symbol])
                        if next_symbols:
                            for s in next_symbols:
                                if s in grammar:
                                    follow[symbol].update(first[s] - {"EMPTY"})
                                    if "EMPTY" in first[s]:
                                        continue
                                    break
                                else:
                                    follow[symbol].add(s)
                                    break
                        else:
                            follow[symbol].update(follow[nt])
                        changed |= len(follow[symbol]) > before
    return follow
