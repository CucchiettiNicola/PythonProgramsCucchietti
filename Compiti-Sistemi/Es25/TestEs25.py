import Es25 as ex25

sentence = "All good things come to those who wait"

print('\nbreak_words(sentence) --> ', end='')
words = ex25.break_words(sentence)
print(words)

print('\nsort_words(words) --> ', end='')
sorted_words = ex25.sort_words(words)
print(sorted_words)

print('\nprint_first_word(words) --> ', end='')
ex25.print_first_word(words)
print('\nprint_last_word(words) --> ', end='')
ex25.print_last_word(words)
print('\nwords --> ',sorted_words)

print('\nprint_first_word(sorted_words) --> ', end='')
ex25.print_first_word(sorted_words)
print('\nprint_last_word(sorted_words) --> ', end='')
ex25.print_last_word(sorted_words)
print('\nsorted_words --> ',sorted_words)

print('\nsort_sentence(sentence) --> ', end='')
sorted_words = ex25.sort_sentence(sentence)
print(sorted_words)

print('\nprint_first_and_last(sentence): ')
ex25.print_first_and_last(sentence)
print('\nprint_first_and_last_sorted(sentence): ')
ex25.print_first_and_last_sorted(sentence)