input = 20


def find_prime_list_under_number(number):
    answer = []
    for i in range(2, number + 1):
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                break
        else:
            answer.append(i)

    return answer


result = find_prime_list_under_number(input)
print(result)


# 20 이하의 소수를 모두 반환

# for i in range(2, number + 1)
#   for j in range(j, int(j ** 0.5) + 1)
#       if i % j == 0:
#           break
#   answer.append(i)
# return answer