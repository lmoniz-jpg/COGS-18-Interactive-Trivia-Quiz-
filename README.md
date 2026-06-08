### COGS-18-Interactive-Trivia-Quiz-

### This project is a multiple choice trivia game! The game randomly selects questions from a question bank, presents them to the player one at a time, the player answers each question, and then the player is given a score at the end. Have fun!

### How to Run

Download and then import Raw_InteractiveTriviaQuiz.ipynb, moduleITG.py, scirptITG.py, testsITG.py

Open Raw_InteractiveTriviaQuiz.ipynb in Jupyter Notebook

Run the import moduleITG cell first

Call moduleITG.play() to start the game

Type 1, 2, 3, or 4 to answer each question

### Files

moduleITG.py — contains all game logic and functions

scriptITG.py — demonstrates each function individually

testsITG.py — unit tests for the module using unittest

Raw_InteractiveTriviaGame.ipynb — main notebook with intro, demo, and tests

### Functions

get_questions — retrieves random questions from the question bank
check_answer — checks if a given answer is correct
calculate_score — calculates the final score and percentage
get_grade — converts a percentage into a letter grade
run_quiz — runs the interactive quiz
play — runs the full game in one function call

### Requirements

Python 3.x
No external libraries required
