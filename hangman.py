import random
# List of random words
word_list = ['ardvark','baboon','camel']
#Select a word randomly
selected_word = random.choice(word_list)
#This is for easy debugging
print(f"psst, the word is: {selected_word}")
#convert the selected word into a list
selected_word_list = list(selected_word)
#Take user guessed input
guessed_letter=input('Guess a letter: ').lower()

#match and show to user if the guess is correct or not
for char in selected_word_list:
    if guessed_letter==char:
        print(guessed_letter,end=' ')
    else:
        print('__',end=' ')
