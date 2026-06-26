import requests
import time
import random
import html
from util_funcs import get_int, get_str, clear_screen, clear_screen_delayed, write_json, load_json
from abc import ABC, abstractmethod
from typing import List, Optional
from pathlib import Path

class OpenTrivia():
    CATEGORIES = {
        9: "General Knowledge",
        10: "Books",
        11: "Film",
        12: "Music",
        13: "Musicals & Theatres",
        14: "Television",
        15: "Video Games",
        16: "Board Games",
        17: "Science & Nature",
        18: "Science: Computers",
        19: "Science: Mathematics",
        20: "Mythology",
        21: "Sports",
        22: "Geography",
        23: "History",
        24: "Politics",
        25: "Art",
        26: "Celebrities",
        27: "Animals",
        28: "Vehicles",
        29: "Comics",
        30: "Science: Gadgets",
        31: "Anime & Manga",
        32: "Cartoons & Animations"
    }


class Player():
    def __init__(self, name) -> None:
        self.name = name
        self.__score = 0

    def add_score(self) -> None:
        self.__score += 1
    def get_score(self) -> int:
        return self.__score

    def reset_score(self) -> None:
        self.__score = 0


class Question(ABC):
    def __init__(self, 
                 question, 
                 correct_answer
                 ) -> None:
        self.question = question
        self.correct_answer = correct_answer

    @abstractmethod
    def display_questions(self) -> None:
        pass

    @abstractmethod
    def check_answer(self, answer) -> bool:
        pass


class MultipleChoiceQuestion(Question):
    def __init__(self, question, correct_answer,choices) -> None:
        super().__init__(question, correct_answer)
        self.choices = choices

    def display_questions(self) -> None:
        print(self.question)
        for index, choice in enumerate(self.choices, start=1):
            print(f"[{index}] {choice}")

    def check_answer(self, answer) -> bool:
        if answer < 1 or answer > len(self.choices):
            return False
        selected_choice = self.choices[answer - 1]
        return selected_choice == self.correct_answer
    
class TrueOrFalseQuestion(Question):

    def display_questions(self) -> None:
        print(self.question)
        print("[1] True")
        print("[2] False")
    
    def check_answer(self, answer) -> bool:
        selected_choice = "True" if answer == 1 else "False" if answer == 2 else None
        return selected_choice == self.correct_answer

class QuizSession():

    def __init__(
        self,
        player:Player,
        questions:List[Question]
        ) -> None:
        
        self.player = player
        self.questions = questions

    def play(self,ui) -> None:
        for number, question in enumerate(self.questions, start=1):
            ui.display_question(number,question,len(self.questions))
            answer = ui.get_answer()

            if self.answer_question(question,answer):
                 ui.display_correct_answer()
            else:
                 ui.display_wrong_answer(question.correct_answer)
            time.sleep(2)
            clear_screen()

    def answer_question(
        self,
        question,
        answer
    ) -> bool:

        if question.check_answer(answer):
            self.player.add_score()
            return True

        return False
         
