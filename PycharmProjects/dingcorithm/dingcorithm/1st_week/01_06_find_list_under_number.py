input = 20


def find_prime_list_under_number(number):
    result = []
    for i in range(2, number + 1):
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                break
        else:
            result.append(i)
    return result


result = find_prime_list_under_number(input)
print(result)