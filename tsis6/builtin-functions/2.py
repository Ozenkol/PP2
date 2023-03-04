def filter_upper(char):
    if char.isupper() is True:
        return True
    else:
        return False


def filter_lower(char):
    if char.islower() is True:
        return True
    else:
        return False


str = input()

print(len(list(filter(filter_upper, str))))
print(len(list(filter(filter_lower, str))))
