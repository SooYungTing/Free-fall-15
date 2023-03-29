import tkinter as tk
from PIL import Image, ImageTk
import sys


class FreefallQuiz:
    def __init__(self):
        self.questions = ["1. What is freefall?",
                          "2. What is the acceleration due to gravity on Earth?",
                          "3. What is the formula for calculating the distance an object falls during freefall?"]

        self.choices = [["A. The motion of an object under the influence of gravity, without any other forces acting on it", "B. The motion of an object under the influence of air resistance", "C. The motion of an object under the influence of both gravity and air resistance"],
                        ["A. 9.8 m/s^2", "B. 10 m/s^2", "C. 8 m/s^2"],
                        ["A. d = 1/2 * g * t^2", "B. d = g * t^2", "C. d = g * t"]]

        self.answers = ["A", "A", "A"]
        self.topics = ["\n-    Freefall",
                       "\n-  Acceleration due to gravity",
                       "\n-    Calculating distance during freefall"]

        self.window = tk.Tk()
        self.window.title("Freefall Theory Quiz")
        self.window.attributes('-fullscreen', True)

        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()

        bg_image = Image.open("Background.png")
        bg_image = bg_image.resize((screen_width, screen_height))
        self.bg_photo = ImageTk.PhotoImage(bg_image)
        canvas = tk.Canvas(self.window, highlightthickness=0)
        canvas.create_image(0, 0, image=self.bg_photo, anchor='nw')
        canvas.pack(fill="both", expand=True)

        # For centering purposes
        half_x = self.window.winfo_screenwidth() // 2
        half_y = self.window.winfo_screenheight() // 2

        # Create label to display title message
        welcome_message = "Quiz"
        canvas.create_text(half_x, 50, text=welcome_message, fill="yellow", font=("Times New Roman", 40, "bold"))

        self.create_widgets()

    def create_widgets(self):
        self.question_labels = []
        self.answer_frames = []
        self.answer_radios = []
        self.answer_vars = []
        question_frame = tk.Frame(self.window)

        for i in range(len(self.questions)):
            question_frame.pack(side="top", padx=10, pady=10, anchor="w") #if removed there is no words/text

            question_label = tk.Label(question_frame, text=self.questions[i], font=("Times New Roman", 15))
            question_label.pack(side="top", anchor="w")
            self.question_labels.append(question_label)

            answer_var = tk.StringVar()
            self.answer_vars.append(answer_var)

            answer_frame = tk.Frame(question_frame)
            answer_frame.pack(side="top", padx=10, pady=5, anchor="w")
            self.answer_frames.append(answer_frame)

            for j in range(len(self.choices[i])):
                answer_radio = tk.Radiobutton(answer_frame, text=self.choices[i][j], font=("Times New Roman", 15), variable=answer_var,
                                              value=chr(65 + j))
                answer_radio.pack(side="top", padx=10, pady=2, anchor="nw")
                self.answer_radios.append(answer_radio)

        self.submit_button = tk.Button(self.window, text="Submit", font=("Times New Roman", 15), command=self.check_answers,
                                     width=12, height=2)
        self.submit_button.pack(side="top", padx=10, pady=10, anchor="se")

    def check_answers(self):
        score = 0
        improvement_topics = []
        for i in range(len(self.questions)):
            user_answer = self.answer_vars[i].get()
            if user_answer == self.answers[i]:
                score += 1
            else:
                improvement_topics.append(self.topics[i])

        self.show_results(score, improvement_topics)

    def show_results(self, score, improvement_topics):
        results_window = tk.Toplevel(self.window)
        results_window.title("Quiz Results")

        score_label = tk.Label(results_window, text=f"Total Marks: {score}/{len(self.questions)}")
        score_label.pack(padx=10, pady=10)

        if improvement_topics:
            topics_label = tk.Label(results_window, text=f"Topics to improve: {', '.join(improvement_topics)}")
            topics_label.pack(padx=10, pady=10)
        else:
            no_topics_label = tk.Label(results_window, text="Great job! You don't need to improve on anything.")
            no_topics_label.pack(padx=10, pady=10)

    def whatOS() -> str:
        os = sys.platform()

        if os == 'Darwin':
            return 'MacOS'
        elif os == 'Windows':
            return 'Windows'
        else:
            return 'Linux'

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    quiz = FreefallQuiz()
    quiz.run()