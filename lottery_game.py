# Make a lotery game suing input function
import random

print("Hi ! Enter ur Name ")

person_name  = input()

print("hey {} can you guess the number for lot ".format(person_name))

def lotery_luck ():
    lot_number = random.randint(1,30)    
    guess_number = input()
    if (guess_number == lot_number):
        return print("Hurray ! {} you won the lot ".format(person_name))
    else :
        return print("sorry {0} better luck next tym \n the Orignal Lot Number is {1}".format(person_name,lot_number))
        
    
 
print(lotery_luck())

print("want to take a chance again?(yes/no)")
chance = input()

while (chance == 'yes'):
    print("please enter your lucky number :")
    print(lotery_luck())
    print("want to take a chance again?(yes/no)")
    chance = input()


print("Thank you For Playing Game!!") 