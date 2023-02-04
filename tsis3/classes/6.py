def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
new_list = list(filter(lambda x: is_prime(x), my_list))
print(new_list)