import art

print(art.logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

go=True

def cipher(t,s,d) :

    cipher_text=""
    p_letter_no=0
    letter_no=0
   
    if d=="decode" or d=="encode" :
        for letter in t :
            if letter in alphabet :
                p_letter_no=alphabet.index(letter)
                if d=="decode" :
                    letter_no=p_letter_no-s
                    if letter_no < 0 :
                        while letter_no < 0:
                            letter_no+=len(alphabet)
                        cipher_text+=alphabet[letter_no]  
                        
                    else :
                        cipher_text+=alphabet[letter_no]

                elif d=="encode" :
                    letter_no=p_letter_no+s
                    if letter_no > (len(alphabet)-1) :
                        while letter_no > len(alphabet)-1:
                            letter_no-=len(alphabet)
                        cipher_text+=alphabet[letter_no]  
                        
                    else :
                        cipher_text+=alphabet[letter_no]
            else :
                cipher_text+=letter
        print(cipher_text)
    else :
        print("Wrong Input!") 

while go==True :
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    cipher(t=text,s=shift,d=direction)

    decision=input("Do you want to restart the program? Type Yes or No \n").lower()
    if decision == "no" :
        go=False
        print("Good bye!")

# def getDecision():
#     decision=input("Do you want to restart the cipher program Type yes or No")
#     if decision=="Yes" :
#         getInputs()

# getInputs()  
# def encrypt(t,s) :
#   cipher_text=""
#   p_letter_no=0
#   letter_no=0
  
#   for letter in t :
#     if letter==' ' :
#       cipher_text+=' '
#     else :
#       p_letter_no=alphabet.index(letter)
#       letter_no=p_letter_no+s
#       if letter_no > (len(alphabet)-1) :
#         while letter_no > len(alphabet)-1:
#           letter_no-=len(alphabet)
#         cipher_text+=alphabet[letter_no]  
         
#       else :
#         cipher_text+=alphabet[letter_no]
      
#   print(f"The encoded text : {cipher_text}")

# def decrypt(t,s):
#   cipher_text=""
#   p_letter_no=0
#   letter_no=0
#   for letter in t :
#     if letter==' ' :
#       cipher_text+=' '
#     else :
#       p_letter_no=alphabet.index(letter)
#       letter_no=p_letter_no-s
#       if letter_no < 0 :
#         while letter_no < 0:
#           letter_no=len(alphabet)+letter_no
#         cipher_text+=alphabet[letter_no]  
         
#       else :
#         cipher_text+=alphabet[letter_no]
        
#   print(f"The decoded text : {cipher_text}")

# if direction=="encode":
#   encrypt(t=text,s=shift) 
# elif direction=="decode" :
#   decrypt(t=text,s=shift)
# else :
#   print("Wrong Input!")
    