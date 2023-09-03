import random

# Define quiz questions and answers
quiz_questions = [
    {
        "question": "What is the capital of France?",
        "choices": ["A) London", "B) Paris", "C) Berlin", "D) Madrid"],
        "correct_answer": "B"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "choices": ["A) Earth", "B) Venus", "C) Mars", "D) Jupiter"],
        "correct_answer": "C"
    },
    {
        "question": "What is 2 + 2?",
        "correct_answer": "4"
    },
    {
        "question": "What is the largest mammal in the world?",
        "choices": ["A) Elephant", "B) Giraffe", "C) Blue Whale", "D) Rhinoceros"],
        "correct_answer": "C"
    },
    {
        "question": "What is the capital of Japan?",
        "choices": ["A) Beijing", "B) Tokyo", "C) Seoul", "D) Bangkok"],
        "correct_answer": "B"
    },
    {
        "question": "Which gas do plants absorb from the atmosphere?",
        "choices": ["A) Oxygen", "B) Nitrogen", "C) Carbon Dioxide", "D) Hydrogen"],
        "correct_answer": "C"
    }
]


# Function to display welcome message and rules
def welcome_message():
    print("Welcome to the Quiz Game!")
    print("You will be asked multiple-choice and fill-in-the-blank questions.")
    print("Type the letter(s) of your answer choice or the answer itself when prompted.")
    print("Let's get started!\n")


# Function to play the quiz
def play_quiz():
    score = 0
    for question in quiz_questions:
        print(question["question"])

        if "choices" in question:
            for choice in question["choices"]:
                print(choice)

        user_answer = input("Your answer: ").strip().upper()

        if user_answer == question.get("correct_answer", "").upper():
            print("Correct!\n")
            score += 1
        else:
            print(f"Incorrect. The correct answer is: {question['correct_answer']}\n")

    return score


# Function to display final results
def display_results(score):
    print(f"Quiz completed! Your final score is: {score}/{len(quiz_questions)}")


# Main game loop
def main():
    welcome_message()

    play_again = True
    while play_again:
        score = play_quiz()
        display_results(score)

        play_again_input = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again_input != "yes":
            play_again = False


if __name__ == "__main__":
    main()
