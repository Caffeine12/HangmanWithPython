import random

# List of random words
word_list = ['ardvark','baboon','camel']

#Select a word randomly
selected_word = random.choice(word_list)

#This is for easy debugging
print(f"psst, the word is: {selected_word}")

#make a display list to give user feedback
display=[]
for _ in selected_word:
    display+="_"
print(display)

#Take user guessed input
guessed_letter=input('Guess a letter: ').lower()

#match if the guess is correct or not
for position in range(len(selected_word)):
    if guessed_letter==selected_word[position]:
        display[position]=guessed_letter
    
print(display)
