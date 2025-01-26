genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]


def get_melon_best_album(genre_array, play_array):
    result = []
    dict_play = {}
    dict_index = {}
    last_added_index = 0

    while last_added_index < len(play_array):
      genre = genre_array[last_added_index]
      play = play_array[last_added_index]

      if genre in dict_play:
        dict_play[genre] += play
        dict_index[genre].append([last_added_index, play])
        last_added_index += 1
      else:
        dict_play[genre] = play
        dict_index[genre] = [[last_added_index, play]]
        last_added_index += 1

    sorted_dict_play = sorted(dict_play.items(), key=lambda item: item[1], reverse=True)

    for genre, play in sorted_dict_play:
      sorted_dict_index = sorted(dict_index[genre], key=lambda item: item[1], reverse=True)

      count = 0
      for idx, play in sorted_dict_index:
        if count < 2:
          result.append(idx)
          count += 1
        else:
          break
    return result


print("정답 = [4, 1, 3, 0] / 현재 풀이 값 = ", get_melon_best_album(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))
print("정답 = [0, 6, 5, 2, 4, 1] / 현재 풀이 값 = ", get_melon_best_album(["hiphop", "classic", "pop", "classic", "classic", "pop", "hiphop"], [2000, 500, 600, 150, 800, 2500, 2000]))