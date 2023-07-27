#!/usr/bin/env python3

import requests
import random
import html

url = "https://opentdb.com/api.php?amount=6&category=15"

def main(): 
    response = requests.get(url).json()

    questions = []
    answers = []
    correctCounter = 0

    for result in response['results']:
        print(html.unescape(result['question']))
        
        # Let's make a list of answers such that we can print the correct answer and incorrect in a random order
        options = []
        correct = html.unescape(result['correct_answer'])
        options.append(correct)
        
        for index in range(len(result['incorrect_answers'])):
            options.append(html.unescape(result['incorrect_answers'][index]))

        random.shuffle(options)
        i = 1
        for option in options:
            print(str(i) + '. ' + option)
            i += 1

        print("")

        if result['type'] == 'multiple':
            userAnswer = input("Please choose an answer between 1 and 4:\n> ")
            if options[int(userAnswer) - 1] == correct:
                print("Nicely done! That was correct!")
                correctCounter += 1 
            else:
                print("Ooof. Nice try. The correct answer was " + correct + '.')


        if result['type'] == 'boolean':
            userAnswer = input("Please choose true or false:\n> ")
            if userAnswer.upper() == correct.upper():
                print("That's correct! 5 points to Gryffindor!")
                correctCounter += 1
            else:
                print("That wasn't quite right... The correct answer was " + correct + '.')

    print(f"You got {correctCounter} out of 6 correct!\nThanks for playing~") 
                

if __name__ == '__main__':
    main()
