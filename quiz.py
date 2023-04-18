import tkinter as tk
from PIL import Image, ImageTk
import sys


class FreefallQuiz:
    def __init__(self):
        self.questions = ["1. What is freefall?",
                          "2. Can freefall occur in a vacuum?",
                          "3. What is the formula for calculating the distance an object falls during freefall?",
                          "4. How does air resistance affect freefall?",
                          "5. How does freefall differ on other planets or moons in our solar system?"]

        self.choices = [
            ["A. The motion of an object under the influence of gravity, without any other forces acting on it",
             "B. The motion of an object under the influence of air resistance",
             "C. The motion of an object under the influence of both gravity and air resistance"],
            ["A. Yes, as long as there is gravity present", "B. No, freefall requires a medium like air or water",
             "C. It depends on the temperature of the environment"],
            ["A. d = 1/2 * g * t^2", "B. d = g * t^2", "C. d = g * t"],
            ["A. It increases the acceleration of the object", "B. It decreases the acceleration of the object",
             "C. It depends on the mass of the object"],
            ["A. The acceleration due to gravity is the same on all planets and moons",
             "B. The acceleration due to gravity is higher on larger planets and moons",
             "C. The acceleration due to gravity varies on different planets and moons, depending on their mass and size"]]

        self.answers = ["A", "A", "A", "B", "C"]
        self.topics = ["\n-  Freefall",
                       "\n-  Freefall in vacuum environment",
                       "\n-  Calculating distance during freefall",
                       "\n-  Air resistance effect in freefall",
                       "\n-  Acceleration due to gravity"]

        self.window = tk.Tk()
        self.window.title("Freefall Theory Quiz")
        self.window.attributes('-fullscreen', True)
        self.create_widgets()

    def create_widgets(self):
        self.question_labels, self.answer_frames, self.answer_radios, self.answer_vars = [], [], [], []

        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()

        canvas = tk.Canvas(self.window, highlightthickness=0)
        canvas.pack(fill="both", expand=True)

        bg_image = Image.open("Background.png")
        bg_image = bg_image.resize((screen_width, screen_height))
        self.bg_photo = ImageTk.PhotoImage(bg_image)
        canvas.create_image(0, 0, image=self.bg_photo, anchor='nw')

        half_x = self.window.winfo_screenwidth() // 2

        canvas.create_text(half_x, 50, text="Quiz", fill="yellow", font=("Times New Roman", 40, "bold"))

        for i, question in enumerate(self.questions):
            answer_var = tk.StringVar()
            canvas.create_text(10, 130 + 130 * i, text=question, fill="white",
                               font=("Times New Roman", 20, "bold"), anchor='nw')
            self.answer_vars.append(answer_var)

            for j, choice in enumerate(self.choices[i]):
                answer_text = choice
                text_position = (40, 160) if self.whatOS() == 'Mac' else (50, 160)
                canvas.create_text(text_position[0], text_position[1] + 130 * i + 40 * j, text=answer_text,
                                   fill="white",
                                   font=("Times New Roman", 15), anchor='nw')
                answer_radio_button = tk.Radiobutton(canvas, variable=answer_var, value=chr(65 + j),
                                                     bg=self.get_bg_color())
                answer_radio_button.place(x=18, y=153 + 130 * i + 40 * j + 5)
                self.answer_radios.append(answer_radio_button)

        self.submit_button = tk.Button(canvas, text="Submit", font=("Times New Roman", 15),
                                       command=self.check_answers, width=12, height=2)
        self.submit_button.pack(side="bottom", padx=10, pady=10, anchor="se")

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

        tk.Label(results_window, text=f"Total Marks: {score}/{len(self.questions)}").pack(padx=10, pady=10)

        improvement_text = f"Topics to improve:{''.join(improvement_topics)}" if improvement_topics else "Great job! You don't need to improve on anything."
        tk.Label(results_window, text=improvement_text).pack(padx=10, pady=10)

        import MainPage
        self.window.wait_window(results_window)
        self.window.destroy()
        root = tk.Tk()
        MainPage.MainPageGUI(root)
        root.mainloop()

    def whatOS(self):
        if sys.platform.startswith('darwin'):
            return 'Mac'
        elif sys.platform.startswith('win'):
            return 'Windows'
        elif sys.platform.startswith('linux'):
            return 'Linux'
        else:
            return 'Unknown'

    def get_bg_color(self):
        os = self.whatOS()
        return 'SystemTransparent' if os == 'Mac' else '#011547'

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    quiz = FreefallQuiz()
    quiz.run()