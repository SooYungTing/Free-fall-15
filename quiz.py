import tkinter as tk
from PIL import Image, ImageTk
import sys


# Define quiz questions and answers
questions = ["1. What is freefall?",
             "2. What is the acceleration due to gravity on Earth?",
             "3. What is the formula for calculating the distance an object falls during freefall?"]

choices = [["A. The motion of an object under the influence of gravity, without any other forces acting on it", "B. The motion of an object under the influence of air resistance", "C. The motion of an object under the influence of both gravity and air resistance"],
           ["A. 9.8 m/s^2", "B. 10 m/s^2", "C. 8 m/s^2"],
           ["A. d = 1/2 * g * t^2", "B. d = g * t^2", "C. d = g * t"]]

answers = ["A", "A", "A"]


# Define function to check answers
def check_answers():
    score = 0
    improvement_topics = []
    for i in range(len(questions)):
        user_answer = answer_vars[i].get()
        if user_answer == answers[i]:
            score += 1
        else:
            improvement_topics.append(topics[i])


    # Open new window for results and topics to improve
    results_window = tk.Toplevel(window)
    results_window.title("Quiz Results")

    score_label = tk.Label(results_window, text=f"Total Marks: {score}/{len(questions)}")
    score_label.pack(padx=10, pady=10)

    if improvement_topics:
        topics_label = tk.Label(results_window, text=f"Topics to improve: {', '.join(improvement_topics)}")
        topics_label.pack(padx=10, pady=10)
    else:
        no_topics_label = tk.Label(results_window, text="Great job! You don't need to improve on anything.")
        no_topics_label.pack(padx=10, pady=10)


# Create window and widgets
window = tk.Tk()
window.title("Freefall Theory Quiz")

# Set window to full screen
window.attributes('-fullscreen', True)

# Get screen dimensions
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# Add background image
background_image = Image.open("Background.png")
background_photo = ImageTk.PhotoImage(background_image)
background_label = tk.Label(window, image=background_photo)
background_label.place(x=0, y=0, width=screen_width, height=screen_height)


question_labels = []
answer_frames = []
answer_radios = []
answer_vars = []
topics = ["\n-    Freefall", "\n-  Acceleration due to gravity", "\n-    Calculating distance during freefall"]

for i in range(len(questions)):
    question_frame = tk.Frame(window)
    question_frame.grid(row=i, column=0, padx=10, pady=10, sticky="w")

    question_label = tk.Label(question_frame, text=questions[i])
    question_label.pack(side="top", anchor="w")
    question_labels.append(question_label)

    answer_var = tk.StringVar()
    answer_vars.append(answer_var)

    answer_frame = tk.Frame(question_frame)
    answer_frame.pack(side="top", padx=10, pady=5, anchor="w")
    answer_frames.append(answer_frame)

    for j in range(len(choices[i])):
        answer_radio = tk.Radiobutton(answer_frame, text=choices[i][j], variable=answer_var, value=chr(65 + j))
        answer_radio.pack(side="top", padx=10, pady=2, anchor="w")
        answer_radios.append(answer_radio)

def whatOS() -> str:
    os = sys.platform()

    if os == 'Darwin':
        return 'MacOS'
    elif os == 'Windows':
        return 'Windows'
    else:
        return 'Linux'

submit_button = tk.Button(window, text="Submit", command=check_answers)
submit_button.grid(row=len(questions), column=0, padx=10, pady=10, sticky="e")

 # create a label to show the result after submission
result_label = tk.Label(answer_frame, text="")
result_label.pack(pady=10)

# pack everything in the answer_frame
question_label.pack(pady=10)
answer_frame.pack(pady=10)

    # run the mainloop
window.mainloop()

