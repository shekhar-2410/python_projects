import random

# Sample questions
questions = {
    "General Knowledge": {
        "easy": {
            "What is the capital of France?": "Paris",
            "What is 5 + 7?": "12"
        },
        "medium": {
            "Who wrote 'To Kill a Mockingbird'?": "Harper Lee",
            "What is the largest ocean on Earth?": "Pacific"
        }
    },
    "Science": {
        "easy": {
            "What planet is known as the Red Planet?": "Mars",
            "What gas do plants absorb from the atmosphere?": "Carbon Dioxide"
        },
        "medium": {
            "What is the chemical symbol for water?": "H2O",
            "How many bones are in the adult human body?": "206"
        }
    }
}

def greet_user():
    print ("welcome to the Quiz Game!")
    print ("Choose a category and difficulty to begin.")

def ask_question(question,answer):
    user_answer = input(question + "")
    return user_answer.strip().lower()== answer.lower()

def run_quiz():
    greet_user()
    score = 0

    #select category and difficulty 
    category = input("Enter a category (General Knowledge or Science): ")
    difficulty = input("Enter a difficulty (easy or medium): ")

    if category in questions and difficulty in questions[category]:
        selected_questions = list(questions[category][difficulty].items())
        random.shuffle(selected_questions)

        for question,answer in selected_questions:
            if ask_question(question,answer):
                print("Correct🎉")
                score += 1
            else:
                print("Incorrect😢")

        print(f"Your score is {score}/{len(selected_questions)}")
    else:
        print("Invalid category or difficulty.")


run_quiz()  
    
     
