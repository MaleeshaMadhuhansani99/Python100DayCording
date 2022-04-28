import random

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

word_list = ["aardvark", "baboon", "camel","dictionary"]

word_num = random.randint(0,len(word_list)-1)
word=[]
space = []
for n in range(0,len(word_list[word_num])) :
  word += word_list[word_num][n]
  space += "_" 
print(*space)
print("\n\n")
j=0
l=len(stages)-1
r=0
while not j==len(space) :
  guess=input(f"\nGuess the letter : ").lower()
  i=0
  p=0
  while not i== len(word_list[word_num]) :
    if (word[i]==guess) :
      space[i]=guess
      j+=1
      p+=1
      r+=1
    i+=1 
  print("\n")
  print(*space)
  if p==0 :
    if l>1 :
      print("\nWrong!\n")
      print(stages[l-1])
      l=l-1
    else :
      print(stages[l-1])
      print("You lose! Game Over !")
      j=len(space) 
if r==len(space) :
    print("You win!")
  

