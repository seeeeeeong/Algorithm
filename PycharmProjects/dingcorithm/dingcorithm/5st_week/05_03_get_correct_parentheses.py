from collections import deque

balanced_parentheses_string = "()))((()"

def is_correct_parentheses(string):
  stack = []
  for i in range(len(string)):
    if string[i] == "(":
      stack.append("(")
    elif string[i] == ")":
      if len(stack) == 0:
        return False
      stack.pop()

  if len(stack) != 0:
    return False
  else:
    return True

def separate_to_u_v(string):
  queue = deque(string)
  left, right = 0, 0
  u, v = "", ""

  while queue:
    char = queue.popleft()
    u += char
    if char == '(':
      left += 1
    if char == ')':
      right += 1
    if left == right:
      break

  v = ''.join(list(queue))
  return u, v

def reverse_parentheses(string):
  reversed_string = ""
  for char in string:
    if char == '(':
      reversed_string += ')'
    else:
      reversed_string += '('
  return reversed_string

def change_to_correct_parentheses(string):
  if string == '':
    return ''
  u, v = separate_to_u_v(string)
  if is_correct_parentheses(u):
    return u + change_to_correct_parentheses(v)
  else:
    return '(' + change_to_correct_parentheses(v) + ')' + reverse_parentheses(u[1:-1])

def get_correct_parentheses(balanced_parentheses_string):
  if is_correct_parentheses(balanced_parentheses_string):
    return balanced_parentheses_string
  else:
    return change_to_correct_parentheses(balanced_parentheses_string)



print(get_correct_parentheses(balanced_parentheses_string))  # "()(())()"가 반환 되어야 합니다!

print("정답 = (((()))) / 현재 풀이 값 = ", get_correct_parentheses(")()()()("))
print("정답 = ()()( / 현재 풀이 값 = ", get_correct_parentheses("))()("))
print("정답 = ((((()())))) / 현재 풀이 값 = ", get_correct_parentheses(')()()()(())('))