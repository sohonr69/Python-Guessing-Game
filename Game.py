import random
import webbrowser

print("Welcome to Guessing Game \n")
print("Enter starting and ending range of numbers and random number will be generated by the computer,\nThen go on guessing until you gues the correct number \n")
print("========================================================")

print("Play stupid game, win stupid prizes.")

print("======================================================== \n")

startSeed = input("Enter starting range : ")
endSeed = input("Enter ending range : ")    

number = random.randint(int(startSeed), int(endSeed))   

answer = input("\nEnter your guess : ")

while int(answer) != int(number):

     if int(answer) < int(number):
        answer = input("Higher : ")
     if int(answer) > int(number):
        answer = input("Lower : ")
    

print("You have won stupid prize :D")
webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
