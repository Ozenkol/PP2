import re

def repl(match):
    return match[1]+" "+match[2]


text = input()

print(re.sub(r'([A-Z]\w+)([A-Z]\w+)', repl, text))