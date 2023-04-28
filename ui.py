THEME_COLOR = "#375362"
from tkinter import *
from quiz_brain import QuizBrain
class QuizInterface:
    def __init__(self,quiz_brain: QuizBrain):
        self.quiz =quiz_brain
        self.window = Tk()
        self.window.title("Quizler")
        self.window.config(padx=20,pady=20,background=THEME_COLOR)
        self.score = Label(text="Score: 0",fg="white",bg=THEME_COLOR)
        self.score.grid(row=0,column=1)
        self.canvas = Canvas(height=250,width=300,background="white")
        self.question = self.canvas.create_text(150,
                                                125,
                                                width=280,
                                                text="Questions",
                                                fill=THEME_COLOR,
                                                font=("Arial",20,"italic"))
        self.right = PhotoImage(file="images/false.png")
        self.wrong = PhotoImage(file="images/true.png")
        self.b_1 = Button(image=self.right,background=THEME_COLOR,highlightthickness=0,command=self.true_press)
        self.b_2 = Button(image=self.wrong, background=THEME_COLOR,highlightthickness=0,command=self.false_press)
        self.canvas.grid(row=1,column=0,columnspan=2,pady=50)
        self.b_1.grid(row=2,column=0)
        self.b_2.grid(row=2,column=1)
        self.get_next_question()
        self.window.mainloop()
    def get_next_question(self):
        self.canvas.config(background="white")
        if self.quiz.still_has_questions():
            self.score.config(text=f"Score: {self.quiz.s}")
            q_t = self.quiz.next_question()
            self.canvas.itemconfig(self.question,text=q_t)
        else:
            self.canvas.itemconfig(self.question,text="The End")
            self.b_1.config(state="disabled")
            self.b_2.config(state="disabled")
    def true_press(self):
        i_r=self.quiz.check_answer("True")
        self.feedback(i_r)
    def false_press(self):
        i_r=self.quiz.check_answer("False")
        self.feedback(i_r)
    def feedback(self,i_r):
        if i_r:
            self.canvas.config(background="green")
        else:
            self.canvas.config(background="red")
        self.window.after(1000,self.get_next_question)





