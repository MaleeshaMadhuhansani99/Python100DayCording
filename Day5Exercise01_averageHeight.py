# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split(", ") 
# student_heights = input("Input a list of student heights ")
# list_student_height=student_heights.split(", ") if we take split() then the elements prints with spaces between them
height=0
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
  
#Write your code below this row 👇
  height += student_heights[n]

avg_height= height/len(student_heights)
print(avg_height)

avg_height_rounded=round(avg_height) #we can take round(avg_height, 2) and then we can round the height to the second decimal point
print(f"Average height is {avg_height_rounded}")




