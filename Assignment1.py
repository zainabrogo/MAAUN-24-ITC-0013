# Function to calculate percentage and display result
def calculate_result(score, total):
    percentage = (score / total) * 100
    print("\nQuiz Completed!")
    print(f"Your Final Score: {score}/{total}")
    print(f"Percentage: {percentage:.2f}%")

    if percentage >= 50:
        print("Status: PASS")
    else:
        print("Status: FAIL")


# List of questions (at least 3 dictionaries)
quiz_questions = [
    {
        "question": "What does VPN stand for?",
        "options": [
            "A. Virtual Private Network",
            "B. Verified Public Network",
            "C. Virtual Public Node",
            "D. Variable Private Network"
        ],
        "correct_answer": "A"
    },
    {
        "question": "Which of the following is a strong password?",
        "options": [
            "A. 12345678",
            "B. password",
            "C. Admin123",
            "D. T9#kL7!q"
        ],
        "correct_answer": "D"
    },
    {
        "question": "What type of attack attempts to trick users into revealing information?",
        "options": [
            "A. Phishing",
            "B. Brute Force",
            "C. DDoS",
            "D. Spoofing"
        ],
        "correct_answer": "A"
    }
]

score = 0
total_questions = len(quiz_questions)

# Loop through questions
for index, question in enumerate(quiz_questions, start=1):
    print(f"\nQuestion {index}: {question['question']}")
    
    for option in question["options"]:
        print(option)

    user_answer = input("Enter your answer (A/B/C/D): ").upper()

    # Evaluate answer
    if user_answer == question["correct_answer"]:
        print("Correct!")
        score += 1
    else:
        print(f"Wrong! Correct answer is {question['correct_answer']}")

# Call result function
calculate_result(score, total_questions)