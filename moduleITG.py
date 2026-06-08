"""Code for my project."""

import random

# Built-in question bank (list of dicts)
# Each question has: 'question', 'choices' (list of 4), 'answer' (0-indexed int)

Question_Bank = [
    {
        "question": "What is the capital of France?",
        "choices": ["Berlin", "Madrid", "Paris", "Rome"],
        "answer": 2,
    },
    {
        "question": "How many sides does a hexagon have?",
        "choices": ["5", "6", "7", "8"],
        "answer": 1,
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "choices": ["Venus", "Saturn", "Jupiter", "Mars"],
        "answer": 3,
    },
    {
        "question": "Who wrote 'Romeo and Juliet'?",
        "choices": ["Charles Dickens", "William Shakespeare", "Mark Twain", "Homer"],
        "answer": 1,
    },
    {
        "question": "What is the chemical symbol for water?",
        "choices": ["O2", "CO2", "H2O", "HO"],
        "answer": 2,
    },
    {
        "question": "Which ocean is the largest?",
        "choices": ["Atlantic", "Indian", "Arctic", "Pacific"],
        "answer": 3,
    },
    {
        "question": "What year did World War II end?",
        "choices": ["1943", "1944", "1945", "1946"],
        "answer": 2,
    },
    {
        "question": "What is 12 x 12?",
        "choices": ["124", "144", "132", "148"],
        "answer": 1,
    },
    {
        "question": "Which element has the atomic number 1?",
        "choices": ["Helium", "Oxygen", "Carbon", "Hydrogen"],
        "answer": 3,
    },
    {
        "question": "What language is primarily spoken in Brazil?",
        "choices": ["Spanish", "English", "Portuguese", "French"],
        "answer": 2,
    },
]


def get_questions(n=5, shuffle=True):
    """
    Select a subset of trivia questions from the question bank.

    Parameters:
    
    n : int, optional
        Number of questions to return. Must be between 1 and the total
        number of available questions. Default is 5.
    shuffle : bool, optional
        If True, questions are randomly shuffled before selection.
        Default is True.

    Returns:
    
    list of dict
        A list of question dictionaries, each containing:
        - 'question' (str): The question text.
        - 'choices' (list of str): Four answer choices.
        - 'answer' (int): Index (0-based) of the correct choice.

    Raises:
    
    ValueError
        If n is less than 1 or greater than the number of available questions.

    Examples:
    
    >>> questions = get_questions(3)
    >>> len(questions)
    3
    >>> all('question' in q for q in questions)
    True
    """
    if n < 1 or n > len(Question_Bank):
        raise ValueError(
            f"n must be between 1 and {len(Question_Bank)}, got {n}."
        )

    questions = Question_Bank.copy()

    if shuffle:
        random.shuffle(questions)

    return questions[:n]


def check_answer(question, user_answer):
    """
    Check whether the user's answer is correct for a given question.

    Parameters:
   
    question : dict
        A question dictionary with keys 'question', 'choices', and 'answer'.
    user_answer : int
        The 0-based index of the choice selected by the user.

    Returns:
   
    bool
        True if the user's answer matches the correct answer, False otherwise.

    Examples:
    
    >>> q = {'question': 'What color is the sky?',
         'choices': ['Red', 'Blue', 'Green', 'Yellow'],
         'answer': 1}
    >>> check_answer(q, 1)
    True
    >>> check_answer(q, 0)
    False
    """
    return user_answer == question["answer"]


def calculate_score(results):
    """
    Calculate the final score and percentage from a list of results.

    Parameters:
  
    results : list of bool
        A list where each element is True (correct) or False (incorrect),
        representing the outcome of each question.

    Returns:
    
    dict
        A dictionary with the following keys:
        - 'correct' (int): Number of correct answers.
        - 'total' (int): Total number of questions answered.
        - 'percentage' (float): Score as a percentage (0.0 to 100.0).

    Raises:
    
    ValueError
        If results is an empty list.

    Examples:

    >>> calculate_score([True, False, True, True])
    {'correct': 3, 'total': 4, 'percentage': 75.0}
    >>> calculate_score([False, False])
    {'correct': 0, 'total': 2, 'percentage': 0.0}
    """
    if len(results) == 0:
        raise ValueError("results list cannot be empty.")

    correct = sum(results)  # True == 1, False == 0
    total = len(results)
    percentage = (correct / total) * 100

    return {"correct": correct, "total": total, "percentage": percentage}


def get_grade(percentage):
    """
    Convert a numeric score percentage into a letter grade.

    Parameters:
    
    percentage : float
        A score percentage between 0.0 and 100.0 (inclusive).

    Returns:
    
    str
        A letter grade: 'A', 'B', 'C', 'D', or 'F'.

    Raises:
   
    ValueError
        If percentage is outside the range [0, 100].

    Examples:
    
    >>> get_grade(95.0)
    'A'
    >>> get_grade(72.5)
    'C'
    >>> get_grade(50.0)
    'F'
    """
    if not (0.0 <= percentage <= 100.0):
        raise ValueError(f"percentage must be between 0 and 100, got {percentage}.")

    if percentage >= 90:
        return "A"
    elif percentage >= 80:
        return "B"
    elif percentage >= 70:
        return "C"
    elif percentage >= 60:
        return "D"
    else:
        return "F"


def run_quiz(questions):
    """
    Run an interactive trivia quiz in the terminal.

    Displays each question and its multiple-choice options, collects
    user input, and tracks correct/incorrect responses.

    Parameters:
   
    questions : list of dict
        A list of question dictionaries (see get_questions for format).

    Returns:
    
    list of bool
        A list of booleans indicating whether each answer was correct (True)
        or incorrect (False), in the order the questions were presented.

    Notes:
    
    - Accepts input as integers 1-4 (displayed to user as 1-indexed).
    - Reprompts the user if invalid input is entered.
    - Prints immediate feedback after each answer.

    Examples:

    >>> # This function is interactive and requires user input at runtime.
    >>> # It returns a list of booleans, e.g.:
    >>> # [True, False, True, True, True]
    """
    results = []

    print("\n Welcome to the Trivia Quiz Game! ")
    print(f"You'll be answering {len(questions)} questions.\n")
    print("-" * 40)

    for i, q in enumerate(questions, start=1):
        print(f"\nQuestion {i} of {len(questions)}:")
        print(q["question"])

        # Print numbered choices (1-indexed for user friendliness)
        for j, choice in enumerate(q["choices"], start=1):
            print(f"  {j}. {choice}")

        # Collect and validate user input
        while True:
            try:
                raw = input("\nYour answer (1-4): ").strip()
                user_index = int(raw) - 1  # convert to 0-based index
                if user_index not in range(4):
                    print("Please enter a number between 1 and 4.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a number.")

        # Check answer and give feedback
        correct = check_answer(q, user_index)
        results.append(correct)

        if correct:
            print("✅ Correct!")
        else:
            correct_text = q["choices"][q["answer"]]
            print(f"❌ Wrong! The correct answer was: {correct_text}")

    print("\n" + "-" * 40)
    return results

def play():
    # Get 5 random questions from the bank
    questions = get_questions(5)

    # Run the quiz and collect the results
    results = run_quiz(questions)

    # Calculate final score from the results
    score = calculate_score(results)

    # Convert the percentage to a letter grade
    grade = get_grade(score['percentage'])

    #Display final score and grade
    print(f"\n🏆 Final Score: {score['correct']}/{score['total']} ({score['percentage']:.1f}%)")
    print(f"📝 Grade: {grade}")
