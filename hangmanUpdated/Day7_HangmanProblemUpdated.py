import random
import hangman_art
import hangman_words
print(hangman_art.logo)
print("\n\n")


word_num = random.randint(0,len(hangman_words.word_list)-1)
word=[]
stage_num=len(hangman_art.stages)-1
space = []
for n in range(0,len(hangman_words.word_list[word_num])) :
  word += hangman_words.word_list[word_num][n]
  space += "_" 
print(*space)
print(hangman_art.stages[stage_num])
print("\n\n")
j=0

r=0

while not j==len(space):
  guess=input(f"\nGuess the letter : ").lower()  
  position=len(space)-1
  while not position < 0 :
    if guess==space[position] :
      print("Already used !")
      position=-1
    position-=1
  i=0
  p=0
  while not i== len(hangman_words.word_list[word_num]) :
    if (word[i]==guess) :
      space[i]=guess
      j+=1
      p+=1
      r+=1
    i+=1 
  print("\n")
  print(*space)
  if p==0 :
    stage_num=stage_num-1
    if stage_num>0 :
      print("\nWrong!\nYou lose a life\n")
    elif stage_num==0 :
      print("\nWrong!\n")
      print("You lose! Game Over !")
      j=len(space)
  print(hangman_art.stages[stage_num])
  
if r==len(hangman_words.word_list[word_num]) :
    print("You win!")
  

