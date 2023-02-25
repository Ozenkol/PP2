import re

# def repl(match):
#     #return ' This is match -> '+ match[2] + ' <- '
#     return " "+match[0]


data = input()
print(re.sub(r'([A-Z])', " "+r"\1", data))


