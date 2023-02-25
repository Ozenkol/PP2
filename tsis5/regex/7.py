import re

def repl(match):
    #return ' This is match -> '+ match[2] + ' <- '
    return match[1]+match[3].upper()


data = input()
print(re.sub(r'([a-z])(_)([a-z])', repl, data))