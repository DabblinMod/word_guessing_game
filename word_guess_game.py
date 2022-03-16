#guessing the words
#import the random module, make a list to hold the words you are going to be guessing
#use a variable to hold each character. If word is a match you can keep guessing the letter.

import random
import sys

class guessWord:
    def __init__(self):
        self.words=["this", "teenager", "filly", "colt", "Applejack", "Snake",
    "viper", "mystique", "charlie", "keith", "osmos", "periods", "dance"]
    #This is going to be what we use to guess our words. You don't want it to be global though
    def displayMenu(self):
        print("\nWould you like to play this guessing game?\n")
        print("Select: Y or N")
        ans=str(input("Decision: "))#players choice
        return ans.upper() #ensures answer is uppercase
    def guess(self):
        decision=self.displayMenu()
        failed=0 #number of failed attempts
        turns=4 #number of turns
        #use the number of turns as the number of chances a player gets to
        #use a while loop to loop through a prompt 
        correct=0
        if(decision=="Y"):
            while(turns > 0):
                randomWord=random.choice(self.words)
                guesses=""
                #print("Randomly selected word is: ", randomWord)
                    #converts the first letter of a word to a number than changes it back to a string char
                    #check the Unicode value of a character before leaving hints. We want to make sure we don't get any errors
                if(ord(randomWord[0]) == 122): #we check if the character is the last letter in the alphabet
                    print("\n")
                    firstPrevChar= chr(ord(randomWord[0])- 2)
                    secondPrevChar= chr(ord(randomWord[0]) - 3)
                    print(f"The letter starts after the alphabets: {secondPrevChar} and {firstPrevChar}\n")
                elif(ord(randomWord[0]) >= 97 and ord(randomWord[0]) < 122): #checking for all characters before 'z' in the alphabet
                    letterBefore=chr(ord(randomWord[0])-3) #takes the letter three before the starting character of a word in alphabet
                    letterAfter=chr(ord(randomWord[0])+ 1) #takes the letter after the starting word in the alphabet
                    print("Here are your hints:\n")
                    print(f"\tThe first word starts with a letter that is between these letters in the alphabet {letterBefore} and {letterAfter}\n")
                incorrect=0
                charCount=0
                while(incorrect != 1):
                    print("Count is: ", charCount, "\nWord len is: ", len(randomWord))
                    if(charCount==0):
                        guess=chr(ord(input("Enter a single character to guess the first letter of your string: ")))
                    elif(charCount == len(randomWord)):
                        print("You guessed the word correctly! Good job! Let's go on to the next word.\n")
                        break
                    elif(charCount > 0 and len(randomWord)):
                        guess=chr(ord(input("Enter a single character to guess the next letter of your word: ")))
                    if(charCount==0 and randomWord.startswith(guess)):
                        guesses+=guess
                        charCount+=1
                        print("Guess so far: ", guesses)
                        print("Correct! Nice work!\n")
                    elif(randomWord[charCount]==guess):
                        print("Correct! Nice work!\n")
                        charCount+=1
                        guesses+=guess
                        print("Guess so far: ", guesses)
                    else:
                        incorrect +=1
                        print("Sorry you got that wrong! We'll have to move on to the next person. You'll get a turn on the next word.")
                        turns-=1
                        print("Turns left: ", turns)
                    
        elif(decision=="N"):
            #exit the game.
            print("You have decided to exit the game. Thanks for playing!\n")
            print("Goodbye\n... ... ...\n")
            sys.exit()
#game exits here
