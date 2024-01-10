from question_class import question_model
from quiz_brain import QuizBrain
from data_api import api_data

# from data import question_data
# from apidata import question_api_data

question_bank = []
for entries in api_data:
    question_text = entries["question"]
    # print(question_text)
    question_answer = entries["correct_answer"]
    # print(question_answer)
    new_question = question_model(q_text=question_text, q_answer=question_answer)
    # print(new_question)
    question_bank.append(new_question)
# print(question_bank)
quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()
#
print("you have completed the quiz")
print(f"your final score was: {quiz.score}/{quiz.question_number} ")

