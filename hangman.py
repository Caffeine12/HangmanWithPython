import random
word_list = ['ardvark','baboon','camel']
selected_word = random.choice(word_list)
print(f"psst, the word is: {selected_word}")

selected_word_list = list(selected_word)

guessed_letter=input('Guess a letter: ').lower()

for char in selected_word_list:
    if guessed_letter==char:
        print(guessed_letter,end=' ')
    else:
        print('__',end=' ')