class ConsoleUi:
    # utility UI
    @staticmethod
    def ask(msg:str) -> None:
        input(f"{msg}")

    # === QuizApp Class Display Section ===
    @staticmethod
    def display_main_menu() -> None:
        print("="*26)
        print("\tQuiz APP")
        print("="*26) 
        print("[1] Start Quiz\n[2] Leaderboard\n[3] Exit")

    @staticmethod
    def display_player_creation_screen() -> None:
        print("="*26)
        print("\tCreate Player")
        print("="*26)

    #Get Quiz Section
    @staticmethod
    def display_quiz_settings_menu() -> None:
        print("="*36)
        print("\tGet Quiz Settings")
        print("="*36)

    @staticmethod
    def display_categories_table() -> None:
        print("Enter the category number you want to select")
        for key,value in OpenTrivia.CATEGORIES.items():
            print(f"{key}: {value}")


        # === QuizApp Class Function startSession() section ===
    @staticmethod
    def display_question(number,question,total) -> None:
        print(f"\nQuestion {number}/{total}")
        question.display_questions()

    @staticmethod
    def get_answer() -> int:
        return get_int("Answer:")

    @staticmethod
    def display_correct_answer() -> None:
        print("Correct!")

    @staticmethod
    def display_wrong_answer(correct_answer) -> None:
        print(f"Wrong! The correct answer was: {correct_answer}")
        # === End of QuizApp Class Function startSession() section ===
    
    # === End of  QuizApp Class Display Section ===



    # === OpenTriviaApi Class Display Section ===
    @staticmethod
    def display_req_error(e) -> None:
        print(f"Error fetching quiz: {e}")
    @staticmethod
    def display_no_data():
        print("No questions found for the selected settings.")
    # === End of OpenTriviaApi Class Display Section ===

    # === Leaderboard Class Section ===
    @staticmethod
    def display_leaderboard(scores:dict) -> None:
        print("="*26)
        print("\tLeader Board")
        print("="*26)
        if scores:
            for name, score in sorted(
                scores.items(),
                key=lambda item: item[1],
                reverse=True
            ):
                print(f"{name}: {score}")
        else:
            print("No scores yet.")
    # === End of Leaderboard Class Section ===

class Leaderboard():

    FILE_PATH = Path(__file__).parent / "leaderboard.json"
    #store incoming player object attr in a dictionary
    def __init__(self) -> None:
        self.scores = {}
        self.load_leaderboard()
    
    def add_score(self, player:Player) -> None:
        """
        Get player object together with score
        if player object already exist, get's the highest score
        saves the from score dict var to by calling save_leaderboard()
        """
        self.scores[player.name] = max(
            self.scores.get(player.name, 0),
            player.get_score()
        )
        self.save_leaderboard()

    def save_leaderboard(self) -> None:
        """
        call write_json() to save the scores dict var to a json file
        """
        write_json(self.FILE_PATH, self.scores, "leaderboard.json",feedback=False)

    def load_leaderboard(self) -> None:
        """
        call load_json() to load the scores and store it in leaderboard class object attr scores
        """
        self.scores = load_json(self.FILE_PATH,"leaderboard.json")

class OpenTriviaApi:

    def build_api_url(self, settings) -> str:
        url = f"https://opentdb.com/api.php?amount={settings.amount}"

        if settings.category:
            url += f"&category={settings.category}"

        if settings.difficulty:
            url += f"&difficulty={settings.difficulty}"

        if settings.q_type:
            url += f"&type={settings.q_type}"

        return url
    
    @staticmethod
    def parse_question(item) -> Optional[Question]:
        question_text = html.unescape(item["question"])
        correct_answer = html.unescape(item["correct_answer"])
        question_type = item["type"]
        if question_type == "multiple":

            choices = [
                html.unescape(choice)
                for choice in item["incorrect_answers"]
            ]

            choices.append(correct_answer)
            random.shuffle(choices)

            return MultipleChoiceQuestion(
                question_text,
                correct_answer,
                choices
            )

        elif question_type == "boolean":

            return TrueOrFalseQuestion(
                question_text,
                correct_answer
            )

        return None

    def fetch_quiz(self, settings) -> List[Question]:
        for attempt in range(3):
            try:
                response = requests.get(
                    self.build_api_url(settings),
                    timeout=10
                )
                response.raise_for_status()
                break
            except requests.RequestException as e:
                ConsoleUi.display_req_error(e)
                time.sleep(2)
        else:
            return []

        data = response.json()

        if data["response_code"] != 0:
            ConsoleUi.display_no_data()
            ConsoleUi.ask("Press Enter to get quiz settings again.")
            return []

        questions = [
            question
            for item in data["results"]
            if (question := self.parse_question(item)) is not None
        ]

        return questions

