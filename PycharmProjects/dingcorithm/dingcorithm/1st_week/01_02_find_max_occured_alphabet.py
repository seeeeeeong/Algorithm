def find_max_occurred_alphabet(string):
  alphabet_array = [0] * 26

  for alphabet in string:
    if not alphabet.isalpha():
      continue
    alphabet_array[ord(alphabet) - ord('a')] += 1

  max_alphabet_occurrence = 0
  max_alphabet_index = 0
  for i in range(len(alphabet_array)):
    if alphabet_array[i] > max_alphabet_occurrence:
      max_alphabet_occurrence = alphabet_array[i]
      max_alphabet_index = i

  return chr(max_alphabet_index + ord('a'))


result = find_max_occurred_alphabet
print("정답 = i 현재 풀이 값 =", result("hello my name is dingcodingco"))
print("정답 = e 현재 풀이 값 =", result("we love algorithm"))
print("정답 = b 현재 풀이 값 =", result("best of best youtube"))


# alphabet_array = [] -> 알파벳 빈도 저장
# for string -> alphabet_array += 1 -> 빈도 수 저장
# for alphabet -> max값을 찾는다.
