userName = input("Welcome to the Elite 101 Chatbot! What is your name? ")
print(userName)
userAge = input("Hello " + userName + " what is your age? ")
print(userAge)
print("Hello " + userName + " you are " + userAge + " years old!")
if userAge < "16":
  print("You are too young to drive.")
else:
  print("You are old enough to drive!")
  
print("These are your options: \n 1. option 1 \n 2. option 2 \n 3. option 3 \n 4. exit ")

userOption = input("Please select an option: ")
print(userOption)

if userOption == "1":
  print("Congrats this option gives you goodluck")
if userOption == "2":
  print("Sadly you got the unlucky option")
if userOption == "3":
  print("You got the safe option this option gives you nothing")
if userOption == "4":
  print("You have exited the program. Goodbye")
  quit()

print("Great JOB!")