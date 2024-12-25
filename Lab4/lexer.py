import re

def tokenize(input, token_rules):
    tokens = []
    while input:
        match = None
        for token_type, pattern in token_rules.items():
            regex = re.compile(pattern)
            match = regex.match(input)
            if match:
                if token_type != "WHITESPACE":  # Пропускаем пробелы
                    tokens.append((token_type, match.group(0)))
                input = input[match.end():]
                break
        if not match:
            raise ValueError(f"Unexpected token: {input[0]}")
    tokens.append(("EOF", "EOF"))  # Добавляем конец файла
    return tokens
