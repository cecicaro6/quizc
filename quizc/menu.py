from quizc.console.quiz_ui_handler import *


class Menu(object):
    MENU_PROMPT = "> "

    def __init__(self):
        self.car = ""
        self.quiz = None
        self.quiz_answers = None

    def show_main_menu(self):
        print("""
Quizc - A command quiz utility
======================================
1. Create quiz
2. Fill quiz
3. Show quiz
4. Exit
======================================
        """)

    def process2(self):
        self.show_main_menu()
        option = input(self.MENU_PROMPT)
        should_exit = False
        if option == "1":
            self.quiz = QuizUIHandler.create_quiz()
        elif option == "2":
            if self.quiz is None:
                print("No quiz available, you must create first a quiz")
            else:
                self.quiz_answers = QuizUIHandler.fill_quiz(self.quiz)
        elif option == "3":
            if self.quiz_answers is None:
                print("No filled quiz available, you must create first a quiz")
            else:
                QuizUIHandler.show_quiz(self.quiz_answers)
        elif option == "4":
            should_exit = True

        return should_exit

    def option1(self):
        self.quiz = QuizUIHandler.create_quiz()
        return False

    def option2(self):
        if self.quiz is None:
            print("No quiz available, you must create first a quiz")
        else:
            self.quiz_answers = QuizUIHandler.fill_quiz(self.quiz)
        return False

    def option3(self):
        if self.quiz_answers is None:
            print("No filled quiz available, you must create first a quiz")
        else:
            QuizUIHandler.show_quiz(self.quiz_answers)
        return False

    def option4(self):
        return True

    def process(self):
        self.show_main_menu()
        option = input(self.MENU_PROMPT)
        should_exit = False
        switcher = {
            1: self.option1,
            2: self.option2,
            3: self.option3,
            4: self.option4
        }
        func = switcher.get(option, "option4")  # if not found exit
        result = func()
        return result