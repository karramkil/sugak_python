word_numbers = input("Введите номера слов через пробел: ").split()
words = input("Введите сами слова через пробел: ").split()
word_dict = {int(num): word for num, word in zip(word_numbers, words)}
new_sentence = " ".join([word_dict[num].capitalize() for num in sorted(word_dict.keys())])
print("Новое предложение:", new_sentence)
