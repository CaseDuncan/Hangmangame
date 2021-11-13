import random

#function 
def hangman():
    word_list = ['hangman', 'kenya', 'jesus', 'programming', 'riverside']
    answer = random.choice(word_list)
    turns = 10
    guess_made = ''
    validEntries = set('abcdefghijklmnopqrstuvwxz')

    while len(answer)>0:
        correct_answer = ''
        
        for letter in answer:
            if letter in guess_made:
                correct_answer = correct_answer+letter
            else:
                correct_answer = correct_answer + "_"
                if correct_answer == answer:
                    print(correct_answer)
                    print("You Wooon!")
                    break
        print("Guess the correct word", correct_answer)
        guess = input()

        if guess in validEntries:
            guess_made = guess_made+guess
        else:
            print("Invalid character")
            guess = input()

    if turns ==9:
        print("9 turns left")
        print("----------------")

    if turns ==8:
        print("8 turns left")
        print("----------------")
        print("         O       ")

    if turns ==7:
        print("7 turns left")
        print("----------------")
        print("         O   ")
        print("         |   ")

    if turns ==6:
        print("6 turns left")
        print("-------------")
        print("         O   ")
        print("         |   ")
        print("        /    ")

    if turns ==5:
        print("5 turns left")
        print("----------------")
        print("         O   ")
        print("         |   ")
        print("        / \   ")
        

    if turns ==4:
        print("4 turns left")
        print("----------------")
        print("        \O   ")
        print("         |   ")
        print("        / \   ")
            
    if turns ==3:
        print("3 turns left")
        print("----------------")
        print("        \O/  ")
        print("         |   ")
        print("        / \   ")
            
    if turns ==2:
        print("2 turns left")
        print("--------------")
        print("        \O/ | ")
        print("         |    ")
        print("        / \   ")

    if turns ==1:
        print("Only one  turn left! Hangman on his last breath")
        print("--------------")
        print("        \O/_| ")
        print("         |    ")
        print("        / \   ")
    
    if turns == 0:
        print("You Loose!")
        print("You let a good man die!")
        
 
            
name = input('Enter your Name')
print("welcome", name)
print("Guess the word in 10 or less attempts!")
hangman()