class QuizBrain:

    def __init__(self, question_list):  # question_bank (list) will be received in question_list
        self.question_number = 0  # it will be keep incrementing when next_question() method is called
        self.question_list = question_list  # question_bank then get assign to question_list attribute
        self.score = 0  # it will get increment when check_answer() method condition met

    def still_has_question(self):
        """return True/False"""
        return self.question_number < len(self.question_list)

    def next_question(self):
        """print the next question and ask user to answer it"""
        # go to next question and ask user for answer, then check the answer.
        # it also increments question_number before it prints
        # it then call check_answer() method to check the answer
        current_question = self.question_list[self.question_number]
        self.question_number += 1  # need increase question_number everytime called next question
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False):")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        """Take in user_answer and correct_answer and compare if it's same"""
        # it will increment total score when answers are the same
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}")
        print(f"Your current score is {self.score}/{self.question_number}")
        print("\n")

