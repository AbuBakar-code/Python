from data import question_data

class Question:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

class BrainQuiz:
    def __init__(self, q_list):
        self.question_no = 0
        self.question_list = q_list
        self.score = 0
    
    def next_question(self):
        current_question = self.question_list[self.question_no]
        self.question_no += 1
        user_answer = input(f"Q{self.question_no}: {current_question.question} (True/False)")
        self.check_answer(user_answer, current_question.answer)
    
    def still_has_question(self):
        if self.question_no < len(self.question_list):
            return True
        else:
            return False
    
    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You've got right answer!")
            self.score += 1
        else:
            print("Wrong answer!")
        print(f"The correct answer is:{correct_answer}")
        print(f"Your current score is : {self.score}/{self.question_no}")

question_bank = []

for q in question_data:
    question_text = q['question']
    answer = q['correct_answer']
    new_question = Question(question_text, answer)
    question_bank.append(new_question)

quiz = BrainQuiz(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print("You've completed the quiz!")
print(f"Your score is: {quiz.score}/{quiz.question_no}")