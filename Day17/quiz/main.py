from data import question_data
from question_model import Question
from quiz_brain import Quiz


question_bank = []

quiz = Quiz(question_bank)

for ques in question_data:
    new_ques = Question(ques["text"], ques["answer"])
    question_bank.append(new_ques)

while quiz.still_has_ques():
    quiz.next_ques()
print('\n')
print("You Have Completed the Quiz.")
print(f"Your Final Score is: {quiz.score}/{quiz.question_number}")
