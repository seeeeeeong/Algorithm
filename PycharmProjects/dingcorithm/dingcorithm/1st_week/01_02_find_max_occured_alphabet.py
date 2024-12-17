# def find_max_occurred_alphabet(string):
#   alphabet_array = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
#                     "m", "n", "o", "p", "q", "r", "s",
#                     "t", "u", "v", "x", "y", "z"]
#   max_occurrence = 0
#   max_alphabet = alphabet_array[0]
#
#   for alphabet in alphabet_array:
#     occurrence = 0
#     for char in string:
#       if char == alphabet:
#         occurrence += 1
#
#     if occurrence > max_occurrence:
#       max_alphabet = alphabet
#       max_occurrence = occurrence
#
#   return max_alphabet

def find_max_occurred_alphabet(string):
  alphabet_occurrence_array = [0] * 26

  for char in string:
    if not(char.isalpha()):
      continue
    arr_index = ord(char) - ord('a')
    alphabet_occurrence_array[arr_index] += 1

  max_occurrence = 0
  max_alphabet_index = 0

  for i in range(len(alphabet_occurrence_array)):
    alphabet_occurrence = alphabet_occurrence_array[i]

    if alphabet_occurrence > max_occurrence:
      max_occurrence = alphabet_occurrence
      max_alphabet_index = i

  return chr(max_alphabet_index + ord('a'))




print("정답 = i 현재 풀이 값 =", find_max_occurred_alphabet("hello my name is dingcodingco"))
print("정답 = e 현재 풀이 값 =", find_max_occurred_alphabet("we love algorithm"))
print("정답 = b 현재 풀이 값 =", find_max_occurred_alphabet("best of best youtube"))

