def words_sorting(*args):
    words_dict = {}
    all_sum = 0
    for word in args:
        word_sum = 0
        for letter in word:
            word_sum += ord(letter)
        words_dict[word] = word_sum
        all_sum += word_sum
    if all_sum % 2 == 0:
        sorted_words = dict(sorted(words_dict.items(),key=lambda x: x[0]))
    if all_sum % 2 != 0:
        sorted_words = dict(sorted(words_dict.items(),key=lambda x: -x[1]))

    result = []
    for word,ascii_sum in sorted_words.items():
        result.append(f"{word} - {ascii_sum}\n")
    return "".join(result)

print(
    words_sorting(
        'escape',
        'charm',
        'mythology'
  ))

print(
    words_sorting(
        'escape',
        'charm',
        'eye'
  ))
print(
    words_sorting(
        'cacophony',
        'accolade'
  ))

