import random
import webbrowser

print("Welcome to Guessing Game \n")
print("Enter starting and ending range of numbers and random number will be generated by the computer,\nThen go on guessing until you gues the correct number \n")
print("========================================================")

print("Play stupid game, win stupid prizes.")

print("======================================================== \n")

startSeed = input("Enter starting range : ") #asking input for starting seed
endSeed = input("Enter ending range : ")    #asking input for limit number

number = random.randint(int(startSeed), int(endSeed))   #here random number generated is stored to "number" variable
                                                        #since passing variable as argument passed variables as string int() method is used to convert to int which is predefined method                                                    


answer = input("Enter your guess : ") #asking input from user


while int(answer) != int(number):  #a simple while loop to run an expression while the answer provided by user is false
                                   #note that int() method is beign used here, if not used python treates both the variables as string 
    answer = input("Try again : ") 
    

print("You have won stupid prize :D")
webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
