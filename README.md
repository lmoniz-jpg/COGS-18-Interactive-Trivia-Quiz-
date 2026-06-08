### COGS-18-Interactive-Trivia-Quiz-

### This project is a multiple choice trivia game! The game randomly selects questions from a question bank, presents them to the player one at a time, the player answers each question, and then the player is given a score at the end. Have fun!

### How to Run

Open Raw_InteractiveTriviaQuiz.ipynb in Jupyter Notebook
Run the import module cell first
Call module.play() to start the game
Type 1, 2, 3, or 4 to answer each question

###Files

module.py — contains all game logic and functions
script.py — demonstrates each function individually
tests.py — unit tests for the module using unittest
ProjectNotebook.ipynb — main notebook with intro, demo, and tests

###Functions

get_questions — retrieves random questions from the question bank
check_answer — checks if a given answer is correct
calculate_score — calculates the final score and percentage
get_grade — converts a percentage into a letter grade
run_quiz — runs the interactive quiz
play — runs the full game in one function call

###Requirements

Python 3.x
No external libraries required
