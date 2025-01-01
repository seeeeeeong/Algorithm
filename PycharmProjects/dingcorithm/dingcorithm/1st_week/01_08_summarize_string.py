def summarize_string(input_str):
  n = len(input_str)
  count = 0
  result_str = ''

  for i in range(n - 1):
    if input_str[i] == input_str[i + 1]:
      count += 1
    else:
      result_str += input_str[i] + str(count + 1) + '/'
      count = 0

  result_str += input_str[n - 1] + str(count + 1)

  return result_str


# 이 부분을 채워보세요!


input_str = "acccdeee"

print(summarize_string(input_str))