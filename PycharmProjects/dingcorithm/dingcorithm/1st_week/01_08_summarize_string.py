def summarize_string(input_str):
  result = ""
  count = 0
  for i in range(len(input_str) - 1):
    if input_str[i] != input_str[i + 1]:
      result += input_str[i] + str(count + 1) + "/"
      count = 0
    else:
      count += 1

  result += input_str[-1] + str(count + 1)

  return result


input_str = "acccdeee"

print(summarize_string(input_str))


# for i in range(len(input_str) - 1):
#   if input_str[i] != input_str[i + 1]
#     result += input_str[i] + str(count + 1) + '/'
#     count = 0
#   else:
#     count += 1
# result += input_str[-1] + str(count + 1)

