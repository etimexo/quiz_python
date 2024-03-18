print("Welcome")
score = 0
answer = input("Do you want to play? (yes/no): ")
if answer.lower() != "yes":
    quit()

answer = input("Are you human? ")
if answer.lower() != "yes":
    print("Come back when you become one!")
    quit()
    
answer = input("What is the full meaning of HTML? ")
if answer.lower() == "hypertext markup language":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")


answer = input("What is the full meaning of ROM? ")
if answer.lower() == "read only memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    
answer = input("What year are we currently? ")
if answer == 2024 or answer == str(2024):
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
print("Weldone, you got {} out of 3".format(score))
mark = (score / 3) * 100
final = round(mark, 2)
print("Your percentage: {}%".format(final))