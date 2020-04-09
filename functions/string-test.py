import stringfunc

#from stringfunc import print_first_and_last
#print_first_and_last("potato faces")

sentence = "All good things come to those who wait"
words = stringfunc.break_words(sentence)
words
sorted_words = stringfunc.sort_words(words)
print(sorted_words)
stringfunc.print_first_word(words)
stringfunc.print_last_word(words)
print(words)
stringfunc.print_first_word(sorted_words)
stringfunc.print_last_word(sorted_words)
print(sorted_words)
sorted_words = stringfunc.sort_sentence(sentence)
print(sorted_words)
stringfunc.print_first_and_last(sentence)
stringfunc.print_first_and_last_sorted(sentence)
print(sorted_words)