import random

class Question:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def get_question(self):
        return f"What is {self.num1} + {self.num2}?"

    def check_answer(self, answer):
        return answer == self.num1 + self.num2


class Quiz:
    def __init__(self):
        self.questions = []
        self.score = 0

    def generate_questions(self, num_questions):
        for i in range(num_questions):
            num1 = random.randint(1, 20)
            num2 = random.randint(1, 20)
            self.questions.append(Question(num1, num2))

    def run_quiz(self):
        for question in self.questions:
            print(question.get_question())
            answer = int(input("Enter your answer: "))
            if question.check_answer(answer):
                print("Correct!")
                self.score += 2
            else:
                print("Incorrect!")
        print(f"Your final score is {self.score} out of {len(self.questions) * 2}")


num_questions = int(input("Kaç soru cevaplamak istersin? "))
quiz = Quiz()
quiz.generate_questions(num_questions)
quiz.run_quiz()