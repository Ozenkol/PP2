import re

def repl(match):
    #return ' This is match -> '+ match[2] + ' <- '
    return match[2].upper()


data = input()
print(re.sub(r'(_)([a-z])', repl, data))


