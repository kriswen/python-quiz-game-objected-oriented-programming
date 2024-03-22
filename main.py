from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


# create new_question objects from question_data list
# then add it to question_bank list
question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    # create new question object
    new_question = Question(question_text, question_answer)
    # add the new question object to the list
    question_bank.append(new_question)


# QuizBrain
# assign question_bank list to QuizBank
# then loop through all questions in the question_bank/quiz)
quiz = QuizBrain(question_bank)
while quiz.still_has_question():
    quiz.next_question()

final_score = quiz.score
num_of_questions = len(question_bank)  # or num_of_questions = quiz.question_number
print(f"You've completed the quiz")
print(f"Your final score was: {final_score}/{num_of_questions}")
# # easy to use
# print(question_bank[0].answer)

