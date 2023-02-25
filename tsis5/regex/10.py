import re

def repl(match):
    return match[1]+'_'+match[2].lower()

text = input()

print(re.sub(r"([a-z])([A-Z])", repl, text))