class QuizSettings:
    VALID_DIFFICULTIES = ["easy", "medium", "hard"]
    VALID_TYPES = ["multiple", "boolean"]

    def __init__(self, amount, category, difficulty, q_type) -> None:
        self.amount = amount
        self.category = category
        self.difficulty = difficulty
        self.q_type = q_type

    @classmethod
    def create(cls, amount, category, difficulty, q_type, categories) -> Optional['QuizSettings']:
        # Default values
        amount = 10 if amount.strip() == "" else amount
        category = None if category.strip() == "" else category
        difficulty = None if difficulty.strip() == "" else difficulty.lower()
        q_type = None if q_type.strip() == "" else q_type.lower()

        # Amount validation
        if not str(amount).isdigit() or int(amount) <= 0:
            print("Amount must be a positive integer.")
            return None

        # Category validation (ID)
        if category is not None:
            if not category.isdigit():
                print("Category must be a number.")
                return None

            category = int(category)

            if category not in categories:
                print("Invalid category ID.")
                return None

        # Difficulty validation
        if difficulty is not None and difficulty not in cls.VALID_DIFFICULTIES:
            print("Invalid difficulty.")
            return None

        # Type validation
        if q_type is not None and q_type not in cls.VALID_TYPES:
            print("Invalid question type.")
            return None

        return cls(
            int(amount),
            category,
            difficulty,
            q_type
        )

class QuizApp():


    def __init__(self,api:OpenTriviaApi, leaderboard:Leaderboard, ui:ConsoleUi) -> None:
        self.player = None
        self.api = api
        self.leaderboard = leaderboard
        self.ui = ui


    def redraw_settings_screen(self) -> None:
        """Got Roasted by clanker becoz of these"""
        clear_screen()
        self.ui.display_quiz_settings_menu()
        
    def get_quiz_settings(self) -> QuizSettings:
        while True:
            self.ui.display_quiz_settings_menu()
            print("Press Enter for defaults.")
            print("Amount: 10 | Category: Any | Difficulty: Any | Type: Any\n")

            amount = get_str("Number of Questions")

            self.redraw_settings_screen()
            self.ui.display_categories_table()
            category = get_str("Select Category")

            self.redraw_settings_screen()
            difficulty = get_str(
                "Select Difficulty (easy/medium/hard)"
            )

            self.redraw_settings_screen()
            q_type = get_str(
                "Select Type (multiple/boolean)"
            )

            settings = QuizSettings.create(
                amount,
                category,
                difficulty,
                q_type,
                OpenTrivia.CATEGORIES
            )

            if settings:
                return settings

            print("\nInvalid settings. Please try again.")
            time.sleep(2)
            clear_screen()

        
    def show_results(self) -> None:
        print(f"Player: {self.player.name}")
        print(f"Score: {self.player.get_score()}")
        self.leaderboard.add_score(self.player)


    def create_player(self) -> None:
        self.ui.display_player_creation_screen()
        while True:
            name = input("Enter Name: ").strip()

            if name:
                break

            print("Name cannot be empty.")

        self.player = Player(name)

    def start_quiz(self) -> None:
        clear_screen()
        self.create_player()

        while True:
            clear_screen()
            settings = self.get_quiz_settings()
            clear_screen()
            questions = self.api.fetch_quiz(settings)

            if questions:
                break

        session = QuizSession(
            self.player,
            questions
        )

        session.play(self.ui)

        self.show_results()
        input("Enter to Main Menu")
        clear_screen()

    def run(self) -> None:

        clear_screen_delayed(1)
        while True:
            self.ui.display_main_menu()
            choice = get_int("Enter Choice:")

            if choice == 1:
                self.start_quiz()
            elif choice == 2:
                clear_screen()
                self.ui.display_leaderboard(self.leaderboard.scores)
                input("Enter to go back")
                clear_screen()
            elif choice == 3:
                print("Exiting..")
                time.sleep(1)
                break
            else:
                print("Invalid Command")
                clear_screen_delayed(1)

def main():
    app = QuizApp(OpenTriviaApi(), Leaderboard(),ConsoleUi())
    app.run()

if __name__ == '__main__':
    clear_screen()
    main()