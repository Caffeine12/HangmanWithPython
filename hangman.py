import random

# List of random words
word_list = ['ardvark','baboon','camel']

#Select a word randomly
selected_word = random.choice(word_list)

#This is for easy debugging
print(f"psst, the word is: {selected_word}")

#Total lives
lives=6

#make a display list to give user feedback
display=[]
for _ in selected_word:
    display+="_"
print(display)

end_of_game = False

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']


while not end_of_game:
    matched=False
    #Take user guessed input
    guessed_letter=input('Guess a letter: ').lower()

    #match if the guess is correct or not
    for position in range(len(selected_word)):
        if guessed_letter==selected_word[position]:
            display[position]=guessed_letter
            matched=True
    if matched==False:
        lives-=1
        print(stages[lives])
        if lives==0:
            print("You have lost")
            break
    
    print(display)
    if "_" not in display:
        end_of_game = True
        print("You have won")
