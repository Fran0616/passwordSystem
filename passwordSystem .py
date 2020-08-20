#basic password system. The program ustilize the while statment to continuesly promt user to enter the password and break when the password is correct. 
#variable for password enter
userInput= input("Enter the password: ")
#while loop condition. The condition is to promt user to reenter password and break when the password matches. 
while userInput != "chupacabra":
    userInput = input("Wrong password. Try again: ")
    if userInput == "chupacabra":
        break
#will display once loop is broken.
print ("You've successfully logged in.")
