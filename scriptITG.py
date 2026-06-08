"""Script to run some part of my project."""

# Imports
from module import get_questions, check_answer, calculate_score, get_grade, run_quiz

# Demo 1: get_questions
# Retrieve 3 questions from the bank (no shuffle so output is more predictable)
sample_questions = get_questions(n=3, shuffle=False)

print(f"Retrieved {len(sample_questions)} questions:\n")
for i, q in enumerate(sample questions, start=1):
    print(f"Q{i}: {q['question']}")
    for j, choice in enumerate(q['choices'], start=1):
        marker = "✅" if j - 1 == q['answer'] else "  "
        print(f"  {marker} {j}. {choice}")
    print()

#Demo 2: check_answer
# Test check_answer with a known question
test_q = {
    'question': 'What color is the sky?',
    'choices': ['Red', 'Blue', 'Green', 'Yellow'],
    'answer': 1 # 'Blue' is index 1
}

print("Testing check_answer():")
print(f"  Answering 'Blue' (index 1): {check_answer(test_q, 1)}")   #True
print(f"  Answering 'Red'  (index 0): {check_answer(test_q, 0)}\n")  # False

#Demo 3: calculate_score
# Simulate a results list and calculate the score
mock_results = [True, False, True, True, False]
score = calculate_score(mock_results)

print("calculate_score([True, False, True, True, False]):")
print(f"  Correct:    {score['correct']}")
print(f"  Total:      {score['total']}")
print(f"  Percentage: {score['percentage']}%\n")

# Demo 4: get_grade
# Showing how percentages map to letter grades
test_scores = [100.0, 85.0, 72.0, 65.0, 45.0]

print("get_grade() examples:")
for pct in test_scores:
    grade = get_grade(pct)
    print(f" {pct}% → {grade}")

# Full Interactive Trivia Quiz

print("\n--- Running the full quiz! ---")
questions = get_questions(n=5, shuffle=True)
results = run_quiz(questions)

score = calculate_score(results)
grade = get_grade(score['percentage'])

print(f"\n🏆 Final Score: {score['correct']}/score['total']} ({score['percentage']:.1f}%)")
print(f"Grade: {grade}")


# PYTHON SCRIPT HERE

pass
