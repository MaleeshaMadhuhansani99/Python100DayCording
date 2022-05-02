def prime_checker(number):
  devided_count=0
  for no in range(2,round(number/2)+1):
    if number % no == 0 :
      devided_count+=1

  if devided_count!=0 :
    print(f"{number} isn't a prime number")
  else :
    print(f"{number} is a prime number")
    
n = int(input("Check this number: "))
prime_checker(number=n)



