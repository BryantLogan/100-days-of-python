from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:


    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        # Creating the window
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg= THEME_COLOR)
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.canvas.grid(column=0, row=1, columnspan=2, sticky="EW")

        # Creating the True/False Buttons
        true_button_img = PhotoImage(file="Day 34 - API Practice and GUI Quiz App\images\\true.png")
        self.true_button = Button(image=true_button_img,highlightthickness=0, command=self.is_true)
        self.true_button.grid(column=0, row=2)
        
        false_button_img = PhotoImage(file="Day 34 - API Practice and GUI Quiz App\images\\false.png")
        self.false_button = Button(image=false_button_img,highlightthickness=0, command=self.is_false)
        self.false_button.grid(column=1, row=2)

        # Creating the question text
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Example Text", 
            fill=THEME_COLOR, 
            font= ("Arial", 20, "italic")
        )
        self.canvas.grid(column=0, row=1, columnspan=2, sticky="EW", pady=50)
        
        # Creating the score label
        self.score_label = Label(text="Score: 0", fg="white", bg= THEME_COLOR)
        self.score_label.grid(column=1, row=0)

        # Calling next question function
        self.get_next_question()

        self.window.mainloop()

    
    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text= q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
    
    def is_true(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def is_false(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)
    
    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
