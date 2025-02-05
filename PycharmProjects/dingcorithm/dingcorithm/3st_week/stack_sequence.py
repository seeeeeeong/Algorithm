def stack_sequence(n, sequence):
    num = 1
    sequence_idx = 0
    stack = []
    result = []

    while True:
        if len(stack) == 0:
            stack.append(num)
            result.append("+")
            num += 1

        elif sequence[sequence_idx] == stack[-1]:
            stack.pop()
            result.append("-")
            sequence_idx += 1
            if sequence_idx == len(sequence):
                break

        else:
            if n < num:
                print("NO")
                break
            stack.append(num)
            result.append("+")
            num += 1

    if len(stack) == 0:
        for char in result:
            print(char)


sequence = [4, 3, 6, 8, 7, 5, 2, 1]
n = 8
stack_sequence(n, sequence)

sequence = [1, 2, 5, 3, 4]
n = 5
stack_sequence(n, sequence)