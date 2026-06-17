# Create a quiz game with 2d data collection
# Topic Applied if-else, while, for loop and data collection

def display_intro():
    print("--- Welcome to Quiz Game! --- ")
    input("   Press Enter to Continue!   ")

def display_question_answer(questions, choices, quest_num):

    for quest_num, question in enumerate(questions):
        print(f"{quest_num+1}. {question}")
        for choice in choices[quest_num]:
            print(f"{choice}")
        guesses=get_guesses()
        quest_num += 1
        print()
    return guesses


def get_guesses():
    guess = input("Enter your answer: ").upper()
    guesses.append(guess)
    return guesses

def scoring(guesses, answers, score):
    i = 0
    for guess, answer in zip(guesses,answers):
        if guess == answer:
            score += 1
            print(f"Question no.{i+1} is correct!")
            print(f"Your Answer is: {guess}")
        else:
            print(f"Question no.{i+1} is incorrect!")
            print(f"Your answer is: {guess}")
            print(f"Correct answer is: {answer}")
        i += 1
        print()
    return score

def display_score(score):
    print("---------------")
    print("--  Results  --")
    print("---------------")
    print("Your Guesses: ", end=" ")
    for guess in guesses:
        print(guess, end=" ")
    print()
    print("Correct Answers: ", end=" ")
    for answer in answers:
        print(answer, end=" ")
    print()

    score = int(score / len(questions) *100)
    print(f"Your final Score is {score}%")


questions = ("In what programming language python is written on?",
             "HTML stands for?",
             "CSS stands for?",
             "Four Pillars of Object Oriented Programming?",
             "Python is Used for Machine learning and AI?")
 
choices = (("A. C","B. C++","C. Java", "D. Rust"),
           ("A. Hyper Text Marker Language", "B. Hyper Text Makeup Language "
            ,"C. Hyper Text Markup Language","D. Hyper Text Mark Language"
            ),
           ("A. Cascading Style Shit","B. Cascading Style Shet", 
            "C. Cascading Styles Sheets", "D. Cascading Style Sheets"
            ),
           ("A. Abstract, Inherit, Method, Polymorph",
            "B. Abstraction, Inheritance, Encapsulation, Polymorphism",
            "C. Abstraction, Inheritance, Methods, Polymorphism",
            "D. None of the above"
            ),
           ("A. True","B. False")
           )

answers = ("A","C","D","B","A")
guesses = []
score = 0
quest_num = 0

display_intro()
print()
guesses = display_question_answer(questions,choices, quest_num)

score = scoring(guesses, answers, score)

display_score(score)