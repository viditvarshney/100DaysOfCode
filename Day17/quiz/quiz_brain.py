class Quiz:
    def __init__(self, questions):
        self.question_number = 0
        self.score = 0
        self.question_list = questions

    def check_answer(self, user_choice, correct_answer):
        """Check the user's Answers"""
        choices = ['true', 'false']

        if user_choice.lower() in choices:
            if user_choice.lower() == correct_answer.lower():
                print("You are Right")
                self.score += 1
            else:
                print("You are Wrong")
            print(
                f"The correct answer is : {correct_answer}")
            print(
                f"Your current score is: {self.score}/{self.question_number}")
            print('\n')
        else:
            print("Invalid Option Selected")

    def next_ques(self):
        """Returns the next question from the question bank."""
        curr_ques = self.question_list[self.question_number]
        self.question_number += 1
        choice = input(
            f"Q.{self.question_number}: {curr_ques.text} (True/False):  ")
        self.check_answer(choice, curr_ques.answer)

    def still_has_ques(self):
        """Return True when the question bank has more questions otherwise False"""
        return self.question_number < len(self.question_list)
