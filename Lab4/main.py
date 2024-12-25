from lexer import tokenize
from grammar import compute_first, compute_follow
from parser import create_table, parse

token_rules = {
    "USER": r"my_object",
    "START": r"start",
    "DIRECTION": r"forward|back|left|right",
    "ROTATION": r"rotate",
    "ANGLE_DIRECTION": r"\+|\-",
    "NUMBER": r"[0-9]+",
    "WHITESPACE": r"\s+",
}

grammar = {
    "commands": [["command", "commands'"]],
    "commands'": [["command", "commands'"], ["EMPTY"]],
    "command": [["USER", "command'"]],
    "command'": [["moveCommand"], ["rotateCommand"], ["startCommand"]],
    "moveCommand": [["DIRECTION"]],
    "rotateCommand": [["ROTATION", "ANGLE_DIRECTION", "NUMBER"]],
    "startCommand": [["START"]],
}

input_text = "my_object start my_object rotate -90 my_object forward"
tokens = tokenize(input_text, token_rules)

first = compute_first(grammar)
follow = compute_follow(grammar, first)
table = create_table(grammar, first, follow)

try:
    parse(tokens, grammar, table)
    print("Input is valid!")
except ValueError as e:
    print(f"Error: {e}")
